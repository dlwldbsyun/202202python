# 1주차 팀미션
# 1번

num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
    return [ i for i in num_list if i % 2 != 0]
        
print(get_odd_num(num_list))

# 2번 : string 문장을 받아 단어를 역순으로 배열

sentence = "Why a is there will a is there Where"

def reserve_sentence(sentence):
    s1 = sentence.split()
    s2 = s1[::-1]
    answer = " ".join(s2)
    return answer

print(reserve_sentence(sentence))

# 3번 :  각 학생들의 점 수가 튜플 형태로 저장되어 있고, 이를 포함한 리스트를 
# 이용 해 각 학생들의 평균 점수를 출력하는 함수를 제작하세요.

score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_avg(score):
    avg = lambda x,y : (x+y)/2
    rtn = [avg(*score[i]) for i in range(len(score))]
    for i, v in enumerate(rtn):
        print("{0}번째, 평균 : {1}".format(i+1,v))

get_avg(score)

# 4번 : 두개의 납품처에서 각각 과일과 야채들이 납품되었습니다. 
# 이를 각각 물 품의 갯수를 나타내는 2개의 딕셔너리로 정리했습니다. 
# 물품을 정리하기 위해서 2 개의 딕셔너리 객체를 합쳐 출력하는 함수를 제작하세요.

