esc = 1

while esc != 10:
    print("구구단 몇 단을 계산할까요?(1~9)")
    dan = int(input())
    
    if dan == 10:
        print("구구단 게임을 종료합니다.")
        break

    for i in range(1, 10):
        print(f"{dan} X {i} = {dan*i}")