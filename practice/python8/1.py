#1. numpy- ARRAYS
import numpy as np
a1= np.array([1,2,3])
a2= np.array([[1,2],[3,4]])
a3= np.array([1,2,3,4,5], ndmin=3)
# ndmin 차원으로 출력해라 
a4= np.array([1,2,3],dtype=complex)
# complex -> 복소수 차원으로 출력해라 
print (a1)
print (a2)
print (a3)
print (a4)

#2. numpy- Array creation
b1=np.arange(10)
b2=np.arange(2,9,3)
b3=np.ones(3) #float가 디폴트임 
b4=np.zeros(6)
print(b1)
print(b2)
print(b3)
print(b4)