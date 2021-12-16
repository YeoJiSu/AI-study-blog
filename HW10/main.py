import numpy as np

def main():
    print()
    print("Which learning algorithm do you want to use?")
    print(" 1. Linear Regression")
    print(" 2. K-NN")
    aType = int(input("Enter the number: "))

    if aType == 1: 
        ml = LinearRegression()
    elif aType == 2:
        ml = KNN()
    fileName = input("Enter the file name of training data: ")
    ml.setData('train', fileName)
    fileName = input("Enter the file name of test data: ")
    ml.setData('test', fileName)
    ml.buildModel()
    ml.testModel()
    ml.report()

class ML:
    def __init__(self):
        self._trainDX = np.array([]) # Feature value matrix (training data)
        self._trainDy = np.array([]) # Target column (training data)
        self._testDX = np.array([])  # Feature value matrix (test data)
        self._testDy = np.array([])  # Target column (test data)
        self._testPy = np.array([])  # Predicted values for test data

    def setData(self, dtype, fileName): # set class variables
        XArray, yArray = self.createMatrices(fileName)
        if dtype == 'train':
            self._trainDX = XArray
            self._trainDy = yArray
        elif dtype == 'test':
            self._testDX = XArray
            self._testDy = yArray
            self._testPy = np.zeros(np.size(yArray)) # Initialize to all 0
            
    def createMatrices(self, fileName): # Read data from file and make arrays
        infile = open(fileName, 'r')
        XSet = []
        ySet = []
        for line in infile:
            data = [float(x) for x in line.split(',')]
            features = data[0:-1]
            target = data[-1]
            XSet.append(features)
            ySet.append(target)
        infile.close()
        XArray = np.array(XSet)
        yArray = np.array(ySet)
        return XArray, yArray

    def testModel(self):
        n = np.size(self._testDy)
        for i in range(n):
            self._testPy[i] = self.runModel(self._testDX[i])
                
    def report(self):
        n = np.size(self._testDy) # Number of test data
        totalSe = 0
        for i in range(n):
            se = (self._testDy[i] - self._testPy[i]) ** 2
            totalSe += se
        rmse = np.sqrt(totalSe) / n
        print()
        print("RMSE: ", round(rmse, 2))
        
class LinearRegression(ML):
    def __init__(self):
        super().__init__()
        self._w = np.array([]) # Optimal weights for linear regression
        
    def buildModel(self): # Do linear regression and return optimal w
        X = self._trainDX
        n = np.size(self._trainDy)
        X0 = np.ones([n, 1])
        nX = np.hstack((X0, X)) # Add a column of all 1's as the first column
        y = self._trainDy
        t_nX = np.transpose(nX)
        self._w = np.dot(np.dot(np.linalg.inv(np.dot(t_nX, nX)), t_nX), y)
        return self._w
    
    def runModel(self, data): # Apply linear regression to a test data
        nData = np.insert(data, 0, 1)
        return np.inner(self._w, nData)
        
class KNN(ML):
    def __init__(self):
        super().__init__()
        self._k = 0            # k value for k-NN
        
    def buildModel(self):
        self._k = int(input("Enter the value for k: "))
        
    def runModel(self, query):
        # 인자 query는 testDx 값임. 
        # query 와 가장 가까이 있는 이웃한 train값들이 closetK 변수에 저장.
        closetK = self.findCK(query)
        # closestK의 값(거리) 평균을 predict 변수에 저장.
        predict = self.takeAvg(closetK)
        return predict

    # findCK 함수 작성하기 
    # query (= testDx[i] ) 와 가장 가까이 있는 (이웃한) K개의 trainDx[i] 찾기 (→closestK)
    def findCK(self, query):
        # train 데이터 개수를 변수 m에 저장
        m = np.size(self._trainDy)
        # 몇개의 단위로 clusturing 할 것인지 k에 저장
        k = self._k
        # closetK는 2 X 2 matrix가 되게끔 
        closestK = np.arange( 2 * k).reshape(k,2)
        for i in range(k):
            closestK[i,0] = i
            # closestK 변수에 index 마다 거리를 다 저장해둔다. 
            closestK[i,1] = self.sDistance(self._trainDX[i],query)
        for i in range(k,m):
            # k번째 다음것과의 거리 구해서, 거리가 현재 closestK의 거리보다 작으면 업데이트
            self.updateCK(closestK, i, query)
        return closestK
    
    # sDistance 작성하기
    # trainDx[i]와 query(=testDx[i] )의 거리 구하는 함수
    def sDistance(self, dataA, dataB):
        # x, y, z 등 차원이 있을 것이므로 차원을 변수 dim 에 저장
        dim = np.size(dataA)
        # 거리를 저장할 변수 sumOfSquares를 0으로 초기화 
        sumOfSquares = 0
        for i in range(dim):
            # 거리 구하는 공식을 이용해 거리들 모두 합하기 
            sumOfSquares += (dataA[i]- dataB[i])**2
        return sumOfSquares
    
    # updateCK 함수 작성하기 
    # k번째 다음것과의 거리 구해서, 거리가 현재 closestK의 거리보다 작으면 업데이트
    def updateCK(self, closestK, i, query):
        # 거리를 d 변수에 저장
        d = self.sDistance(self._trainDX[i], query)
        for j in range(len(closestK)):
            # closetK 거리가 d보다 크다면 값을 d로 바꾸어준다. 
            if closestK[j,1] > d:
                closestK[j,0] = i
                closestK[j,1] = d
                break
    
    #takeAvg 함수 작성하기 
    #찾은 closestK의 값 (거리) 평균 구하기(→ predict)
    def takeAvg(self, closestK):
        k = self._k
        total = 0
        for i in range(k):
            # k의 개수만큼 train 데이터들을 다 더해서 
            j = closestK[i, 0]
            total += self._trainDy[j]
        # k 로 나누어줘서 평균을 구한다.
        return total / k

main()
