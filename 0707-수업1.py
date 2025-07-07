"""num1= int(input("숫자를 입력해주세요: "))
print(num1//4)
print(num1%4)
print(num1**4)"""

"""weight = int(input("몸무게(kg)를 입력하세요: "))
height = float(input("키(m)를 입력하세요: "))
BMI = weight / height**2
print(f"BMI지수는 {BMI:.2f}")"""

"""sec = int(input("초 입력: "))
min = sec // 60
sec = sec % 60
hour = min // 60
min = min % 60
day = hour // 24
hour = hour % 24
print(f"{day}일{hour}시간{min}분{sec}초")"""

"""finance = int(input("물건의 가격을 입력합니다: "))
N_500 = (1000-finance) // 500
remainder_1 =(1000-finance) % 500
N_100 = remainder_1 // 100
remainder_2 = remainder_1 % 100
N_50 = remainder_2 // 50
remainder_3 = remainder_2 %50
N_10 = remainder_3 // 10

print(f"500원 {N_500}개\n100원 {N_100}개\n50원 {N_50}개\n10원 {N_10}개")"""

"""number = int(input("세 자리 숫자 입력: "))
number1 = number % 10
number = number // 10
number10 = number % 10
number100 = number // 10
print(f"백의 자리: {number100}")
print(f"십의 자리: {number10}")
print(f"일의 자리: {number1}")"""

"""number = int(input("다섯 자리 숫자를 입력합니다: "))
number1 = number % 10
remainder = number // 10
number10 = remainder % 10
remainder1 = remainder // 10
number100 = remainder1 % 10
remainder2 = remainder1 //10
number1000 = remainder2 % 10
number10000 = remainder2 // 10
print(f"만의 자리: {number10000}")
print(f"천의 자리: {number1000}")
print(f"백의 자리: {number100}")
print(f"십의 자리: {number10}")
print(f"일의 자리: {number1}")"""

"""num1 = int(input("첫 번째 숫자 입력: "))
num2 = int(input("두 번째 숫자 입력: "))
num3 = int(input("세 번째 숫자 입력: "))
print(f"10000 += num1 -> {10000+num1}")
print(f"10000 -= num2 -> {10000-num2}")
print(f"10000 *= num3 -> {10000*num3}")"""

"""txt = input("문자열 입력: ")
num = input("숫자 입력: ")
txt2 = txt
txt += num
txt2 *= int(num)
print(txt)
print(txt2)"""

"""num = int(input("숫자를 입력해주세요: "))
txt = "삐약"
txt*=num
print(txt)"""

"""num = input("숫자 3개를 입력해주세요: ")
num1, num2, num3 = num.split(" ")
startnum = 100
startnum-=int(num1)
startnum-=int(num2)
startnum-=int(num3)
print(startnum)"""

"""egg = int(input("계란 개수 입력: "))
tmp = egg
tmp %= 30
egg //= 30
print("계란 {0}판, 나머지{1}개".format(egg,tmp))"""

first = int(input("피자를 몇 등분할까?: "))
second = int(input("한 조각을 몇 등분할까?: "))
pizza = 100
pizza /= first
pizza /= second
print(f"이 조각은 피자 한 판의 {pizza:.2f}%")





