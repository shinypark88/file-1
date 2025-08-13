##dict = {}
##for i in range(1,100+1):
##    dict[i] = []
##    for i2 in range(0,100+1):
##        dict[i].insert(i2,0)
##case = int(input())
##for cases in range(0,case):
##    h,y = input().split(" ")
##    for n1 in range(int(h)+1,int(h)+10+1):
##        for n2 in range(int(y)+1, int(y)+10+1):
##            dict[n1][n2] = 1
##n=0
##for num1 in range(1,100+1):
##        for num2 in range(1,100+1):
##            if dict[num1][num2] == 1:
##                n+=1
##print(n)



##output = []
##for i in range(1,100+1):
##    Two = "{:b}".format(i)
##    L = len(Two)
##    count = 0
##    for i2 in range(0,L):
##        if Two[i2] == "0":
##            count+=1
##    if count==1:
##        output.append(i)
##for i in output:
##    print("{} : {}".format(i, "{:b}".format(i)))
##print("합계:", sum(output))
##

##dict = {}
##myList = [1,2,3,4,1,2,3,1,4,1,2,3]
##for num in myList:
##    if num not in dict:
##        dict[num] = 1
##    elif num in dict:
##        dict[num]+=1
##print("{}에서 사용된 숫자의 종류는 {}개입니다.".format(myList, len(list(dict.keys()))))
##print("참고:", dict)
##    

##dict = {}
##code = input("염기 서열을 입력해주세요: ")
##L = len(code)
##for i in range(0,L):
##    if "{}의 개수".format(code[i]) not in dict.keys():
##        dict["{}의 개수".format(code[i])] = 1
##    else:
##        dict["{}의 개수".format(code[i])] +=1
##print(dict)


##dict = {}
##code = input("염기 서열을 입력해주세요: ")
##L = len(code)
##for i in range(0,L-2,3):
##    if "{}의 개수".format(code[i]+code[i+1]+code[i+2]) not in dict.keys():
##        dict["{}의 개수".format(code[i]+code[i+1]+code[i+2])] = 1
##    else:
##        dict["{}의 개수".format(code[i]+code[i+1]+code[i+2])] +=1
##print(dict)
##


