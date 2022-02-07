import numpy as np

X = np.array([[1,-2,3],[7,5,0],[-2,-1,2]])
Y = np.array([[0,1],[1,-1],[-2,1]])

print("행렬 곱 : \n", X @ Y) # numpy에서는 @이가 행렬의 곱

# inner: X행렬과 Y전치행렬을 내적함

Y = np.array([[0,1,-1],[1,-1,0]])
print("행렬 내적 : \n",np.inner(X,Y))

# 역행렬

print(np.linalg.inv(X)) # 역행렬
print(X @ np.linalg.inv(X))

# 유사역행렬
# 만일 역행렬을 계산할 수 없다면 유사역행렬 또는 무어-펜로즈 역행렬을 이용

Y = np.array([[0,1],[1,-1],[-2,1]])

print(np.linalg.pinv(Y))
print(np.linalg.pinv(Y) @ Y)

