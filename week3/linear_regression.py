import numpy as np
import sympy as sym
from sympy.abc import x

xy = np.array([[1.,2.,3.,4.,5.,6.],[10.,20.,30.,40.,50.,60.]])

x_train = xy[0,]
y_train = xy[1,]

# 직선의 기울기 weight
# y절편의 값 bias

weight = sym.diff(sym.poly())

print(x_train,x_train.shape)
print(y_train,y_train.shape)

X = np.array([[1,1],[1,2],[2,2],[2,3]])
y = np.dot(X,np.array([1,2])) + 3

beta_gd = [10.1, 15.1, -6.5] # [1,2,3]이 정답
X_ = np.array([np.append(x,[1]) for x in X])

for t in range(5000):
    error = y - X_ @ beta_gd
    grad = -np.transpose(X_) @ error
    beta_gd -= 0.01*grad

print(beta_gd)