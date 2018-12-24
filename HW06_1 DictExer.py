#21500630 전여훈
#20181110
'''
1. 딕셔너리의 key를 모두 출력
2. 딕셔너리의 value를 모두 출력
3. key를 기준으로 딕셔너리를 내림차순 정렬하여 출력
4. value의 평균값을 출력
5. 각 key의 value 만큼 '*'문자를 key와 함께 출력. 이때, key를 기준으로 내림차순 정렬하여 출력
''' 

gradeCounts = {"A":8, "D":3, "B":15, "F":2, "C":6, "P":7, "I":1}


print("Keys:", gradeCounts.keys())
print("Values:", gradeCounts.values())
t=sorted(gradeCounts.items())
print("Sorted by Key:", t)

sum=0
for i in range (len(gradeCounts)):
    sum = sum+t[i][1]

print("The average of the Values:", sum/len(gradeCounts))

for i in range(len(gradeCounts)):
    print(t[i][0]+':'+'*' * t[i][1])
