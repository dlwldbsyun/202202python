# differentiation, gradient vector
from mimetypes import init
import sympy as sym
from sympy.abc import x, y
# import numpy as np

# print(sym.diff(sym.poly(x**2 + 2*x +3),x))

# 미분을 어디에 쓸까
# 만약에 미분값이 음수일때 x에 미분값을 더하면 왼쪽으로 가고 함숫값은 증가
# 만약에 미분값이 양수일때 x에 미분값을 더하면 오른쪽으로 가고 함숫값은 증가
# 미분을 통해 어디로 값을 이동할지 예측

# 경사하강법
# def func(val):
#     fun = sym.poly(x**2 + 2*x +3)
#     return fun.subs(x,val),fun

# def func_gradient(fun,val):
#     _, function = fun(val)
#     diff = sym.diff(function, x)
#     return diff.subs(x, val), diff

# def gradient_descent(fun, init_point, lr_rate=1e-2, epsilon=1e-5):
#     cnt = 0
#     val = init_point
#     diff, _ = func_gradient(fun, init_point)
#     while np.abs(diff) > epsilon:
#         val = val - lr_rate*diff
#         diff, _ = func_gradient(fun, val)
#         cnt += 1

#     print("함수: {}, 연산횟수: {}, 최소점: ({}, {})".format(fun(val)[1],cnt,val, fun(val)[0]))

# gradient_descent(fun=func, init_point=np.random.uniform(-2,2))

# 편미분

print(sym.diff(sym.poly(x**2 + 2*x*y +3)+sym.cos(x+ 2*y),x))