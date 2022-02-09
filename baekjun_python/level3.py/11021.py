# 11021
# import sys

# T = int(input())
# A = list(range(T))
# B = list(range(T))

# for i in range(T):
#     a, b = map(int, sys.stdin.readline().split())
#     A[i] = a
#     B[i] = b

# for i in range(T):
#     print("Case #{} : {}".format(i+1,A[i]+B[i]))

t = int(input())

for i in range(t):
    i += 1
    a, b = map(int, input().split())
    print("Case #%s: %s" %(i, a+b))