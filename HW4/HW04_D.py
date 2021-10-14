class Fraction:
    # 분자를 0, 분모를 1이라는 default값으로 초깃값을 설정합니다. 
    def __init__(self, numerator=0, denominator=1):
        self._numerator = numerator
        self._denominator = denominator
    # 분자 세터를 설정합니다. 
    def setNumerator(self, numerator):
        self._numerator = numerator
    # 분자 게터를 만듭니다.
    def getNumerator(self):
        return self._numerator
    # 분모 세터를 설정합니다. 
    def setDenominator(self, denominator):
        self._denominator = denominator
    # 분모 게터를 만듭니다. 
    def getDenominator(self):
        return self._denominator
    # 분자, 분모의 최대공약수를 리턴합니다. 
    def GCD(self, m, n): 
        while n != 0:
            t = n
            n = m % n
            m = t
        return m
    # 분자 분모를 약분합니다. 
    def reduce(self):
        # 우선 게터를 통해 분자, 분모를 받아오고 
        n=self.getNumerator()
        d=self.getDenominator()
        # 게터를 통해 받아온 분자, 분모를 GCD함수의 인자에 넣어 최대공약수를 gcd에 저장합니다. 
        gcd = self.GCD(n,d)
        # 분자, 분모를 gcd로 약분한 값을 각각 num과 den에 저장합니다. 
        num=n/gcd
        den=d/gcd
        # 세터에 num과 den을 각각 전달합니다. 
        self.setNumerator(int(num))
        self.setDenominator(int(den))

def main():
    #분자와 분모를 int로 입력받습니다. 
    num = int(input("Enter numerator of fraction: "))
    den = int(input("Enter denominator of fraction: "))
    #분자가 num이고 분모가 den인 객체 f를 생성합니다. 
    f = Fraction(num, den)
    #객체 f의 분자 분모가 약분되도록 reduce()함수를 작동시킵니다. 
    f.reduce()
    #객체 f의 분자 분모를 받아와 예시 출력 형태처럼 출력되도록 작성합니다. 
    print("Reduction to lowest terms: {0}/{1}".format(f.getNumerator(),f.getDenominator()))
main()
