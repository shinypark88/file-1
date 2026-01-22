import random
목록 = ["가위","바위","보"]
사람 = 목록.index(input())
컴퓨터 = random.randint(0,2)

if 사람==컴퓨터:
    print("무승부")
elif 사람-컴퓨터==1 or 사람-컴퓨터==-2:
    print("사람 승리")
else:
    print("컴퓨터 승리")
