Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num1=10
print(num1, type(num1))
10 <class 'int'>
num2=3.14
print(num2, type(num2))
3.14 <class 'float'>
m_str="안녕하세요"
print(m_str, type(m_str))
안녕하세요 <class 'str'>
print(1+1, type(1+1))
2 <class 'int'>
print(0.3+2.04, type(0.3+2.04))
2.34 <class 'float'>
print(1+2.3, type(1+2.3))
3.3 <class 'float'>
print(f">{'abc':5s}<")
>abc  <
num1=17
print(num1)
17
print("10진수 17 = %d"%(num1))
10진수 17 = 17
print("1진수 17의 8진수 = %o"%(num1))
1진수 17의 8진수 = 21
]
print("10진수 17의 8진수 = %o"%(num1))
10진수 17의 8진수 = 21
print("10진수 17의 16진수 = %x"%(num1))
10진수 17의 16진수 = 11
num2=97
print("%d %c" % (num2, num2))
97 a
float1= 1234.567
print(float1)
1234.567
print("기본 출력 %f" % (float))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print("기본 출력 %f" % (float))
TypeError: must be real number, not type
print("기본 출력 %f" %(float1))
기본 출력 1234.567000
print("지수표기법 %e" % (float1))
지수표기법 1.234567e+03
print("소수 둘째자리까지 %.2f" % (float))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print("소수 둘째자리까지 %.2f" % (float))
TypeError: must be real number, not type
print("소수 둘째자리까지 %.2f" % (float1))
소수 둘째자리까지 1234.57
txt1= "Hello"
txt2= "World!"
print("기본 출력\n%s %s"% (txt1, txt2))
기본 출력
Hello World!
print("7칸 출력\n %7s %7s"% (txt1, txt2))
7칸 출력
   Hello  World!\
print("7칸 출력\n%7s %7s"% (txt1, txt2))
   
7칸 출력
  Hello  World!
num1=17
print(num1)
17
print("10진수 17 = {0}".format(num1))
10진수 17 = 17
print("10진수 17의 8진수 = {0:o}".format(num1))
10진수 17의 8진수 = 21
print("10진수 17의 6진수 = {0:x}".format(num1))
10진수 17의 6진수 = 11
num2=98
print("{0} {1:c}".format(num2, num2))
98 b
print("{0} {0:c}".format(num2, num2))
98 b
float1=1234.567
print(float1)
1234.567
print("기본 출력 {0:f}".format(float1))
기본 출력 1234.567000
print("지수표기법 {0:e}".format(float1))
지수표기법 1.234567e+03
print("소수 둘째자리까지 {0:2f}".format(float1))
소수 둘째자리까지 1234.567000
print("소수 둘째자리까지 {0:.2f}".format(float1))
소수 둘째자리까지 1234.57
txt1="Hello"
txt2="World!"
print("기본 출력\n{0:s} {1:s}".format(txt1, txt2))
기본 출력
Hello World!
print("7칸 출력\n{0:7s} {1:7s}".format(txt1, txt2))
7칸 출력
Hello   World! 
print("7칸 출력\n{0:7s} {1:7s}".format(txt1, txt2))
7칸 출력
Hello   World! 
print("7칸 출력\n{0:7s} {1:7s}?".format(txt1, txt2))
7칸 출력
Hello   World! ?
r=5
pi=3.14
print("넓이는 r * r * pi = %d"%(r,pi))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print("넓이는 r * r * pi = %d"%(r,pi))
TypeError: not all arguments converted during string formatting
print("넓이는 r * r* pi = %d"%(r, r, pi))
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print("넓이는 r * r* pi = %d"%(r, r, pi))
TypeError: not all arguments converted during string formatting
r=5
pi=3.14
print("넓이는 r * r *pi"%(r, pi))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print("넓이는 r * r *pi"%(r, pi))
TypeError: not all arguments converted during string formatting
r=5
pi=3.14
print("넓이는 %d * %d * %f"%(r, r, pi))
넓이는 5 * 5 * 3.140000
r=5
pi=3.14
print("넓이는 %d * %d * %f"%(r, r, pi))
넓이는 5 * 5 * 3.140000
print("넓이는 %d * %d * %.2f"%(r, r, pi))
넓이는 5 * 5 * 3.14
5 * 5 * 3.14
78.5
print("넓이는 %d * %d * %.2f = %f"%(r, r, pi, r * r * pi))
넓이는 5 * 5 * 3.14 = 78.500000
print("넓이는 %d * %d * %.2f = %.1f"%(r, r, pi, r * r * pi))
넓이는 5 * 5 * 3.14 = 78.5
>>> r=5
>>> pi=3.14
>>> print("넓이는 {0:d} * {0:d} * {1:f} = {2:f}".format(r, r, pi, r * r * pi))
넓이는 5 * 5 * 5.000000 = 3.140000
>>> print("넓이는 {0:d} * {0:d} * {1:.2f} = {2:.1f}".format(r, pi, r * r * pi))
넓이는 5 * 5 * 3.14 = 78.5
>>> r=5
>>> pi=3.14
>>> r * r * pi
78.5
>>> print("넓이는 %f"%(r * r * pi))
넓이는 78.500000
>>> print("넓이는 %.1f"%(r * r * pi))
넓이는 78.5
>>> num1=17
>>> print(num1)
17
>>> print(f"10진수 17 = {num1}")
10진수 17 = 17
>>> print(f"10진수 17의 8진수 = {num1:o}")
10진수 17의 8진수 = 21
>>> print(f"10진수 17의 16진수 = {num1:x}")
10진수 17의 16진수 = 11
>>> num2 = 100
>>> print(f"{num2} {Num2:c})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"{num2} {num2:c}")
...       
100 d
>>> float1=1234.567
...       
>>> print(float1)
...       
1234.567
\
>>> print(f"기본출력 {float1:f}")
...       
기본출력 1234.567000
