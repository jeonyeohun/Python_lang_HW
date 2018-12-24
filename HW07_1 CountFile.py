# 21500630 전여훈
# 20181130
# 파일을 읽어 파일내의 단어 수, 글자 수, 공백제외 글자 수, 줄 수를 계산하여 출력하는 함수

import sys

def ReadText(): 
    txtcnt = 0
    spcnt = 0
    line = 0
    wcnt = 0

    try:
        inf = open("data.txt", 'r')
        s = inf.readlines()
        for i in range(len(s)):
            s[i].strip('\0')
            tempList = s[i].split()
            wcnt = wcnt+len(tempList)
            
            line = line+1
            txtcnt = txtcnt+len(s[i])
            for j in range(len(s[i])):
                if s[i][j] == ' ':
                    spcnt = spcnt+1

        print("The number of words:", spcnt)
        print("The number of characters:", txtcnt)
        print("The number of char without space:", txtcnt-spcnt)
        print("The number of lines:", line)
        
    except IOError as err:
        print("I/O error: {0}".format(err))
