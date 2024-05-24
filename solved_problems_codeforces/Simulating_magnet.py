import numpy as np

length = 10
num = length ** 2
randphi = 2 * np.pi * np.random.rand(num).reshape(length, length,1)
randtheta = np.pi * np.random.rand(num).reshape(length, length,1)
mag= np.array([np.cos(randphi)*np.sin(randtheta), np.sin(randphi)*np.sin(randtheta), np.cos(randtheta)])
# print(mag.shape)
# print(mag[0,:]**2+mag[1,:]**2+mag[2,:]**2)
x=np.random.rand(10)
print(x)
print(np.random.rand())