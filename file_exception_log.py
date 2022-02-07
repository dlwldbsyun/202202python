# exception handling
# 

# for i in range(10):
#     try: 
#         print(10/i)
#     except ZeroDivisionError:
#         print("Not divided 0")


a = [1,2,3,4,5]
for i in range(10):
    try:
        print(i, 10 // i)
        print(a[i])
        print(v)
    except ZeroDivisionError:
        print("Error")
        print("Not divided by 0")
    except IndexError as e:
        print(e)
    except Exception as e:
        print(e)

# while True:
#     value = input("변환할 정수값을 입력해주세요")
#     for digit in value:
#         if digit not in "0123456789":
#             raise ValueError("숫자값을 입력하지 않으셨습니다.")
#     print("정수값으로 변환된 숫자 -", int(value))

def get_binary_number(decimal_number):
    assert isinstance(decimal_number, int) 
    # 앞의 코드가 True나 False로 나올 수 있도록하고 False면 error
    return bin(decimal_number)

print(get_binary_number(10))

# with open("i_have_a_dream.txt","r") as my_file:
#     i = 0
#     while True:
#         line = my_file.readline()
#         if not line:
#             break
#         print(str(i)+"==="+line.replace("\n","")) # 한줄씩 값 출력
#         i += 1

# with open("i_have_a_dream.txt","r") as my_file:
#     contents = my_file.read()
#     word_list = contents.split(" ") # 빈칸을 기준으로 단어를 분리해서 리스트로
#     line_list = contents.split("\n") # 한줄씩 분리하여 리스트로

# print("Total Number if Characters : ", len(contents))
# print("Total Number of Words : ", len(word_list))
# print("Total Number of Lines : ", len(line_list))

# File Write

# f = open("count_log.txt", mode='w', encoding = "utf8")
# for i in range(1,11):
#     data = "{0}번째 줄입니다.\n".format(i)
#     f.write(data)
# f.close()

# #

# with open("count_log.txt", mode="a", encoding="utf8") as f:
#     for i in range(11, 21):
#         data = "{0}번째 줄입니다.\n".format(i)
#         f.write(data)


# os

# import os
# os.mkdir("log")

# try: 
#     os.mkdir("abc")
# except FileExistsError as e:
#     print("Already created")
import os
import shutil

# source = "i_have_a_dream.txt"
# test = os.path.join("abc", "sungchul.txt")

# shutil.copy(source, test) # i_have_a_dream의 내용을 sungchul 이곳에 복사

import pathlib
from traceback import print_tb

# cwd = pathlib.Path.cwd()
# print(cwd) # 파일 위치

if not os.path.exists("log"):
    os.mkdir("log")

TARGET_FILE_PATH = os.path.join("log", "count_log.txt")
if not os.path.exists(TARGET_FILE_PATH):
    f = open("log/count_log.txt", mode="w", encoding="utf8")
    f.write("기록이 시작됩니다.\n") # 실행시킬 때마다 계속 입력되어 저장
    f.close()

# pickle :: 영속화

import pickle

# f = open("list.pickle", "wb")
# test = [1,2,3,4,5]
# pickle.dump(test, f)
# f.close()

# del test

# print(test)

# f = open("list.pickle","rb")
# test_pickle = pickle.load(f)
# print(test_pickle)
# f.close

# class Multiply(object):
#     def __init__(self, multiplier):
#         self.multipier = multiplier

#     def multiply(self, number):
#         return number * self.multipier

# v_multiply = Multiply(5)
# v_multiply.multiply(10)

# f = open("multiply_object.pickle","wb")
# pickle.dump(v_multiply,f)
# f.close()

# del v_multiply

# f = open("multiply_object.pickle","rb")
# multiply_pickle = pickle.load(f)
# print(multiply_pickle.multiply(100))

# log_handling
# 프로그램이 실행되는 동안 일어나는 정보를 기록으로 남기기

import configparser
config = configparser.ConfigParser()
config.sections()

config.read("example.cfg")
config.sections()

for key1 in config['SectionOne']:
    value1 = config['SectionOne'][key1]
    print("{0} : {1}".format(key1, value1))

config['SectionOne']["status"]

