from turtle import shape
import numpy as np

# arr1 = np.random.random((3,5))
# arr2 = np.random.random((2,3))

# dot = np.transpose(arr1) @ np.transpose(arr2)

# print(dot,dot.shape)

# arr1 = np.array([[5,7],[9,11]], float)
# arr2 = np.array([[2,4],[6,8]],float)

# concat_1 = np.concatenate((arr1, arr2), axis=0)
# concat_2 = np.concatenate((arr1, arr2), axis=1)

# print(concat_1)
# print(concat_2)

xy = np.array([[1.,2.,3.,4.,5.,6.],[10.,20.,30.,40.,50.,60.]])

x_train = xy[0,]
y_train = xy[1,]


print(x_train,x_train.shape)
print(y_train,y_train.shape)


