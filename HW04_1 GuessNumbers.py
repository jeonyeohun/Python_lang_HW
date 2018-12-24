
# coding: utf-8

# In[ ]:


#21500630 전여훈
#2018/10/13
"""
1. 1~9의 숫자로 구성된 4개의 아이템 리스트를 생성 <random.sample(range(1, 10), 4)>
2. 사용자에게 4개의 정수를 입력받아 리스트를 구성, 사용자가 입력한 4개의 값이 중복되는경우 다시 입력을 받는다 
<check_list(listname,input_num)> 생성.
3. 컴퓨터가 만든 리스트의 아이템과 사용자가 입력한 리스트 아이템의 위치가 같으면 strike, 다르지만 같은 값이면 ball로 판정하여 화면에 출력
4. 사용자가 입력한 값을 받을 때마다 횟수를 세고 컴퓨터가 만든 리스트값을 맞출 때까지 반복.
"""
# 랜덤한 4개의 숫자가 들어있는 리스트 생성
import random
ComList = random.sample(range(1, 10), 4)

# 중복된 정수가 사용자가 입력한 리스트 안에 들어가 있는지 확인하는 함수
def check_list (UserList, n):
    cnt=0
    for i in range (len(UserList)):
        if UserList[i] == n:
            cnt+=1
    if cnt >1:
        return False
    else:
        return True

strcnt = 0
gcnt=0

#사용자가 입력한 4개의 숫자의 위치와 값이 컴퓨터의 리스트와 일치할 경우 반복문 종료
while(strcnt!=4):
#반복이 새로 시작될때마다 총 시도횟수를 담는 gcnt변수를 제외한 리스트와 카운트 변수를 모두 초기화
    gcnt +=1
    i=0
    UserList = [0,0,0,0]
    strcnt = 0
    ballcnt = 0
    
#사용자에게 리스트 길이만큼의 정수를 입력받고 하나의 정수가 입력될 때마다 중복숫자확인 함수를 호출하여 검사
    while(i<len(UserList)):
        UserList[i]= int(input("put integer: "))
        n = UserList[i]
        
#중복숫자확인 함수가 중복된 숫자가 있다고 반환할 경우 i번째 입력을 다시 반복함
        if check_list(UserList, n)==False:
            print("repeated number, input different number")
            i=i-1
        i=i+1
        
#사용자의 리스트와 컴퓨터의 리스트를 비교해서 
#같은 값이 인덱스 위치에 존재하면 ballcnt 변수를 증가, 같은 인덱스 자리에 같은 값이 존재하면 strcnt 변수 증가
    for i in range (len(UserList)):
        for j in range (len(ComList)):
            if UserList[i] == ComList[j] and i==j:
                strcnt += 1
            elif UserList[i] == ComList[j]:
                ballcnt += 1
    print(str(strcnt)+"-Strike!", str(ballcnt)+"-Ball!")
    print()

print("You win! on", gcnt, "try")
            


