"""remainder = 1357 // 10
number1 = 1357 % 10
remainder1 = remainder // 10
number10 = remainder % 10
number1000 = remainder1 // 10
number100 = remainder1 % 10
print(number1)
print(number10)
print(number100)
print(number1000)

number = str(input("숫자 5개를 입력해주세요: "))
number1, number2, number3, number4, number5 = number.split(" ")
average = (int(number1)+int(number2)+int(number3)+int(number4)+int(number5))/5
print(f"{average:.3f}")

txt = input("문자열을 입력해주세요: ")
txt1,txt2 = txt.split(" ")
txt3 = txt1[0].upper()+txt1[1:]
txt4 = txt2[0].upper()+txt2[1:]
txt5=txt3+" "
txt5+=txt4
print(txt5)

a = 10
b = 20
a==b
a!=5.6
"30000" == "30000"
"B"!="P"

a = 10
b = 20
a < b < 40
13.2 <= b
"30000" >= "30001"
"B" >= "P"

num1 = float(input("첫 번째 숫자 입력: "))
num2 = float(input("두 번째 숫자 입력: "))
print(f"num1 >= num2 = {num1 >= num2}")
print(f"num1 <= num2 = {num1 <= num2}")
print(f"num1 == num2 = {num1 == num2}")
print(f"num1 != num2 = {num1 != num2}")

num1 = float(input("첫 번째 숫자 입력: "))
num2 = float(input("두 번째 숫자 입력: "))
num3 = float(input("세 번째 숫자 입력: "))

ascending = num1 < num2 < num3
descending = num1 > num2 > num3

print(type(ascending), type(descending))
print(f"num1<num2<num3 = {ascending}")
print(f"num1>num2>num3 = {descending}")

num = int(input("숫자를 입력해주세요: "))
print(num <=100)"""

num = int(input("숫자를 입력해주세요: "))
between = 30 <num <60
print(f"{between}")
