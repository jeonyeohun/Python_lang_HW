
# coding: utf-8

# In[14]:


# 문자열을 입력받아 사용자가 원하는 글자(들)만 대문자로 만드는 프로그램
sentence = input("Input a sentence: ")
search = input("Input a word for search: ")
count = 0 
index = -5

if sentence.islower()==False:   # 입력받은 문자열이 모두 소문자로 구성되어있는지 확인 
    sentence = sentence.lower()  # 대문자가 섞여있다면 대문자도 소문자로 변환
    
while index != -1:
    index = sentence.find(search, index)    #바꿀 글자의 첫 글자의 인덱스 위치를 반환
    if index >= 0:
        beforeStr = sentence[0:index]   #바꿀 글자를 발견 하면 그 글자의 앞까지의 문자들을 새로운 문자열로 저장
        changeStr = sentence[index:index+len(search)].upper()  #바꿀 글자의 길이를 받아와 바꿀글자의 첫 인덱스부터 길이만큼 대문자로 변환 후 새로운 문자열로 저장
        afterStr = sentence[index+len(search):]   #바꿀 글자 이후부터 입력받은 문자열의 끝까지 새로운 문자열로 저장 
        sentence = beforeStr+changeStr+afterStr  #따로 저장한 세 문자열을 하나로 합쳐서 기존 문자열 변수에 저장
        count = count + 1  #글자를 변환한 횟수를 저장
        index = index+1  #찾을 글자의 다음글자부터 다시 찾기위해 인덱스값을 1증가시킴
        

print('A word', "'"+search+"'", 'appears', count, 'times in the sentence')
if count > 0:  # 사용자가 찾고자 하는 글자가 있었다면 
    print(sentence) #변환된 문장을 출력
else: #없다면
    print("There is no such word in the sentence") #문자가 없다는 내용을 출력

