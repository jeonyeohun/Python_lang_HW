#21500630 전여훈

#반복문을 통해 1부터 1000 사이의 모든 홀수를 더하는 코드

sum =0
for i in range (1, 1000, 2):
    sum = sum+i
print("The sum of all odd numbers between 1 and 1000 is: ",sum)

#반복문을 통해 10부터 25까지 모든 수를 더하고 출력하는 코드

sum=0
for i in range (10, 26):
    sum = sum+i
    print(sum)


#반복문을 통해 3의 n거듭제곱을 n=20일 때 까지 모두 출력하는 코드


for i in range (0,21):
    print(3**i)


# 두 정수를 입력 받아서 두 수 사이의 있는 모든 짝수의 평균을 구하는 코드


a = int(input("Input first integer: "))
b = int(input("Input second integer: "))
sum = 0
cnt = 0

if a>b:
    for i in range (b, a+1):
        if i%2 == 0:
            sum = sum+i
            cnt = cnt+1
else:
    for i in range (a, b+1):
        if i%2 == 0:
            sum = sum+i
            cnt = cnt+1

if cnt == 0:            
    print("There is no even number between the given numbers")
else:
    avg = float(sum/cnt)
    print("The average of all even numbers between a and b is: ", avg)
            

        
#입력받은 수에서 홀수 숫자만을 뽑아내어 모두 더하는 코드


num = input("input integer: ")
sum=0
for i in range(len(num)):
    if int(num[i])%2 != 0:
        sum=sum+int(num[i])
print("The sum of all odd digits of an input is: ", sum)

