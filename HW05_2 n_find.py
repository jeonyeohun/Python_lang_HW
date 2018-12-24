# 21500630 전여훈
# 20181030

#리스트의 요소에서 특정한 문자 또는 문자열이 포함ㅇ되어 있다면 그 멤버의 인덱스 값을 리스트로 구성하여 리턴하는 프로그램

def N_find (strlist, find):
    
    NewList = []
    flag = True;
    for st in strlist:
        index =0
        for i in range(len(st)):
            index = st.find(find)
            if index != -1:
                NewList.append(index)
                flag = False
                break;
            
        
    if flag == False:
        return NewList
    else:
        return -1
        
