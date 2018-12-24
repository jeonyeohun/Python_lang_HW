# 21500630 전여훈
# 20181030

# 사용자가 입력한 숫자만큼의 피보나치 수열을 출력하는 프로그램

def fibo (num):
    nownum = 1
    pnum = 1
    newlist=[];
    if num == 0:
        print("Wrong input. You should put number greater than 0")
    else:
        for i in range(1, num+1):    
            if i == 1 or i ==2:
                newlist.append(str(pnum))
            else:
                temp = nownum
                nownum = nownum+pnum
                pnum = temp
                newlist.append(str(nownum))
    newstr='\t'.join(newlist)
    print(newstr)
                     

