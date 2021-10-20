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
print(m3+m4)
print(m3*m4)
print(np.dot(m3,m4))
print(np.inner(m3,m4))