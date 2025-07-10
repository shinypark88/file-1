##num1 = float(input("첫 번째 숫자: "))
##num2 = float(input("두 번째 숫자: "))
##num3 = float(input("세 번째 숫자: "))
##
##average = (num1+num2+num3) / 3
##if average >= 50:
##    print("평균이 50 이상입니다.")
##else:
##    print("평균이 50 미만입니다.")
##
##email = input("이메일 주소를 입력해주세요: ")
##if "@" in email and "." in email:
##    print("유효한 이메일 주소입니다.")
##elif "@" in email:
##    print("'.'가 없습니다.")
##elif "." in email:
##    print("'@'가 없습니다.")
##else:
##    print("유효하지 않은 이메일 주소입니다.")
##
##url = input("url을 입력하세요: ")
##if url.find("http://")>=0:
##    print("HTTP 프로토콜입니다.")
##elif url.find("https://")>=0:
##    print("HTTPS 프로토콜입니다.")
##elif url.find("ftp://")>=0:
##    print("FTP 프로토콜입니다.")
##else:
##    print("알 수 없는 프로토콜입니다.")

##key = input("방향키를 입력해주세요: ")
##if key == "w":
##    print("위 방향키를 입력하셨습니다.")
##elif key == "a":
##    print("좌 방향키를 입력하셨습니다.")
##elif key == "s":
##    print("아래 방향키를 입력하셨습니다.")
##elif key == "d":
##    print("우 방향키를 입력하셨습니다.")
##else:
##    print("잘못 입력하셨습니다.")

##num = int(input("숫자를 입력해주세요: "))
##if num > 0:
##    print("number은 양수입니다.")
##elif num == 0:
##    print("number은 0입니다.")
##elif num < 0:
##    print("number은 음수입니다.")
##
##if num % 2 == 0:
##    print("number은 짝수입니다.")
##elif num % 2 == 1:
##    print("number은 홀수입니다.")

##num = int(input("숫자를 입력해주세요: "))
##if num % 3 == 0:
##    print("이 숫자는 3의 배수입니다.")
##if num % 6 == 0:
##    print("이 숫자는 6의 배수입니다.")
##if num % 9 == 0:
##    print("이 숫자는 9의 배수입니다.")

##txt = input("알파벳을 입력해주세요: ")
##if txt == txt.upper():
##    print("대문자입니다.")
##else:
##    print("소문자입니다.")

##num = int(input("숫자를 입력해주세요: "))
##if 10 <= num <= 99:
##    print("두자리 숫자입니다.")
##else:
##    print("두자리 숫자가 아닙니다.")

##print("숫자 1과 숫자 2를 입력해주세요.")
##number1 = input()
##number2 = input()
##
##if number1> number2:
##    print("숫자 1이 숫자2보다 큽니다.")
##else:
##    if number1 < number2:
##        print("숫자 2가 숫자1보다 큽니다.")
##    else:
##        print("숫자 1과 숫자 2가 같습니다.")

##print("숫자 1과 숫자 2를 입력해주세요.")
##number1 = input()
##number2 = input()
##
##if number1 > number2:
##    print("숫자 1이 숫자 2보다 큽니다.")
##elif number1 < number2:
##    print("숫자 2가 숫자 1보다 큽니다.")
##else:
##    print("숫자 1과 숫자 2가 같습니다.")

##score = 75
##if score > 90:
##    print("성적은 A등급 입니다.")
##elif score > 80:
##    print("성적은 B등급 입니다.")
##elif score > 70:
##    print("성적은 C등급입니다.")
##elif score > 60:
##    print("성적은 D등급입니다.")
##else:
##    print("성적은 F등급입니다.")

##weight = int(input("무게를 입력해주세요: "))
##express = input("특송여부 (y/n) : ")
##domestic = input("국내 배송 여부 (y/n) : ")
##
##if weight <= 2 and (express == "y" or domestic == "y"):
##    print("무료 배송입니다.")
##elif weight <= 5 and (express == "y" or domestic == "y"):
##    print("유료 배송입니다.")
##else:
##    print("배송 불가합니다.")

##player_atk = int(input("현재 공격력: "))
##player_exp = 10
##monster_atk = 100
##
##if monster_atk > player_atk:
##    print("몬스터의 승리!:")
##    print("경험치를 잃었다...")
##    player_exp -= 5
##elif monster_atk < player_atk:
##    print("플레이어의 승리!")
##    print("경험치를 얻었다!1")
##    player_exp += 5
##else:
##    print("몬스터와의 무승부")
##    print("아무런 일도 일어나지 않았다.")
##
##print(f"현재 경험치 : {player_exp} / 다음 레벨업까지 : {100-player_exp}")

##print("[계산기 프로그램]")
##choice = input("연산자를 입력해주세요. (+, -, *, /): ")
##num1 = float(input("첫 번째 숫자: "))
##num2 = float(input("두 번째 숫자: "))
##if choice == "+":
##    result = num1 + num2
##    print(f"결과: {num1} + {num2} = {result}")
##elif choice == "-":
##    result = num1 - num2
##    print(f"결과: {num1} - {num2} = {result}")
##elif choice == "*":
##    result = num1 * num2
##    print(f"결과: {num1} * {num2} = {result}")
##elif choice == "/":
##    if num2 != 0:
##        result = num1 / num2
##        print(f"결과: {num1} / {num2} = {result}")
##    else:
##        print("오류: 0으로 나눌 수 없습니다.")
##else:
##    print("연산자를 잘못 입력하셨습니다.")

##num = int(input("숫자를 입력해주세요.(0~100): "))
##if 45 <= num <= 55:
##    print("Perfect!!")
##elif 35 <= num < 45 or 55 < num <= 65:
##    print("Excellent!!")
##else:
##    print("Good!!")

##yr = int(input("연도를 입력해주세요: "))
##if yr % 400 ==0 or (yr % 4 == 0 and yr % 100 != 0):
##    print("윤년입니다.")
##else:
##    print("윤년이 아닙니다.")

##num1 = int(input("첫번째 숫자를 입력해 주세요: "))
##num2 = int(input("두번째 숫자를 입력해 주세요: "))
##num3 = int(input("세번째 숫자를 입력해 주세요: "))
##
##if (num1 + num3) /2 == num2:
##    print("스트레이트!")
##else:
##    print("X")

##num1 = int(input("첫번째 숫자를 입력해 주세요: "))
##num2 = int(input("두번째 숫자를 입력해 주세요: "))
##num3 = int(input("세번째 숫자를 입력해 주세요: "))
##
##if num1 < num2 < num3:
##    print( num1, num2, num3)
##elif num2 < num3 < num1:
##    print(num2, num3, num1)
##elif num1 < num2 < num3:
##    print(num1, num3, num2)
##elif num2 < num1 < num3:
##    print(num2, num1, num3)
##elif num3 < num1 < num2:
##    print(num3, num1, num2)
##elif num3 < num2 < num1:
##    print(num3, num2, num1)

##count = 0
##while count < 3:
##    print("{0}번째의 while문!".format(count))
##    count += 1
##
##while True:
##    print("반복중~")

##while True:
##    print("무한 반복중...")

count = 0
while count < 3:
    print("{0}회 반복 중...".format(count))
    count+=1

count = 0
while count < 100:
    if count % 3 ==0:
        print("3의 배수: {0}".format(count))
    count+=1
