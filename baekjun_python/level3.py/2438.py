# 2438

N = int(input())

for i in range(1, N+1):
    print('*' * i)

# comprehension
[print('*'*i) for i in range(1, int(input())+1)]