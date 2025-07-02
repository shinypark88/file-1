Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============ RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0702-(1).py ============
Traceback (most recent call last):
  File "C:/Users/sw4_2/Desktop/수강생705/박서환/0702-(1).py", line 2, in <module>
    str1[0] = "D"
TypeError: 'str' object does not support item assignment
allignment = str(input(문자열을 입력하세요: ))
print(allignment[0::2])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
allignment = str(input("문자열을 입력하세요: "))
print(allignment[0::2])
SyntaxError: multiple statements found while compiling a single statement

============ RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0702-(1).py ============
문자열을 입력하세요: 가나다라마바사1234567
가다마사246

============ RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0702-(1).py ============
문자열을 입력하세요: 가나다라마바사1234567
나라바1357

============ RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0702-(1).py ============
문자열을 입력하세요: 가나다라마바사1234567
나라바1357
주민번호를 입력하세요(-포함): 100123-4567890
012

============ RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0702-(1).py ============
문자열을 입력하세요: 가나다라마바사1234567
나라바1357
주민번호를 입력하세요(-포함): 100123-4567890
0123
스타벅스에서만나
song = """\
동해물과 백두산이 마르고
닳도록

하느님이 보우하사
우리나라 만세

무궁화 삼천리 화려 강산

대한사람, 대한으로
길이 보전하세\
"""
print(song[15])
도
print(song[17])


print(song[18])


print(song[30])
리
print(song[25])
우
print(song[30:31])
리
print(song[34:36])
만세
print(song[50])
산
print(song[60])
한
print(song[70])
세
print(song[68:70])
전하
print(song[69:71])
하세
part_song_1 = """\
동해물과 백두산이 마르고
닳도록

하느님이 보우하사
우리나라 만세\
"""
part_song_2 = """\
대한사람, 대한으로
길이 보전하세\
"""
print(part_song_1)\
                    
SyntaxError: multiple statements found while compiling a single statement
print(part_song_1)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(part_song_1)
NameError: name 'part_song_1' is not defined
part_song_1 = """\
동해물과 백두산이 마르고
닳도록

하느님이 보우하사
우리나라 만세\
"""
print(part_song_1)
동해물과 백두산이 마르고
닳도록

하느님이 보우하사
우리나라 만세
part_song_1 = """\
동해물과 백두산이 마르고
닳도록

하느님이 보우하사
우리나라 만세\
"""
part_song_2 = """\
대한사람, 대한으로
길이 보전하세\
"""
print(part_song_1 + "강세"\n +part_song_2)
SyntaxError: unexpected character after line continuation character
print(part_song_1 + "강세\n" + part_song_2)
동해물과 백두산이 마르고
닳도록

하느님이 보우하사
우리나라 만세강세
대한사람, 대한으로
길이 보전하세
part_song_1 = """\
동해물과 백두산이 마르고
닳도록

하느님이 보우하사
우리나라\
"""
part_song_2 = """\
대한사람, 대한으로
길이 보전하세\
"""
print(part_song_1 + "강세" + part_song_2)
동해물과 백두산이 마르고
닳도록

하느님이 보우하사
우리나라강세대한사람, 대한으로
길이 보전하세
print(part_song_1 + "강세\n*2" + part_song_2)
동해물과 백두산이 마르고
닳도록

하느님이 보우하사
우리나라강세
*2대한사람, 대한으로
길이 보전하세
print(part_song_1 + "강세\n\n" + part_song_2)
동해물과 백두산이 마르고
닳도록

하느님이 보우하사
우리나라강세

대한사람, 대한으로
길이 보전하세
str1 = "파이썬, c언어, HTML/CSS, JAVA"
logic1 = "파이썬" in str1
print(logic1)
True
logic2 = "C#" in str1
print(logic2)
False
poison = "이 파이썬 문장에는 독이 있어!"
print("독" in poison)
True
print("약" not in poison)
True
number = 12345678
print(1 in number)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(1 in number)
TypeError: argument of type 'int' is not iterable
number = "1245678"
print(1 in number)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(1 in number)
TypeError: 'in <string>' requires string as left operand, not int
number = "12345678"
print("1" in number)
True
message = "다른 연산자끼리 섞어쓰는 것도 가능해."
print("연산자" in message[2:10])
True
print("연산자" not in "정말 다양한 방법으로" + "연산자를 쓸 수 있어")
False
string = "문자열함수 & 문자열 함수"
print(string.find("자열"))
1
print(string.find("자열"))
1








=========================================================== RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/....py ==========================================================
문자열 입력> 안녕하세요
문자열 입력> 아침입니다
안녕하세요 아침입니다
c = str(b)
b = str(a)
a = str(c)
print(a, b)
아침입니다 안녕하세요
print(string.find("함수"))
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(string.find("함수"))
NameError: name 'string' is not defined. Did you forget to import 'string'?
string = "문자열 함수 & 문자열 함수"
print(string.find("함수"))
4
print(string.rfind("자열"))
10
print(string.rfind("함수"))
13
string = "HelloPython"
number = "12345"
print(string.isalpha())
True
print(string.isnumberic())
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print(string.isnumberic())
AttributeError: 'str' object has no attribute 'isnumberic'. Did you mean: 'isnumeric'?
print(string.isnumeric())
False
print(number.isaslpha())
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print(number.isaslpha())
AttributeError: 'str' object has no attribute 'isaslpha'. Did you mean: 'isalpha'?
print(number.isalpha())
False
print(number.isnumeric())
True
bab = "국밥 컵밥 초밥 김밥 비빔밥"
print("가장 앞에 있는 밥은 "+ str(bab.find("밥"))+"번째!")
가장 앞에 있는 밥은 1번째!
print("가장 뒤에 있는 밥은 "+ str (bab.rfind("밥")) + "번째!")
가장 뒤에 있는 밥은 14번째!

=========================================================== RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/....py ==========================================================
>1번째 숫자: 100
>2번째 숫자: 10

 처음 입력했던 100가 10보다 더 큽니다
eng = "FunnyPython"
>>> kor = "신나는파이썬"
>>> blank = "B L A N K"
>>> print(eng.isalpha())
True
>>> print(kor.isalpha())
True
>>> print(blank.isalpha())
False
>>> num = "20240505"
>>> date = "2024.05.05"
>>> print(num.isnumeric())
True
>>> print(date.isnumeric())
False
>>> sentence = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다."
>>> print("첫번째 완두콩은"+str(sentence.find("완두콩"))+"번째에 있습니다.")
첫번째 완두콩은13번째에 있습니다.
>>> print("두번째 완두콩은"+str(sentence.rfind("완두콩"))+"번째에 있습니다"))
SyntaxError: unmatched ')'
>>> print("두번째 완두콩은"+str(sentence.rfind("완두콩"))+"번째에 있습니다")
두번째 완두콩은26번째에 있습니다
>>> print(sentence[13:24])
완두콩 깐 빈 콩깍지
>>> print(sentence.rfind("강낭콩"))
39
>>> print(sentence[39:48])
강낭콩 깐 빈 콩
>>> print(sentence[39:50])
강낭콩 깐 빈 콩깍지
>>> email = str(input(이메일을 입력해주세요: ))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> email = str(input("이메일을 입력해주세요: "))
이메일을 입력해주세요:  leesam@coding.co.kr
>>> print(email.find("coding"))
8
>>> print(email[:8])
 leesam@
>>> print(email.find("@"))
7
>>> print(email[:7])
 leesam
>>> print("이 이메일의 아이디는"+email[:7}+"입니다.")
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
print("이 이메일의 아이디는"+email[:7}+"입니다.")
>>> print("이 이메일의 아이디는"+email[:7]+"입니다.")
이 이메일의 아이디는 leesam입니다.
