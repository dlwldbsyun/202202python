# 2884

hour, min= map(int, input().split())

if min >= 45:
    min = min-45
    print(f"{hour} {min}")
elif hour>=1 and min < 45:
    print(f"{hour-1} {min+15}")
else:
    print("{} {}".format(23,min+15))