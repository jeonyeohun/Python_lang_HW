
# coding: utf-8

# In[1]:

# 21500630 전여훈

score = float(input("input your score: "))      # 점수를 저장할 변수를 score를 float 형 데이터로 입력받음
types = input("input Letter(L) or PF(PF): ")    # 그레이드인지 PF인지 입력받는 변수

if score >= 90:         # score 변수에 저장된 값이 90 이상이라면
    letter = 'A'        # letter 변수에 그레이드 저장
    PF = 'PD'           # PF 변수에 PF 저장
elif score >= 80:       
    letter = 'B'
    PF = 'Pass'
elif score >= 70:
    letter = 'D'
    PF = 'Pass'
else:
    letter = 'F'
    PF = 'F'
    
if types == 'L':                    #사용자가 L 문자를 types변수에 입력했다면 
    print("Your grade is", letter)  #letter 변수에 저장된 문자 출력
elif types == 'PF':                 #사용자가 PF 문자를 types 변수에 입력했다면
    print("Your grade is", PF)      #PF 변수에 저장된 문자 출력
else:
    print("invalid grade type")     #이외의 입력은 모두 오류 메세지 출력

