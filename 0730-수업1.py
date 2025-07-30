myList = []
N,M = input().split(" ")
for i in range(0,int(N)+1):
    myList.append(i)
    print(myList)
for m in range(0,int(M)):
    i,j = input().split(" ")
    print(reversed(myList[int(i):int(j)+1]))
    newList=myList[0:int(i)]+reversed(myList[int(i):int(j)+1])+myList[int(j)+1:int(N)+1]
    print(newList)
    

    
