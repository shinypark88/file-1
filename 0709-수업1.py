##num1 = int(input("첫 번째 숫자 입력: "))
##num2 = int(input("두 번째 숫자 입력: "))
##print(f"""num1, num2 또는 둘의 합이 10의 배수인가?
##={num1%10==0 or num2%10==0 or (num1+num2)%10==0}""")
##
##
##
##num1 = int(input("첫 번째 숫자 입력: "))
##num2 = int(input("두 번째 숫자 입력: "))
##
##print(f"둘 다 양수? = {num1 > 0 and num2 > 0}")
##print(f"하나라도 양수? = {num1 > 0 or num2 > 0}")
##
##print(f"num1은 0인가? = {not num1}")
##print(f"num2는 0인가? = {not num2}")
##
##num = int(input("숫자를 입력하세요: "))
##print(f"{not num or num == 10 or num == 100}")
##
##num = int(input("숫자를 입력해주세요: "))
##print(f"{num != 0 and (num %2 == 1 or num%8 ==0)}")
##
##num1 = 15
##if num1 == 15 :
##    print("이 숫자는 15입니다.")
##
##num1 = 15
##if num1 != 15:
##    print("이 숫자는 15가 아닙니다.")
##print("위 문장은 출력되지 않습니다.")
##
##str1 = "Python is simple"
##if "is" in str1:
##    print("이 문장에는 is가 있음.")
##level = int(input("레벨을 입력해 주세요: "))
##if level == 15:
##    print("현재 레벨은 15입니다: ")
##if level != 15:
##    print("현재 레벨은 15가 아닙니다.")
##level = int(input("레벨을 입력해 주세요: "))
##if level > 10:
##        print("현재 레벨은 10을 넘습니다.")
##if level < 20:
##        print("현재 레벨은 20보다 작습니다.")
##print("Loading...")
##level = int(input("레벨을 입력해 주세요: "))
##if level >= 10:
##    print("현재 레벨은 10을 넘습니다.")
##if level <= 20:
##    print("현재 레벨은 20보다 작습니다.")
##answer = "이샘_코딩_학원"
##word = input("단어를 입력해주세요: ")
##
##if word in answer:
##    print("해당 언어가 포함되어 있습니다.")
##if word not in answer:
##    print("해당 언어가 포함되어 있지 않습니다.")

##level = int(input("레벨을 입력해 주세요: "))
##if level < 10:
##    print("씨앗 레벨입니다.")
##if level > 10 and level <= 25:
##    print("새싹 레벨입니다.")
##if level > 25 and level <= 40:
##    print("꽃 레벨입니다.")
##if level > 40 and level <= 60:
##    print("나무 레벨입니다.")

##month = int(input("몇 월인지 입력해주세요: "))
##if month >= 3 and month <= 5:
##    season = "봄"
##if month >= 6 and month <= 8:
##    season = "여름"
##if month >=9 and month <= 11:
##    season = "가을"
##if month == 12 or month <= 2:
##    season = "겨울"
##print(f"지금 계절은 {season}입니다.")
##
##number = int(input("숫자를 입력해주세요: "))
##if number % 3 == 0 or number % 5 == 0:
##    print("{}는 3이나 5의 배수입니다.".format(number))

##num = int(input("숫자를 입력해주세요: "))
##if num // 2 == 0:
##    print(f"{num}는 짝수입니다.")

##tem = int(input("현재 온도를 입력해주세요: "))
##if tem< 25:
##    print("시원한 날씨")
##if 25<= tem <30:
##    print("따뜻한 날씨")
##if tem >= 30:
##    print("더운 날씨")

##txt = input("문자열을 입력하세요: ")
##if " " in txt:
##    print("공백이 포함되어 있습니다.")
##if " " not in txt:
##    print("공백이 포함되어 있지 않습니다.")

##age = int(input("나이를 입력해주세요: "))
##if age >= 15:
##    print("15세 관람가")
##if age >= 12:
##    print("12세 관람가")
##if age > 0:
##    print("전체관람가")

##number = 3
##if number == 15:
##    print("이 숫자는 15입니다.")
##else:
##    print("이 숫자는 15가 아닙니다.")
##
##number = 3
##if number == 15:
##    print("이 숫자는 15입니다.")
##elif number == 3:
##    print("이 숫자는 3입니다.")
##else:
##    print("이 숫자는 3도 15도 아닙니다.")

##apple = int(input("사과의 개수를 입력해 주세요; "))
##if apple > 0:
##    print("사과가 있습니다.")
##else:
##    print("사과가 없습니다.")
##
##apple = int(input("사과의 개수를 입력해 주세요; "))
##if apple == 0:
##    print("사과는  10개 있습니다.")
##elif apple == 0:
##    print("사과는 하나도 없습니다.")

##apple = input("문장을 입력하세요: ")
##if " " in apple:
##    print("공백이 포함되어 있습니다.")
##else:
##    print("공백이 포함되어 있지 않습니다.")

##string = input("문자를 입력하세요: ")
##if string.isalpha():
##    print("알파벳 혹은 한글입니다.")
##elif string.isnumeric():
##    print("숫자입니다")
##else:
##    print("특수 문자입니다.")

##height = 170
##if height > 150:
##    print("키가 150 이상입니다.")
##if height > 160:
##    print("키가 160 이상입니다.")
##
##height = 170
##if height > 150:
##    print("키가 150 이상입니다.")
##elif height > 160:
##    print("키가 160 이상입니다.")

height = int(input("키를 입력해주세요: "))
if height > 150:
    print("키가 150 이상입니다.")
elif height > 160:
    print("키가 160 이상입니다.")
else:
    print("키가 150 미만입니다.")

height = int(input("키를 입력해주세요: "))
if height > 170:
    print("키가 170 이상입니다.")
elif height > 150:
    print("키가 150 이상입니다.")
elif height > 160:
    print("키가 160 이상입니다.")
else:
    print("키가 150 미만입니다.")
    
    
