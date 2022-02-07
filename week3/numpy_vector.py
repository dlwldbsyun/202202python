
import numpy as np

def l1_norm(x):
    x_norm = np.abs(x)
    x_norm = np.sum(x_norm)
    return x_norm

def l2_norm(x):
    x_norm = x*x
    x_norm = np.sum(x_norm)
    x_norm = np.sqrt(x_norm)
    return x_norm
    
# print(l1_norm(x))
# print(l2_norm(x,y))

def angle(x,y):
    v = np.inner(x, y) / (l2_norm(x) * l2_norm(y)) # inner:내적함수(정사영된 벡터의 길이)
    theta = np.arccos(v)
    return theta

x = np.array([0,1],int)
y = np.array([0,2],int)
print(angle(x,y))

z = np.array([1,-1,1,-1],int)
w = np.array([4,-4,4,-4],int)
print(np.inner(z,w))