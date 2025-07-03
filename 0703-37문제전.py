Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
string = "문자열_함수는_참_다양해요"
split_string = string.split("_")
print(split_string)
['문자열', '함수는', '참', '다양해요']
string = string.replace("다양해", "멋져")
print(string)
문자열_함수는_참_멋져요
string = "Python Upper Lower"
print(string.upper())
PYTHON UPPER LOWER
print(string.lower())
python upper lower
dessert = "초코케이크 녹차마카롱 모카라떼"
cake, macaron, coffee = dessert.split(" ")
print("케이크:", cake)
케이크: 초코케이크
print("마카롱:", macaron)
마카롱: 녹차마카롱
print("커피:", coffee)
커피: 모카라떼

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0703-2.py =============
int 둘 입력: 7895 651
7895
651
7895651
8546
a,b,c = input("알파벳 셋 입력: ").split()
알파벳 셋 입력: g d r
print(c,b,a,sep=">")
r>d>g
r1,r2 = input("float 둘 입력: ").split()
float 둘 입력: 310.12 52.87
r1 = float(r1)
r2 = float(r2)
print(r1*r2)
16396.0444
message = """대공원에 봄 벚꽃 놀이는
낮 봄 벚꽃 놀이보다
밤 봄ㅂ 벚꽃 놀이니라."""

message = """대공원 봄 벚꽃 놀이는
낮 봄 벚꽃 놀이보다
밤 봄 벚꽃 놀이니라."""

print(message.replace("벚꽃,"개나리"))
                      
SyntaxError: unterminated string literal (detected at line 1)
print(message.replace("벚꽃", "개나리"))
                      
대공원 봄 개나리 놀이는
낮 봄 개나리 놀이보다
밤 봄 개나리 놀이니라.
win = "WindowXP"
                      
update = win.replace("XP", "11")
                      
print(update + "로 업데이트 됐습니다.")
                      
Window11로 업데이트 됐습니다.
japangi = """이 자판기 안에는
포도맛 사이다,
포도맛 쥬스,
포도맛 슬러쉬
가 있습니다."""
                      
taste = input("무슨 맛 자판기로 바꿀까요: ")
                      
무슨 맛 자판기로 바꿀까요: 파인애플
print(japangi.replace("포도", taste))
                      
이 자판기 안에는
파인애플맛 사이다,
파인애플맛 쥬스,
파인애플맛 슬러쉬
가 있습니다.
message = input("영어로 문장을 적어주세요: ")
                      
영어로 문장을 적어주세요: Welcome to DIsney World!
print(message.upper()0
      
SyntaxError: '(' was never closed
print(message.upper())
      
WELCOME TO DISNEY WORLD!
print(message.lower())
      
welcome to disney world!
message = "abcD 1234 ..@@ !!!"
      
trans = message.upper()
      
print(trans)
      
ABCD 1234 ..@@ !!!
phone_number = str(input("전화번호 입력: "))
      
전화번호 입력: 010-115-5648
print(phone_number.replace(-, \n)
      
SyntaxError: invalid syntax
print(phone_number.replace(-,\n)
      
SyntaxError: invalid syntax
print(phone_number.replace("-",\n)
      
SyntaxError: unexpected character after line continuation character
sepphone_number = phone_number.split("-")
      
p1, p2, p3 = phone_number.split("-")
      
print("""\
p1
p2
p2\
""")
      
p1
p2
p2
print(p1)
      
010
print(p2)
      
115
print(p3)
      
5648
print("""p1
p2
p3""")
      
p1
p2
p3
print(p1
      pw
      
SyntaxError: '(' was never closed
print(p1
      p2
      
SyntaxError: '(' was never closed
print(p1\np2\np3)
      
SyntaxError: unexpected character after line continuation character
print(p1 \n p2 \n p3)
      
SyntaxError: unexpected character after line continuation character
file1 = str(input("전화번호 입력: "))
      
전화번호 입력: **
file_1 = str(input("파일명을 입력해주세요: "))
      
파일명을 입력해주세요: image.jpg
file_png = file_1.replace("jpg", "png")
      
print(file_1+"파일을"+file_png+"파일로 변경하였습니다.")
      
image.jpg파일을image.png파일로 변경하였습니다.
text = "Hello, Python! Hello, string!"
      
print(text.upper)
      
<built-in method upper of str object at 0x00000297BC0B2970>
print(text.upper())
      
HELLO, PYTHON! HELLO, STRING!
print(text.lower())
      
hello, python! hello, string!
string = "이 문장안에 있는 글자의 수는 몇개일까요?"
      
print(len(string))
      
23
string = "파이썬 {0}번 복습하기".format(10)
      
print(string)
      
파이썬 10번 복습하기
string2 = f"문자열도 {10:8.2f}번 복습하기"
      
print(string2)
      
문자열도    10.00번 복습하기
tips = "len 함수로 문자열의 갯수를 세봅시다."
      
print(len(tips))
      
22
number = 15335
      
print(len(number))
      
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    print(len(number))
TypeError: object of type 'int' has no len()
year = input("태어난 해를 입력해주세요: ")
      
태어난 해를 입력해주세요: 2000
month = input("태어난 월을 입력해주세요: ")
      
태어난 월을 입력해주세요: 10
day = input("태어난 일을 입력해주세요: ")
      
태어난 일을 입력해주세요: 3
date =f"{}년 {}월 {}일"
      
SyntaxError: f-string: valid expression required before '}'
date = f"{year}년 {month}월 {day}일"
      
print(date)
      
2000년 10월 3일
print("당신의 생일은"+date+"입니다. Happy Birthday!")
      
당신의 생일은2000년 10월 3일입니다. Happy Birthday!
print("당신의 생일은 "+date+"입니다. Happy Birthday!")
      
당신의 생일은 2000년 10월 3일입니다. Happy Birthday!
num1 = f"{10}/{20}"
      
num2 = f"[{10.10}/{20.20}]"
      
print(num1)
      
10/20
print(num2)
      
[10.1/20.2]
pi = 3.14
      
num3 = f"[{pi:4.1f}/{pi:110.0f}]"
      
print(num3)
      
[ 3.1/                                                                                                             3]
num3 = f"[{pi:4.1f}/{pi:010.0f}]"
      
print(num3)
      
[ 3.1/0000000003]
str1 = "Python"
      
str2 = f"[{str1:10s]}/{str1:010s}]"
      
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    str2 = f"[{str1:10s]}/{str1:010s}]"
ValueError: Invalid format specifier '10s]' for object of type 'str'
str2 = f"[{str1:10s}/{str1:010s}]"
      
print(str2)
      
[Python    /Python0000]
mvname = input("영화 제목을 입력하세요: ")
      
영화 제목을 입력하세요: 스파르타 리턴즈
mvyear = input("개봉 연도를 입력하세요: ")
      
개봉 연도를 입력하세요: 2011
mvactor = input("주연 배우를 입력하세요: ")
      
주연 배우를 입력하세요: 이샘
text = "{}은(는} {}년에 개봉한 {} 주연의 영화입니다.".format(mvname, mvyear, mvactor)
      
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    text = "{}은(는} {}년에 개봉한 {} 주연의 영화입니다.".format(mvname, mvyear, mvactor)
ValueError: Single '}' encountered in format string
text = "{0}은(는} {1}년에 개봉한 {2} 주연의 영화입니다.".format(mvname, mvyear, mvactor)
      
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    text = "{0}은(는} {1}년에 개봉한 {2} 주연의 영화입니다.".format(mvname, mvyear, mvactor)
ValueError: Single '}' encountered in format string
text = "{}은(는} {}년에 개봉한 {} 주연의 영화입니다.".format(mvname,mvyear,mvactor)
      
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    text = "{}은(는} {}년에 개봉한 {} 주연의 영화입니다.".format(mvname,mvyear,mvactor)
ValueError: Single '}' encountered in format string
text = "{}은(는) {}년에 개봉한 {} 주연의 영화입니다.".format(mvname,mvyear,mvactor)
      
print(text)
      
스파르타 리턴즈은(는) 2011년에 개봉한 이샘 주연의 영화입니다.
input("아이디를 입력해주세요(6글자 이상): ")
      
아이디를 입력해주세요(6글자 이상): leesam001
'leesam001'
pswd = input("아이디를 입력해주세요(6글자 이상): ")
      
아이디를 입력해주세요(6글자 이상): leesam001
print(pswd[:3]+"*"*5)
      
lee*****
number = 10+2.3
      
msg = "이샘"+"코딩"+"학원"
      
ㅜㅕㅡㅠㄷㄱ = 10-2.3
      
number = 10-2.3
      
number = 10*2.3
      
msg = "이샘코딩학원"*5
      
ㅜㅕㅡㅠㄷㄱ = 10/2.3
      
number = 10/2.3
      
num1 = int(input("첫번 째 숫자 입력: "))
      
첫번 째 숫자 입력: 22
num2 = int(input("두 번째 숫자 입력: "))
      
두 번째 숫자 입력: 13
print(f"num1 + num2 = {num1 +num2}")
      
num1 + num2 = 35
print(f"num1 - num2 = {num1 - num2}")
      
num1 - num2 = 9
print(f"num1 * num2 = {num1 * num2}")
      
num1 * num2 = 286
print(f"(num1 / num2 = {num1 / num2.2}")
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(f"num1 / num2 = {num1 / num2.2}")
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(f"num1 / num2 = {num1 / num2.2f}")
      
SyntaxError: invalid decimal literal
print(f"num1 / num2 = {num1 / num2:.2f}")
      
num1 / num2 = 1.69
num1 = input("숫자를 입력해주세요: ")
      
숫자를 입력해주세요: 123
print(num1+50)
      
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    print(num1+50)
TypeError: can only concatenate str (not "int") to str
num2 = int(num1)
      
print(nu2+50)
      
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    print(nu2+50)
NameError: name 'nu2' is not defined. Did you mean: 'n2'?
print(num2+50)
      
173
print(num2-50)
      
73
print(num2*50)
      
6150
print(num2/50:.3f)
      
SyntaxError: invalid decimal literal
num3 = float(num1)
      
print(num3/50:.3f)
      
SyntaxError: invalid decimal literal
print(f"num3/50:.3f")
      
num3/50:.3f
print(f"{num1/50:.3f}")
      
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    print(f"{num1/50:.3f}")
TypeError: unsupported operand type(s) for /: 'str' and 'int'
print(f"{num2/50:.3f}")
      
2.460
w1 = 3
      
w2 = 4
      
h = 5
      
print(f"사다리꼴의 넓이는 ({w1}+{w2})*{h}/2")
      
사다리꼴의 넓이는 (3+4)*5/2
print(사다리꼴의 넓이는 ({}+{})*{}/2 = {}.format(w1, w2, h,(w1+w2)*h/2))
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("사다리꼴의 넓이는 ({}+{})*{}/2 = {}".format(w1, w2, h,(w1+w2)*h/2))
...       
사다리꼴의 넓이는 (3+4)*5/2 = 17.5
>>> number = 10//3
...       
>>> print(number)
...       
3
>>> number = 10 % 3
...       
>>> print(number)
...       
1
>>> number = 10 ** 2
...       
>>> print(number)
...       
100
>>> number1 = 4+3*2
...       
>>> print(number)
...       
100
>>> number2 = (2+3)*5
...       
>>> print(number2)
...       
25
>>> print(number1)
...       
10
>>> num1 = int(input("첫 번째 숫자 입력: "))
...       
첫 번째 숫자 입력: 11
>>> num2 = int(input("두 번째 숫자 입력: "))
...       
두 번째 숫자 입력: 3
>>> print(f"num1 // num2 = {num1 //num2}")
...       
num1 // num2 = 3
>>> print(f"num1 % num2 = {num1 %num2}")
...       
num1 % num2 = 2
>>> print(f"num1 ** num2 = {num1 **num2}")
...       
num1 ** num2 = 1331
