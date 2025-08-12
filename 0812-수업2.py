dict = {}
for i in range(0,100):
    dict[i] = 0
    for i2 in range(0,100):
        Dict[i][i2] = 0
case = int(input())
for cases in range(0,case):
    y,h = input().split(" ")
    for n1 in range(int(h),int(h)+10):
        dict[n1]=1
        for n2 in range(int(y), int(y)+10):
            Dict[n1][n2] = 1
n=0
for num in range(0,100):
    if dict[num1]==1:
    for num2 in range(0,100):
        if Dict[num2] == 1:
            n+=1
print(n)
