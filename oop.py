##### Object in Python #####

# class SoccerPlayer(object):
#     def __init__(self, name, position, back_number):
#         self.name = name
#         self.position = position
#         self.back_number = back_number

#     def change_back_number(self, new_number):
#         print("선수의 등번호를 변경합니다 : From %d to %d" % \
#             (self.back_number, new_number))
#         self.back_number = new_number

#     def __str__(self):
#         return "Hello, My name is %s. My back number is %d" % \
#             (self.name, self.back_number)

# choi = SoccerPlayer("ga eun", "mf", 10)
# print(choi)

# choi.change_back_number(7)
# print(choi)

# notebook
# note를 정리하는 프로그램
# 사용자는 note에 뭔가를 적을 수 있음
# Note에는 Content가 있고 내용을 제거할 수 있음
# 두개의 노트북을 합쳐 하나로 만들 수 있음
# 노트는 노트북에 삽입
# 노트북은 노트가 삽입 될 때 페이지를 생성, 최고 300페이지까지 저장 가능
# 300페이지 넘기면 더이상 노트 삽입 불가능

# class Note(object):
#     def __init__(self,content = None):
#         self.content = content

#     def write_content(self, content):
#         self.content = content
    
#     def remove_all(self, content):
#         self.content = ""
    
#     def __add__(self, other): # 연산자 메소드
#         return self.content + other.content

#     def __str__(self):
#         return "노트에 적힌 내용입니다: "+ self.content # print

# class NoteBook(object):
#     def __init__(self,title):
#         self.title = title
#         self.page_number = 1
#         self.notes = {}

#     def add_note(self, note, page=0):
#         if self.page_number < 300:
#             if page == 0:
#                 self.notes[self.page_number] = note
#                 self.page_number += 1
#             else:
#                 self.notes = {page : note}
#                 self.page_number += 1
#         else:
#             print("Page가 모두 채워졌습니다.")

#     def remove_note(self, page_number):
#         if page_number in self.notes.keys():
#             return self.notes.pop(page_number)
#         else:
#             print("해당 페이지는 존재하지 않습니다.")

#     def get_number_of_pages(self):
#         print(self.notes.keys())
#         return len(self.notes.keys())

# my_notebook = NoteBook("강의노트")

# new_note = Note("클래스..")
# print(new_note)
# new_note_2 = Note("파이썬 강의")
# print(new_note_2)

# my_notebook.add_note(new_note)
# my_notebook.add_note(new_note_2, 100)
# print(my_notebook.notes[100])
# print(my_notebook.get_number_of_pages())

# 상속


# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def about_me(self):
#         print("저의 이름은 ", self.name, "이구요, 제 나이는 ", str(self.age), "살 입니다.")
    
#     def __str__(self):
#         return "저의 이름은 ", self.name, "이구요, 제 나이는 ", str(self.age), "살 입니다."

# class Employee(Person):
#     def __init__(self, name, age, gender,salary,hire_date):
#         super().__init__(name, age, gender) # 부모객체 사용
#         self.salary = salary
#         self.hire_date = hire_date

#     def do_work(self):
#         print("열심히 일을 합니다.")

#     def about_me(self):
#         super().about_me() # 부모 클래스 함수 사용한다는 의미
#         print("제 급여는 ",self.salary,"원 이구요, 제 입사일은 ", self.hire_date, "입니다.")

# my_person = Person("James", 30, "man")
# my_person.about_me()
# my_employee = Employee("Jane", 29, "woman", 50000, "2010/03/24")
# my_employee.about_me()

# 다형성


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         raise NotImplementedError("Subclass must implement abstract method")

# class Cat(Animal):
#     def talk(self):
#         return 'Meow!'

# class Dog(Animal):
#     def talk(self):
#         return 'Woof!'

# animals = [Cat('Missy'),Cat('Mr.Mistoffelees'),Dog('Lassie')]

# for animal in animals:
#     print(animal.name + ': '+ animal.talk())

# 캡슐화
# 정보은닉 
# 클래스를 설계할 때, 클래스 간 간섭/정보공유의 최소화
# private변수, 데코레이터


# class Product(object):
#     pass

# class Inventory(object):
#     def __init__(self):
#         self.__items = [] # private변수
    
#     @property # 데코레이터
#     def items(self):
#         return self.__items

#     def add_new_item(self,product):
#         if type(product) == Product:
#             self.__items.append(product)
#             print("new item added")
#         else:
#             raise ValueError("Invalid item")

#     def get_number_of_items(self):
#         return len(self.__items)


# my_inventory = Inventory()
# my_inventory.add_new_item(Product())
# my_inventory.add_new_item(Product())

# 데코레이터

from ast import arg


def square(x):
    return x * x

def cube(x):
    return x*x*x

def formula(method, argument_list):
    return [method(value) for value in argument_list]

a = [1,2,3]
s = square

print(formula(s,a))

# inner func

def print_msg(msg):
    def printer():
        print(msg)
    printer()

print_msg("Bye")

# closure ex1

def print_msg1(msg):
    def printer():
        print(msg)
    return printer

another = print_msg1("Bye")
another()

# closure ex2

def tag_func(tag, text):
    text = text
    tag = tag

    def inner_func():
        return '<{0}>{1}<{0}>'.format(tag,text)
    
    return inner_func

func = tag_func('title', "This is Python Class")
func2 = tag_func('title2', "This2 is2 Python2 Class2")
print(func())
print(func2())

# decorator

def star(func):
    def inner(*args, **kwargs):
        print(args[1] * 30)
        func(*args, **kwargs)
        print(args[1] * 30)
    return inner

@star
def printer(msg, mark):
    print(msg)
printer("Hello", "T")