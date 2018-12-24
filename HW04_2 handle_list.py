
# coding: utf-8

# In[65]:


### 21500630 전여훈
#2018/10/13

#10개의 정수를 입력받아 리스트를 만들고
"""
1. 모든 element를 오른쪽으로 한칸씩 이동 후 출력
2. 10개 중 중간에 위치한 2개의 element를 제거 후 출력
3. element 중 두번째로 큰 수를 찾아서 출력
4. element 중 중복되는 값이 있으면 "exist duplicate elements"를 출력.그리고 중복되는 값과 그 값의 인덱스도 출력
"""

#10개의 element가 들어가는 리스트를 선언 및 각 element의 값을 입력 받는다
numList = [0]*10
for i in range (10):
    numList[i] = int(input("정수 입력:"))
print("Original list:", numList)
print()
    
#새로운 메모리에 리스트를 복사하여 할당한다
from copy import* 
CopyList = deepcopy(numList)

#리스트의 인데스 값들을 한칸씩 옆으로 이동, 가장 끝 인덱스값은 다른 공간에 저장했다가 가장 마지막에 0번째 인덱스에 복사 
for i in range (9, 0, -1):
    if(i+1 == len(CopyList)):
        temp = CopyList[9]
    CopyList[i] = CopyList[i-1]
CopyList[0] = temp

print("After moving elements:", CopyList)
print()


#리스트의 길이의 반에 해당하는 인덱스의 값을 삭제
for i in range(2):
    CopyList.remove(CopyList[int(len(CopyList)/2)]) 

print("After removing elements:", CopyList)
print()

#리스트의 모든 값을 비교하여 두번째로 큰 값을 SecBN 변수에 저장 후 출력
biggestN=SecBN=0
SecCnt = False
for i in range (len(CopyList)):
    if biggestN <= CopyList[i]:
        biggestN = CopyList[i]
    elif SecBN <= CopyList[i]:
        SecBN = CopyList[i]
        SecCnt = True
if SecCnt == False:   #SecBN 변수가 한번도 CopyList의 element와 비교되지 않았다면 모든 element의 값이 동일하다는 뜻.
    SecBN=biggestN
    
print("The seceond biggist number is:", SecBN)
print()

#인덱스 중에 중복되는 값이 있는 인덱스가 있다면 그 값을 출력하고 인덱스 번호도 출력
flag = False
cnt = 0
DupList = [0]*10
for i in range (len(CopyList)):
    for j in range (len(CopyList)):
        if CopyList[i] == DupList[j]: #중복값을 저장하는 리스트를 만들고 비교하여 한번 검사한 중복값은 다시 검사하지 않도록 함
            break
        elif CopyList[i] == CopyList[j] and i!=j:
            print("Exist duplicate element")
            print("The duplicate element:", CopyList[j])
            print("The original element's index number:", i)
            print("The duplicate element's index number: ", j)
            print()
            DupList[cnt]=CopyList[i]
            cnt =cnt+1
            flag = True
if flag == False:
    print("There is no duplicate element")

    


# In[ ]:


10

