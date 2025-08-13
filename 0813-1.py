dict = {}
for i in range(0,100):
    dict[i+1] = []
    for i2 in range(0,100):
        dict[i+1].append(0)
case = int(input())
for cases in range(0,case):
    y,h = input().split(" ")
    for n1 in range(int(h),int(h)+11):
        for n2 in range(int(y)-1, int(y)+10):
            dict[n1][n2] = 1
n=0
for num1 in range(1,101):
        for num2 in range(0,100):
            if dict[num1][num2] == 1:
                n+=1
print(n)
        
        
