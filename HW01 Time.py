time=input("시간을 초 단위로 입력하시오 : ")
time=int(time)
hrs=int(time/3600)
mins=int((time%3600)/60)
sec=int((time%3600)%60)
print(time, "초는", hrs, "시간", mins, "분", sec, "초 입니다.")

