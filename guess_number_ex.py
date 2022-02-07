from cmath import pi
import random


true_value = random.randint(1, 100)
print("숫자를 맞춰보세요(1~100)")
print("")
input_value = 1

while true_value != input_value:
    input_value = int(input())
    # 사용자의 입력값이 true_value보다 클 때, 작을 때

    if input_value > true_value:
        print("숫자가 너무 큽니다.")
    else:
        print("숫자가 너무 작습니다.")

print(f"정답입니다. 입력한 숫자는 {true_value} 입니다.")
