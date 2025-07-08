Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
remainder = 1357 // 10
일의자리 = 1357 % 10
remainder1 = remainder // 10
십의자리 = remainder % 10
천의자리 = remainder // 10
천의자리 = remainder1 // 10
백의자리 = remainder1 % 10
print(일의자리\n십의자리\n백의자리\n천의자리)
SyntaxError: unexpected character after line continuation character
print("""
일의자리
십의자리
백의자리
천의자리""")

일의자리
십의자리
백의자리
천의자리

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
7
5
3
1

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
숫자 5개를 입력해주세요: 
============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
숫자 5개를 입력해주세요: 11 2 31 101 7
Traceback (most recent call last):
  File "C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py", line 12, in <module>
    number = int(input("숫자 5개를 입력해주세요: "))
ValueError: invalid literal for int() with base 10: '11 2 31 101 7'

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
숫자 5개를 입력해주세요: 11 2 31 101 7
30.4
txt = input("문자열을 입력해주세요: ")
문자열을 입력해주세요: hello world!
txt1 = txt.split(" ")
print(txt1)
['hello', 'world!']
txt2 = txt1.upper[0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    txt2 = txt1.upper[0]
AttributeError: 'list' object has no attribute 'upper'

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
숫자 5개를 입력해주세요: 11 2 31 101 7
30.400

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
HELLO

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
H

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
HELLO

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
HelloWorld!

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
<built-in method upper of str object at 0x0000021C2CBB3960>



============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
HELLO

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello World!
Traceback (most recent call last):
  File "C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py", line 21, in <module>
    print(txt1.upper([0]))
AttributeError: 'list' object has no attribute 'upper'

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
Traceback (most recent call last):
  File "C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py", line 21, in <module>
    print(txt1.upper([0]))
AttributeError: 'list' object has no attribute 'upper'

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
Traceback (most recent call last):
  File "C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py", line 19, in <module>
    txt2 = txt1[0].sep[0]
AttributeError: 'str' object has no attribute 'sep'

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
Traceback (most recent call last):
  File "C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py", line 19, in <module>
    txt2 = sep.txt1[0]
NameError: name 'sep' is not defined. Did you mean: 'set'?

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
txt2+=txt3

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
HelloHello

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
HelloHello

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
HelloHello
HelloHello

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: hello world!
HelloWorld!

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
문자열을 입력해주세요: 
============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
첫 번째 숫자 입력: 11
두 번째 숫자 입력: 23
num1 >= num2 = False
num1 <= num2 = True

============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
첫 번째 숫자 입력: 11
두 번째 숫자 입력: 23
num1 >= num2 = False
num1 <= num2 = True
num1 == num2 = False
num1 != num2 = True
>>> 
============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
첫 번째 숫자 입력: 11
두 번째 숫자 입력: 22
세 번째 숫자 입력: 33
<class 'bool'> <class 'bool'>
num1<num2<num3 = True
num1>num2>num3 = False
>>> 
============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
첫 번째 숫자 입력: 
============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
숫자를 입력해주세요: 111
True
False
>>> 
============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
숫자를 입력해주세요: 111
False
>>> 
============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
숫자를 입력해주세요: 55
30<num<60
>>> 
============= RESTART: C:/Users/sw4_2/Desktop/수강생705/박서환/0708수업.py =============
숫자를 입력해주세요: 55
True
