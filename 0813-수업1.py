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

##newList = []
##myList = [1,2,[3,4],5,[6,7],[8,9]]
##for L in myList:
##    if type(L) == list:
##        for num in L:
##            newList.append(num)
##    else:
##        newList.append(L)
##print(newList)
##

##def print_3_times():
##    print("안녕하세요")
##    print("안녕하세요")
##    print("안녕하세요")
##
##print_3_times()

##def print_n_times(value,n):
##    for i in range(n):
##        print(value)
##
##print_n_times("안녕하세요",5)

##def print_n_times(value,n):
##    for i in range(n):
##        print(value)
##
##print_n_times("안녕하세요")

##def print_n_times(value,n):
##    for i in range(n):
##        print(value)
##
##print_n_times("안녕하세요",10,20)

##def print_n_times(n,*values):
##    for i in range(n):
##        for value in values:
##            print(value)
##        print()
##print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")

##def print_n_times(value,n=2):
##    for i in range(n):
##        print(value)
##print_n_times("안녕하세요")

##def print_n_times(n=2,*values):
##    for i in range(n):
##        for value in values:
##            print(value)
##        print()
##
##print_n_times("안녕하세요","즐거운","파이썬 프로그래밍")

##def print_n_times(*values,n=2):
##    for i in range(n):
##        for value in values:
##            print(value)
##        print()
##print_n_times("안녕하세요","즐거운","파이썬 프로그래밍",3)

##def print_n_times(*values,n=2):
##    for i in range(n):
##        for value in values:
##            print(value)
##        print()
##print_n_times("안녕하세요","즐거운","파이썬 프로그래밍",n=3)

##def test(a,b=10,c=100):
##    print(a+b+c)
##test(10,20,30)
##test(a=10,b=100,c=200)
##test(c=10,a=100,b=200)
##test(10,c=200)

##value = input("> ")
##
##print(value)

##def return_test():
##    print("A 위치입니다.")
##    return
##    print("B 위치입니다.")
##
##return_test()
##
##def return_test():
##    return 100
##
##value = return_test()
##print(value)

##def return_test():
##    return
##
##value = return_test()
##print(value)

##def sum_all(start,end):
##    output = 0
##    for i in range(start,end+1):
##        output+=i
##    return output
##
##print("0 to 100:",sum_all(0,100))
##print("0 to 1000:",sum_all(0,1000))
##print("50 to 100:",sum_all(50,100))
##print("500 to 1000:",sum_all(500,1000))
##
##def sum_all(start=0,end=100,step=1):
##    output = 0
##    for i in range(start,end+1,step):
##        output+=i
##    return output
##
##print("A.",sum_all(0,100,10))
##print("B.",sum_all(end=100))
##print("C.", sum_all(end=100,step=2))

##def f(x):
##    return 2*x+1
##print(f(10))
##
##def f(x):
##    return x**2+2*x+1
##print(f(10))

##def mul(*values):
##    output = 1
##    for value in values:
##        output*=value
##    return output
##print(mul(5,7,9,10))

##def factorial(n):
##    output = 1
##    for i in range(1,n+1):
##        output*=i
##    return output
##print("1!:",factorial(1))
##print("2!:",factorial(2))
##print("3!:",factorial(3))
##print("4!:",factorial(4))
##print("5!:",factorial(5))

##def factorial(n):
##    if n==0:
##        return 1
##    else:
##        return n * factorial(n-1)
##
##print("1!:",factorial(1))
##print("2!:",factorial(2))
##print("3!:",factorial(3))
##print("4!;",factorial(4))
##print("5!:",factorial(5))

##def fibonacci(n):
##    if n==1:
##        return 1
##    if n==2:
##        return 1
##    else:
##        return fibonacci(n-1)+fibonacci(n-2)
##
##print("fibonacci(1):",fibonacci(1))
##print("fibonacci(2):",fibonacci(2))
##print("fibonacci(3):",fibonacci(3))
##print("fibonacci(4):",fibonacci(4))
##print("fibonacci(5):",fibonacci(5))

##counter = 0
##def fibonacci(n):
##    print("fibonacci({})를 구합니다.".format(n))
##    global counter
##    counter+=1
##
##    if n==1:
##        return 1
##    if n==2:
##        return 2
##    else:
##        return fibonacci(n-1)+fibonacci(n-2)
##fibonacci(10)
##print("---")
##print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))

##counter = 0
##
##def fibonacci(n):
##    counter+=1
##
##    if n==1:
##        return 1
##    if n==2:
##        return 2
##    else:
##        return fibonacci(n-1)+fibonacci(n-2)
##
##print(fibonacci(10))

##dictionary = {
##    1:1,
##    2:1
##}
##
##def fibonacci(n):
##    if n in dictionary:
##        return dictionary[n]
##    else:
##        output = fibonacci(n-1)+fibonacci(n-2)
##        dictionary[n] = output
##        return output
##
##print("fibonacci(10):",fibonacci(10))
##print("fibonacci(20):",fibonacci(20))
##print("fibonacci(30):",fibonacci(30))
##print("fibonacci(40):",fibonacci(40))
##print("fibonacci(50):",fibonacci(50))






    



