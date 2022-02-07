# chapter 01
# 함수와 콘솔창 예제

# name = "Apple"
# price = 5600
# number = 7
# print("{2}, {1}, {0}".format(number, name, price))

# test_list = ['치킨', '피자', '삼겹살', '족발', '초밥', '소주']
# for data in test_list[::2]:
#     if len(data) == 3:
#         print(data)

# def print_greedings(t):
#     t = "Hello."
#     print("In Fn : ", t)

# x = "Hi"
# print_greedings(x)
# print("Out Fn : ", x)

# string = "#You #Only #Live #Once."
# print(string.split("#"))
# print(string.replace("#"," "))

# a, b, *c = (14, 21, 25, 39, 46, 57)
# print(c)

# data_list = [0, 1, 2, 3, 4, 5]

# def f(x):
#     return x ** 5
# for i in data_list:
#     print(f(data_list[i]))

# # 1_function and console I/O

def calsulate_rectangle_area(x, y):
    return x * y

rectangle_x = 10
rectangle_y = 20

print("사각형 x의 길이: ", rectangle_x)
print("사각형 y의 길이: ", rectangle_y)

# 넓이를 구하는 함수 호출
print("사각형의 넓이: ", calsulate_rectangle_area(rectangle_x, rectangle_y))

# f(x) = 2x + 7, g(x) = x^2이고 x = 2 일때
# f(x)+g(x)+f(g(x))+g(f(x))의 값?
# f(2)=11, g(2)=4, f(g(x))=15, g(f(x))=121
# 11 + 4+ 15 + 121 = 151

def f(x):
    return 2 * x + 7


def g(x):
    return x ** 2

x = 2
print('answer : ', f(x)+g(x)+f(g(x))+g(f(x)))
# def안에 print문이 있는 경우 화면에는 찍히지만 값이 저장되진 않음

list_ex = [5, 4, 3, 2, 1]
print(list_ex)

# 주의
# def f(x):
#     return print(x + 10)
# x = 10
# c = f(x)
# print(c)
# out : None // print 문에서 끝나면서 return 값으로 안들어감

# print("Enter your name : ")
# somebody = input()
# print("hi", somebody)

# temp = float(input("Enter your temperature : "))
# print("temperature", temp, "입니다")
# print(type(temp))

# formatting 
# 1. %string 2. 

# 홀수데이터 필요
# num_list가 홀수인 데이터만 출력하도록 하는 함수 작성

# num_list = [1, 5, 7, 15, 16, 22, 28, 29]

# def get_odd_num(num_list):
#     for i in num_list:
#         num_list[i]%2 == 1
#         return num_list[i]
        

# print(get_odd_num(num_list))

