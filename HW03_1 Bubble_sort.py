
# coding: utf-8

# In[2]:

# 21500630 전여훈
# 2018/10/3
# 7개의 숫자를 입력 받아 작은 수부터 큰 수의 순서로 나열하는 프로그램
num1 = int(input("숫자1 입력: "))
num2 = int(input("숫자2 입력: "))
num3 = int(input("숫자3 입력: "))
num4 = int(input("숫자4 입력: "))
num5 = int(input("숫자5 입력: "))
num6 = int(input("숫자6 입력: "))
num7 = int(input("숫자7 입력: "))
    
numbers = [num1, num2, num3, num4, num5, num6, num7]
for i in range (0, len(numbers)-1):
    flag = False   #대소비교를 했는지 확인하기 위한 플래그
    for j in range (0, len(numbers)-1-i):
        if numbers[j] >= numbers[j+1]:
            flag = True
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
    if flag == False:   #대소비교를 하지 않았다면 이미 배열이 완성되어있다는 의미이므로 반복문 탈출
        break
print(i+1, "회 비교했습니다.")
print(numbers)    

