# 15552
# input은 입력한 표현식 문자열로 변환 후 타입 캐스팅으로 int로 재변환해야하므로
# 다량의 반복이 들어갈 경우 runtime error가 발생
import sys

T = int(input())
print(T)

A = list(range(T))
B = list(range(T))

for i in range(T):
    A_temp, B_temp = map(int, sys.stdin.readline().split())
    A[i] = A_temp
    B[i] = B_temp

for i in range(T):
    value = A[i] + B[i]
    print(value)