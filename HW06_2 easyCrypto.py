#21500630 전여훈
#20181110
#특정한 단어를 입력받아 그 단어의 알파벳마다 아스키 코드가 짝수라면 아스키코드상 하나 앞의 문자로 바꾸고, 홀수라면 아스키 코드 상 다음 문자로 변경

def easyCrypto (word):
    newWord = ' '
    for i in word:
        if ord(i) % 2 == 0:
            newWord = newWord+chr(ord(i)-1)
        else:
            newWord = newWord+chr(ord(i)+1)
            
    print(newWord)
