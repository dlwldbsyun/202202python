# 2주차 팀미션
# 

# 1
# 중간고사 기말고사 점수를 따로 받아 저장하는 클래스를 구현해보세요.
# 단, 생성자의 인스턴스는 private으로 선언되어야하며, 
# 데코레이터를 이용해 데이터를 저장하고, 함수를 이용해 평균값을 출력해보세요.

# from ctypes import sizeof

# class Score():
#     def Score(self, mid, final):
#         self.__mid = mid
#         self.__final = final

# score = Score(50, 75)
# print((score.mid + score.final)/2)

# 2
# 다양한 탈 것을 사용하는 게임을 만드는 중입니다.
# 빠른 구현을 위해서 이미 구현한 Car 클래스를 이용해서 
# Bike라는 클래스를 새로 제작하려고 합니다.
# Car 클래스를 상속받아서 새로운 Bike 클래스를 아래와 
# 같이 출력되도록 구성해보세요.

# class Car():
#     def __init__(self, fuel, wheels):
#         self.fuel = fuel
#         self.wheels = wheels

# class Bike():
#     def __init__(self, fuel, wheels, size):
#         self.fuel = fuel
#         self.wheels = wheels
#         self.size = size

# bike = Bike("gas", 2, "small")
# print(bike.fuel, bike.wheels, bike.size)

# 3

# 이번 시험 결과에 대한 데이터를 학과 사무실에서 CSV파일로 전달해줬습니다. 
# 우리는 이 파일을 이용해서 데이터 처리를 진행해야 합니다. 
# 파일 입출력을 이용해 파일 데이터를 리스트로 만들어보세요.
import csv
from importlib.resources import contents

file_path = "./data-01-test-score.csv"
f=open(file_path, "r")

def read_file(file_path):
    temp=csv.reader(f)
    return [ for i in file_path for j in ]

print(read_file())


# 4

# 우리는 방금 CSV 파일을 읽는 함수를 구현해보았습니다. 
# 하지만 이를 조금 더 효율적으로 사용하기 위해서 클래스로 구성을 진행하려고 합니다. 
# 방금 구현한 함수를 포함한 클래스를 구현해보세요.







# 5

# 이전에 구현한 클래스에서 merge_list의 함수 동작을 변경해야합니다. 
# 단순합계가 아닌 평균을 구하는 함수로 변경해보세요.