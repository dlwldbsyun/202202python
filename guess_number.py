# 숫자찾기
# 1~100 임의의 숫자를 맞추시오
import random

print("숫자를 맞춰보세요")
answer = random.randrange(1, 100)
value = ""

while answer != value:
    value = int(input("1~100사이에서 입력: "))
    if value > answer:
        print("숫자가 너무 큽니다")
        continue
    elif value < answer:
        print("숫자가 너무 작습니다")
        continue

print(f"정답입니다. 입력한 숫자는 {answer} 입니다.")