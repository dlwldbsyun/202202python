# 섭씨 -> 화씨
print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
print("변환하고 싶은 섭씨온도를 입력해주세요: ")
ctemp = float(input())
ftemp = ((9/5)*ctemp)+32

print(f'섭씨온도 : {ctemp:.2f}')
print(f'화씨온도 : {ftemp:.2f}')

# print("섭씨온도: {}".format(ctemp))
# ftemp = ((9/5) * ctemp) + 32
# print("화씨온도: {}".format(ftemp))