"""number = input("정수 입력> ")
number = int(number)
if number % 2 == 0:
    print("짝수입니다")
if number % 2 == 1:
    print("홀수입니다")"""

"""number = input("정수 입력>")
number = int(number)
if number % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")"""

"""import datetime
now = datetime.datetime.now()
month = now.month
if 3 <= month <= 5:
    print("현재는 봄입니다")
elif 6 <= month <= 8:
    print("현재는 여름입니다")
elif 9 <= month <= 11:
    print("현재는 가을입니다")
else:
    print("현재는 겨울입니다")"""

"""score = float(input("학점 입력> "))
if score == 4.5:
    print("신")
elif 4.2 <= score < 4.5:
    print("교수님의 사랑")
elif 3.5 <= score < 4.2:
    print("현 체재의 수호자")
elif 2.8 <= score < 3.5:
    print("일반인")
elif 2.3 <= score < 2.8:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score < 2.3:
    print("오락문화의 선구자")
elif 1.0 <= score < 1.75:
    print("불가촉천민")
elif 0.5 <= score < 1.0:
    print("자벌레")
elif score == 0:
    print("시대를 앞서가는 혁명의 씨앗")"""

"""score = float(input("학점 입력> "))
if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체재의 수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
    print("오락문화의 선구자")
elif 1.0 <= score:
    print("불가촉천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 < score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")"""

"""print("# if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환합니다")
else:
    print("0은 False로 변환됩니다")
    print()"""
"""print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다")
else:
    print("빈 문자열은 False 로 변환됩니다")"""

"""number = input("정수 입력> ")
number = int(number)

if number > 0:
    
    pass
else:

    pass"""

"""number = input("정수 입력> ")
number = int(number)

if number > 0:

    raise NotImplementedError
else:

    raise NotImplementedError """
"""import datetime
now = datetime.datetime.now()
hour = now.hour
text = str(input("입력> "))
if "안녕" in text:
    print("안녕하세요.")
elif "몇 시" and "?" in text:
    print("지금은 "+str(hour)+"시 입니다.")
else:
    print(text)"""

number = str(input("정수를 입력해주세요: "))
number2 = int(number)
if number2 % 2 == 0:
    print(number+"은 2로 나누어 떨어지는 숫자입니다.")
else:
    print(number+"은 2로 나누어 떨어지는 숫자가 아닙니다.")
if number2 % 3 == 0:
    print(number+"은 3로 나누어 떨어지는 숫자입니다.")
else:
    print(number+"은 3으로 나누어 떨어지는 숫자가 아닙니다.")
if number2 % 4 == 0:
    print(number+"은 4로 나누어 떨어지는 숫자입니다.")
else:
    print(number+"은 4로 나누어 떨어지는 숫자가 아닙니다.")
if number2 % 5 == 0:
    print(number+"은 5로 나누어 떨어지는 숫자입니다.")
else:
    print(number+"은 5로 나누어 떨어지는 숫자가 아닙니다.")
    
