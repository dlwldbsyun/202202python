print("구구단 몇 단을 계산할까요?(1~9)")

    
while True:
    dan = int(input())

    if 1 <= dan and dan <= 9:
        print(f"구구단 {dan}을 계산합니다.")
        for i in range(1, 10):
            print(f"{dan} X {i} = {dan*i}")

    elif dan == 0:
        print("구구단 게임을 종료합니다.")
        break

    else:
        print("잘못 입력하셨습니다.")