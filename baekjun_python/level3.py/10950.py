# 10950

T = 5
print("{}".format(T))
A = list(range(T))
B = list(range(T))
for i in range(T):
    A_temp, B_temp = map(int, input().split())
    A[i] = A_temp
    B[i] = B_temp


for i in range(T):
    value = int(A[i]) + int(B[i])
    print(value)
