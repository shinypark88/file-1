Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
print(type("안녕하세요"))
<class 'str'>
print(type(273))
<class 'int'>
print("안녕하세요")
안녕하세요
print('안녕하세요')
안녕하세요
print(""안녕하세요"라고 말했습니다")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('"안녕하세요"라고 말했습니다')
"안녕하세요"라고 말했습니다
print("'배가 고픕니다'라고 생각했습니다")
'배가 고픕니다'라고 생각했습니다
print(""\안녕하세요"\라고 말했습니다")
SyntaxError: unexpected character after line continuation character
print("\"안녕하세요\"라고 말했습니다")
"안녕하세요"라고 말했습니다
print('\'배가 고픕니다\'라고 생각했습니다')
'배가 고픕니다'라고 생각했습니다
print("안녕하세요\안녕하세요")
안녕하세요\안녕하세요
print(1+1)
2
print("안녕하세요\n안녕하세요")
안녕하세요
안녕하세요
print("안녕하세요\t안녕하세요")
안녕하세요	안녕하세요
print("\\ \\ \\ \\")
\ \ \ \
print("동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라 만세\n무궁화 삼천리 화려강산 대한사람\n대한으로 길이 보전하세")
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세
print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세""")
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세
print("""
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세
""")

동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세

print("""\
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세\
""")
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세
"문자열"+"문자열"
'문자열문자열'
print("안녕"+"하세요")
안녕하세요
print("안녕하세요"+"!")
안녕하세요!
print("안녕하세요"+1)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print("안녕하세요"+1)
TypeError: can only concatenate str (not "int") to str
print("안녕하세요"+"1")
안녕하세요1
print("안녕하세요"*3)
안녕하세요안녕하세요안녕하세요
print(3*"안녕하세요")
안녕하세요안녕하세요안녕하세요
print("문자 선택 연산자에 대하여 알아볼까요?")
문자 선택 연산자에 대하여 알아볼까요?
print("안녕하세요"[0])
안
print("안녕하세요"[1])
녕
print("안녕하세요"[2])
하
print("안녕하세요"[3])
세
print("안녕하세요"[4])
요
print("안녕하세요"[5])
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print("안녕하세요"[5])
IndexError: string index out of range
print("안녕하세요"[-1])
요
print("안녕하세요"[-2])
세
print("안녕하세요"[-3])
하
print("안녕하세요"[-4])
녕
print("안녕하세요"[-5])
안
print("안녕하세요"[1:4])
녕하세
print("안녕하세요"[0:2])
안녕
print("안녕하세요"[1:3])
녕하
print("안녕하세요"[2:4])
하세
print("안녕하세요:[1:])
      
SyntaxError: unterminated string literal (detected at line 1)
print("안녕하세요"[1:])
      
녕하세요
print("안녕하세요"[:3])
      
안녕하
print("안녕하세요"[10])
      
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print("안녕하세요"[10])
IndexError: string index out of range
print(len("안녕하세요"))
      
5
print(273)
      
273
print(52.273)
      
52.273
print(type(52))
      
<class 'int'>
print(type(52.273))
      
<class 'float'>
print(0)
      
0
print(type(0))
      
<class 'int'>
print(0.0)
      
0.0
print(0.0)
      
0.0
print(type(0.0))
      
<class 'float'>
print("5+7=", 5+7)
      
5+7= 12
print("5-7=", 5-7)
      
5-7= -2
print("5*7=", 5*7)
      
5*7= 35
print("5/7=", 5/7)
      
5/7= 0.7142857142857143
print("3//2=", 3//2)
      
3//2= 1
print("5%2=", 5%2)
      
5%2= 1
print("2**1=", 2**1)
      
2**1= 2
print("2**2=", 2**2)
      
2**2= 4
print("2**3=", 2**3)
      
2**3= 8
print("2**4=", 2**4)
      
2**4= 16
5+3*2
      
11
print(2+2-2*2/2*2)
      
0.0
print(2-2+2/2*2+2)
      
4.0
(5+3)*2
      
16
5+(3*2)
      
11
string="문자열"
      
number=273
      
string+number
      
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    string+number
TypeError: can only concatenate str (not "int") to str
print("안녕"+"하세요"*3)
      
안녕하세요하세요하세요
print(("안녕"+"하세요")*3)
      
안녕하세요안녕하세요안녕하세요
print("안녕"+("하세요"*3))
      
안녕하세요하세요하세요
print("안녕"+"하세요"*3)
      
안녕하세요하세요하세요
print("안녕"+("하세요"*3))
      
안녕하세요하세요하세요
pi=3.14159265
      
pi
      
3.14159265
pi=3.14159265
      
pi+2
      
5.14159265
pi-2
      
1.1415926500000002
pi*2
      
6.2831853
pi/2
      
1.570796325
pi%2
      
1.1415926500000002
pi*pi
      
9.869604378534024
pi+"문자열"
      
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    pi+"문자열"
TypeError: unsupported operand type(s) for +: 'float' and 'str'
pi=3.14159265
      
r=10
      
print("원주율=", pi)
      
원주율= 3.14159265
print("반지름=", r)
      
반지름= 10
print("원의 둘레=", 2*pi*r)
      
원의 둘레= 62.831853
print("원의 넓이=", r*r*pi)
      
원의 넓이= 314.159265
a+=10
      
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    a+=10
NameError: name 'a' is not defined
number=100
      
number+=10
      
number+=20
      
number+=30
      
print("number:", number)
      
number: 160
string = "안녕하세요"
      
string += "!"
      
string += "!"
...       
>>> print("string:", string)
...       
string: 안녕하세요!!
>>> input("인사말을 입력하세요>")
...       
인사말을 입력하세요>안녕하세요
'안녕하세요'
>>> string=input("인사말을 입력하세요>")
...       
인사말을 입력하세요>안녕하세요
>>> print(string)
...       
안녕하세요
>>> print(type(string))
...       
<class 'str'>
>>> number=input("숫자를 입력하세요>")
...       
숫자를 입력하세요>12345
\
>>> print(number)
...       
12345
>>> print(type(number))
...       
<class 'str'>
