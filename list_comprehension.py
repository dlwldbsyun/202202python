# pythonic code

# 2
word_1 = "Hello"
word_2 = "World"
result = [i+j for i in word_1 for j in word_2]
print(result)
# ['HW', 'Ho', 'Hr', 'Hl', 'Hd', 'eW', 'eo', 'er', 'el', 'ed', 'lW', 'lo',
#  'lr', 'll', 'ld', 'lW', 'lo', 'lr', 'll', 'ld', 'oW', 'oo', 'or', 'ol',
#  'od']

# 3 :: filter
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]

# sol1
# result2 = [i+j for i in case_1 for j in case_2 if not (i==j)] 
# print(result2)
# ['AD', 'AE', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA'] AA없음

# sol2
result2 = [i+j if not (i==j) else i for i in case_1 for j in case_2]
print(result2)
# ['A', 'AD', 'AE', 'BA', 'BD', 'BE', 'CA', 'CD', 'CE']

result2.sort()
print(result2)
# ['AD', 'AE', 'BA', 'BD', 'BE', 'CA', 'CD', 'CE']

# 4
from cgi import print_environ
import pprint
from traceback import print_tb

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    pprint.pprint(i)
# ['BROWN', 'brown', 5]
# ['FOX', 'fox', 3]
# ['JUMPS', 'jumps', 5]
# ['OVER', 'over', 4]
# ['THE', 'the', 3]
# ['LAZY', 'lazy', 4]
# ['DOG', 'dog', 3]

# two dimensional vs one dimensional
list_1 = ["A", "B", "C"]
list_2 = ["D", "E", "A"]
result3 = [[i+j for i in list_1] for j in list_2]
print(result3)
# [['AD', 'BD', 'CD'], ['AE', 'BE', 'CE'], ['AA', 'BA', 'CA']] two dimensional
# j 먼저 실행되고 그 다음에 []가 실행

# enumerate
alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]

for i, values in enumerate(zip(alist, blist)):
    print(i, values)
# list(zip(alist,blist)) # [('a1','b1'), ('a2', 'b2'), ('a3', 'b3')]
# list(enumerate(zip(alist, blist))) # [(0,('a1','b1')), (1,('a2', 'b2')), (2, ('a3', 'b3'))]

# lambda
print((lambda x,y : x+y)(10,5))

# reduce func
from functools import reduce

print(reduce(lambda x,y : x+y, [1, 2, 3, 4, 5])) # 15

##### iterable object #####

cities = ["Seoul", "Busan", "Jeju"]

memory_address_cities = iter(cities)
print(memory_address_cities)
print(next(memory_address_cities))
print(next(memory_address_cities))
print(next(memory_address_cities))

# generator comprehension

import sys

def generator_list(value):
    result = []
    for i in range(value):
        yield i

result = generator_list(50)
sys.getsizeof(result) # 데이터 절약

gen_ex = (n*n for n in range(500))
print(type(gen_ex))


##### passing arguments #####

# keyword arguments
def print_something(my_name, your_name, third_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something(third_name="abc", my_name="ji yun", your_name="ga eun")

# default arguments
def print_something_2(my_name, your_name="Team"):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something_2("Sungchul") # my_name = Sungchul
print_something_2("Sungchul" ,"Naver") 

##### variable length asterisk #####

# variable length
def asterisk_test(a,b ,*args):
    return a+b+sum(args)

print(asterisk_test(1,2,3,4,5)) # a=1, b=2, args=(3,4,5)

# keyword variable length
def kwargs_test_1(**kwargs):
    print(kwargs)
    print(type(kwargs))

kwargs_test_1(first=3, second=4, third=5)

def kwargs_test_3(one,two,*args, **kwargs):
    print(one+two+sum(args))
    print(kwargs)

kwargs_test_3(3,4,5,6,7,8,9, first=3, second=4, third=5)

def kwargs_test_2(one,two,*args, **kwargs):
    print(one+two+sum(args))
    print(kwargs)

kwargs_test_2(one=10, two=40, first=3, second=4, third=5)
kwargs_test_2(10, 20, first=3, second=4, third=5)

# asterisk-unpacking a container
def asterisk_test(a, *args):
    print(a, *args)
    print(a, args)
    print(type(args))

test = (2,3,4,5,6)
asterisk_test(1, *test)