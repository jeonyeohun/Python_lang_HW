#21500630 전여훈
#20181204
'''
정렬된 두개의 숫자리스트를 받아 둘을 조합하여 새로운 리스트를 만드는 함수
    조건1: 두 리스트에 같은 값이 있는 경우, 리턴되는 리스트에는 한 번만 추가한다.
    조건2: 두 리스트 중 하나에 중복되는 값은 그대로 중복을 허용한다.
'''
    

def mergeSort(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                list2.remove(j)
    list1.extend(list2)
    list1.sort()
    print(list1)
