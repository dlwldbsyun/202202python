a, b = map(int, input().split()) # map(적용할 함수, 반복가능한 리스트)
if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")