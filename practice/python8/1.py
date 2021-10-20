#1. numpy- ARRAYS
import numpy as np
import matplotlib.pyplot as pl

a1= np.array([1,2,3])
a2= np.array([[1,2],[3,4]])
a3= np.array([1,2,3,4,5], ndmin=3)
# ndmin 차원으로 출력해라 
a4= np.array([1,2,3],dtype=complex)
# complex -> 복소수 차원으로 출력해라 
print (a1)
print (a2)
print (a3)
print (a4,"\n")

#2. numpy- Array creation
b1=np.arange(12)
b2=np.arange(2,9,3)
b3=np.ones(3) #float가 디폴트임 
b4=np.zeros(6)
b5=np.linspace(10,20,5)
print(b1)
print(b2)
print(b3)
print(b4)
print(b5,"\n")

#3. numpy- reshape
c1= b1.reshape(3,4)
print("\nc1= ",c1)
print(c1[2,1]) # 9를 뜻함
print(c1[:,1]) # 1,5,9를 뜻함 
print(np.shape(c1)) #(3,4)의 모양이라는 걸 출력함 dimesion !!
print(np.size(c1)) # 12
print(np.ndim(c1),"\n") # 2차원

#4. numpy - Matrix
m1 = np.eye(3) # identity matrix
m2 = np.eye(3,4)
m3 = np.array([[1,2],[3,4]])
m4 = np.array([[11,12],[13,14]])

print(m1)
print(m2)

print(m3+m4) # 그냥 점끼리만 더헤진거 
print(m3*m4) # 그냥 점끼리만 곱해진거 
print(np.dot(m3,m4)) # 행렬의 곱
print(np.inner(m3,m4)) # 행렬의 곱을 가로가로 세로세로 한거 

#5. numpy - mathematical function
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
n = np.around(a) # 가까운 수로 반올림 -2. 2. -0. 1. 10.
c = np.floor(a) # 크지 않은 최대 정수 -2. 1. -1. 0. 10.
d = np.ceil(a) #  올림 작지 않은 최소 -1. 2. -0. 1. 10.

a = np.array([1.0, 5.55, 123, 0.597, 25.532])
b = np.around(a) # 1. 6. 123. 1. 26.
c = np.around(a, decimals=1) # 1. 5.6 123. 0.6 25.5
d = np.around(a, decimals=-1) # 0. 10.120. 0. 30. *****여기 어렵구만***

a = np.array([[3,7,5],[8,4,3],[2,4,9]])
d = np.amin(a) #2
e = np.amax(a) #9
b = np.amin(a,1) # 1은 가로 방향 이라는 뜻이고 
# 3 3 2
c = np.amin(a,0) # 0은 세로 방향 이라는 뜻이다.
# 2 4 3
k = np.average(a) # 평균
e = np.std(a) # 표준편차
g = np.var(a) # 분산

#6. numpy - random numbers
b= np.random.rand(3,2) # 0부터 1까지의 수를 3행 2열로 표현 
c= np.random.randint(5, size=(2,4)) # 0부터 4까지의 정수를 (2,4)행렬로 랜덤하게 

#7. numpy - linear algebra
a = np.array([[1,2],[3,4]])
b = np.array([[-4],[1]])
c = np.linalg.inv(a) # a의 inverse matrix
d = np.linalg.eig(a) # a의 eigenvalues and eigenvectors of a
x = np.linalg.solve(a,b) # ax = b 가 되는 x 구하기 

#8. numpy - MatPlotLib

gaussian = lambda x: np.exp(-(0.5-x)**2/1.5)
x= np.arange(-2,2.5, 0.01)
y= gaussian(x)

pl.figure()
pl.plot(x,y)
pl.xlabel('x values')
pl.ylabel('exp(-(0.5-x)**2/1.5)')
pl.title("Gaussian Function")
pl.show()
