f = open("yesterday.txt", "r")
yesterday_iyric = ""

while True:
    line = f.readline()
    if not line:
        break
    yesterday_iyric = yesterday_iyric + line.strip() + "\n"
f.close()

print(yesterday_iyric)

# 대소문자 구분 제거
upper_yesterday = yesterday_iyric.upper().count("YESTERDAY")

print('Number of a Word "Yesterday" : ', upper_yesterday)

# "Yesterday" vs "yesterday"
num_of_upper = yesterday_iyric.count("Yesterday")
num_of_lower = yesterday_iyric.count("yesterday")

print('Number of a Word "*Y*esterday" : ', num_of_upper)
print('Number of a Word "*y*esterday" : ', num_of_lower)
