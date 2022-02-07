# 2588

# a = int(input())
# b = int(input()) # b = 325
# print(a*(b%10)) # b % 10 = 5 
# print(a * ((b//10)-((b//100)*10))) # (b//10)-((b//100)*10) = 32 - 30 = 2
# print(a * (b//100)) # b // 100 = 3
# print(a * b)

# 1330

# a, b = map(int, input().split()) # map(적용할 함수, 반복가능한 리스트)
# if a > b:
#     print(">")
# elif a < b:
#     print("<")
# elif a == b:
#     print("==")

# 9498

# score = int(input())
# if 90<=score & score<=100:
#     print("A")
# elif 80<=score:
#     print("B")
# elif 70<=score:
#     print("C")
# elif 60<=score:
#     print("D")
# else:
#     print("F")

# 2753

# year = int(input())

# if year%4==0:
#     if year%100!=0:
#         print("1")
#     elif year%400==0:
#         print("1")
#     else:
#         print("0")
# else:
#     print("0")

# 14681

# x = int(input())
# y = int(input())

# if x>0 and y>0:
#     print("1")
# elif x<0 and y>0:
#     print("2")
# elif x<0 and y<0:
#     print("3")
# else:
#     print("4")

# 2884

# hour, min= map(int, input().split())

# if min >= 45:
#     min = min-45
#     print(f"{hour} {min}")
# elif hour>=1 and min < 45:
#     print(f"{hour-1} {min+15}")
# else:
#     print("{} {}".format(23,min+15))

# 2739

# N = int(input())

# for i in range(1,10):
#     print(f"{N} * {i} = {N*i}")

# 10950

T = 5
print(f"{T}")

for i in range(T):
    A, B = list(map(int,input().split()))

for x,y in A,B:
    print(f"{x+y}")
