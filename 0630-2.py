Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num1=17
print(num1)
17
print(f'10진수 17 = {num1}')
10진수 17 = 17
print(f'10진수 17의 8진수 = {num1:o}')
10진수 17의 8진수 = 21
print(10진수 17의 16진수 = {num1:x}')
      
SyntaxError: unterminated string literal (detected at line 1)
print(f'10진수 17의 16진수 = {num1:x}')
      
10진수 17의 16진수 = 11
num2=100
      
print(f"{num2}{num2:c}")
      
100d
float1=1234.567
      
print(float1)
      
1234.567
print(f"기본 출력  {float1:f}")
      
기본 출력  1234.567000
print(f"지수표기법 {float1:f}")
      
지수표기법 1234.567000
print(f"지수표기법 {float1:e}")
      
지수표기법 1.234567e+03
print(f"소수 둘째자리까지 {float1:x}")
      
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(f"소수 둘째자리까지 {float1:x}")
ValueError: Unknown format code 'x' for object of type 'float'
print(f"소수 둘째자리까지 {float1:.2f}")
      
소수 둘째자리까지 1234.57
txt1= "Hello"
      
txt2= "World!"
      
print(f'기본출력\n{txt1:s} {txt2:s}')
      
기본출력
Hello World!
print(f'7칸 출력\n{txt1:7s} {txt2:7s}?')
      
7칸 출력
Hello   World! ?
\
print(f'넓이는 r*r*pi')
      
넓이는 r*r*pi
r=5
      
pi=3.14
      
print(f'넓이는 r*r*pi')
      
넓이는 r*r*pi
r=5
      
pi=3.14
      
print(f'넓이는 {r} *{r} * {pi}')
      
넓이는 5 *5 * 3.14
print(f'넓이는 {r} * {r} * {pi} = r * r * pi')
      
넓이는 5 * 5 * 3.14 = r * r * pi
print(f'넓이는 {r} * {r} * {pi} = {r * r * pi}')
      
넓이는 5 * 5 * 3.14 = 78.5
golden_ratio = 1.61804
      
print(f'소수 첫째 자리까지 출력: {golden ratio:.1f}')
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(f'소수 첫째 자리까지 출력: {golden_ratio:,1f}')
      
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(f'소수 첫째 자리까지 출력: {golden_ratio:,1f}')
ValueError: Invalid format specifier ',1f' for object of type 'float'
print(f'소수 첫째 자리까지 출력: {golden_ratio:.1f}')
      
소수 첫째 자리까지 출력: 1.6
print(f'소수 둘째자리까지 출력: {golden ratio:.2f}')
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(f;소수 첫째 자리까지 출력: {golden ratio: .1f}')
      
SyntaxError: invalid decimal literal
print(f'소수 첫째 자리까지 출력: {golden_ratio: .1f}')
      
소수 첫째 자리까지 출력:  1.6
print(f'소수 둘째 자리까지 출력: {golden_ratio:.2f}')
      
소수 둘째 자리까지 출력: 1.62
print(f'소수 셋쨰 자리까지 출력: {golden_ratio:.3f')
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
print(f'소수 셋째 자리까지 출력: {golden_ratio: .3f}')
      
소수 셋째 자리까지 출력:  1.618
print(f'소수 넷째 자리까지 출력: {golden_ratio: .4f}')
      
소수 넷째 자리까지 출력:  1.6180
passwd=input("비밀번호 : ")
      
비밀번호 : 
============================================================= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환.py ============================================================
비밀번호 : 
id : 
 입력
print(int("30000"), int(50.0), int(True))
      
30000 50 1
print(float("3.14"), float(5), float(False))
      
3.14 5.0 0.0
print(str(5), str(1,23), str(True))
      
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(str(5), str(1,23), str(True))
TypeError: str() argument 'encoding' must be str, not int
print(str(5), str(1.23), str(True))
      
5 1.23 True
egg=input("계란은 몇 개?")
      
계란은 몇 개? 8
print(egg, type(egg))
      
 8 <class 'str'>
egg=int(egg)
      
print(egg, type(egg))
      
8 <class 'int'>
attack = input("공격력은?")
      
공격력은?10
scale = input("배율은?")
      
배율은?2.2
print("데미지는 ", attack*scale)
      
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print("데미지는 ", attack*scale)
TypeError: can't multiply sequence by non-int of type 'str'
attack = int(input(:"공격력은?")
             
SyntaxError: invalid syntax
attack = int(input("공격력은?")
             10
             
SyntaxError: '(' was never closed
attack = =int(input("공격력은?"))
             
SyntaxError: invalid syntax
attack = int(input("공격력은?"))
             
공격력은?10
scale = int(input("배율은?"))
             
배율은?2.2
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    scale = int(input("배율은?"))
ValueError: invalid literal for int() with base 10: '2.2'
attack= int(input("공격력은?"))
             
공격력은?10
scale = float(input("배율은?"))
             
배율은?2.2
print("데미지는 ", attack * scale)
             
데미지는  22.0
minute = input("분을 입력하세요: ")
             
분을 입력하세요: 10
minute = int(minute)
             
second = 60*minute
             
text = str(minute)+"분="+str(second)+"초"
             
print(text)
             
10분=600초
nickname = str(input("닉네임을 입력하세요: "))
             
닉네임을 입력하세요: ABC
text = "환영합니다"+str(nickname)
             
text = "환영합니다"+str(nickname)+"님!"
             
print(text)
             
환영합니다ABC님!
nickname = str(input("닉네임을 입력하세요: "))
             
닉네임을 입력하세요: ABC
text = "환영합니다" + str(nickname) + "님!"
             
print(text)
             
환영합니다ABC님!
float(input("실수를 입력하세요: ")
      output = float(input("실수를 입력하세요: "))
      
SyntaxError: '(' was never closed
output = float(input("실수를 입력하세요: "))
      
실수를 입력하세요: 5.6789
text = output * 10
      
print(text)
      
56.788999999999994
text2 = output*10
      
print(text2)
      
56.788999999999994
number 1 = int(input("첫번째 숫자를 입력하세요: ")
               
SyntaxError: invalid syntax
num1 = int(input("첫번째 숫자를 입력하세요: "))
               
첫번째 숫자를 입력하세요: 32
num2 = int(input("두번째 숫자를 입력하세요: "))
               
두번째 숫자를 입력하세요: 40
num3 = int(input("세번째 숫자를 입력허세요: "))
               
세번째 숫자를 입력허세요: 5
output = num1+num2+num3
               
\
print(output)
               
77
text = "총합은" +num1+num2+num3
               
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    text = "총합은" +num1+num2+num3
TypeError: can only concatenate str (not "int") to str
text = "총합은" +str(num1+num2+num3)
               
print(text)
               
총합은77
r = int(input("반지름을 입력하세요: "))
               
반지름을 입력하세요: 5
pi=3.14
               
s = "원의 넓이는" + str(r * r* pi)
               
print(s)
               
원의 넓이는78.5
ㅣ = "원의 둘레길이는" + str(2 * pi* r)
...                
>>> print(l)
...                
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    print(l)
NameError: name 'l' is not defined
>>> L = "원의 둘레길이는" +str(2*pi*r)
...                
>>> print(L)
...                
원의 둘레길이는31.400000000000002
>>> L = "원의 둘레길이는" +str(pi*r*2)
...                
>>> print(L)
...                
원의 둘레길이는31.400000000000002
>>> side1 = int(input("윗변을 입력하세요 : "))
...                
윗변을 입력하세요 : 3
>>> side2 = int(input("아랫변을 입력하세요: "))
...                
아랫변을 입력하세요: 4
>>> height = int(input("높이를 입력하세요: "))
...                
높이를 입력하세요: 5
>>> text = "사다리꼴의 넓이는"+ side1*side2*height
...                
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    text = "사다리꼴의 넓이는"+ side1*side2*height
TypeError: can only concatenate str (not "int") to str
>>> text = "사다리꼴의 넓이는"+ str(side1+side2)*height/2)
...       
SyntaxError: unmatched ')'
>>> text = "사다리꼴의 넓이는"+ str(side1+side2)*height/2))
...              
SyntaxError: unmatched ')'
>>> text = "사다리꼴의 넓이는"+ str((side1+side2)*height/2)
...              
>>> print(text)
...              
사다리꼴의 넓이는17.5
>>> print(L:.2f)
...              
SyntaxError: invalid decimal literal
