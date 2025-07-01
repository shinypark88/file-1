Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
string = input("입력> ")
입력> 52273
type(string)
<class 'str'>
print("자료:", string)
자료: 52273
print("자료형:", type(string))
자료형: <class 'str'>
string = input("입력> ")
입력> True
print("자료:", string)
자료: True
string = input("입력> ")
입력> 300
print("입력+100:", string+100)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print("입력+100:", string+100)
TypeError: can only concatenate str (not "int") to str
string_a = input("입력A> ")
입력A> 273
int_a = int(string_a)
string_b = input("입력B> ")
입력B> 52
int_b = int(string_b)
print("문자열 자료:", string_a + string_b)
문자열 자료: 27352
print("숫자 자료:", int_a + int_b)
숫자 자료: 325
output_a = int("52")
output_b = int("52.273")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    output_b = int("52.273")
ValueError: invalid literal for int() with base 10: '52.273'
output_a = int("52")
output_b = float("52.273")
print(type(output_a), output_a)
<class 'int'> 52
print(type(output_b), output_b)
<class 'float'> 52.273
input_a = float(input("첫 번째 숫자> "))
첫 번째 숫자> 273
input_b = float(input("두 번째 숫자> "))
두 번째 숫자> 52
print("덧셈 결과:", input_a + input_b)
덧셈 결과: 325.0
print("뺄셈 결과:", input_a + input_b)
뺄셈 결과: 325.0
print("뺄셈 결과:", input_a - input_b)
뺄셈 결과: 221.0
print("곱셈 결과:", input_a * input_b)
곱셈 결과: 14196.0
print("나눗셈 결과:", input_a / input_b)
나눗셈 결과: 5.25
int("안녕하세요")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int("안녕하세요")
ValueError: invalid literal for int() with base 10: '안녕하세요'
float("안녕하세요")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    float("안녕하세요")
ValueError: could not convert string to float: '안녕하세요'
string_a = input("입력A> ")
입력A> 안녕하세요
int_a = int(string_a)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int_a = int(string_a)
ValueError: invalid literal for int() with base 10: '안녕하세요'
int("52.273")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int("52.273")
ValueError: invalid literal for int() with base 10: '52.273'
string_a = input("입력A> ")
입력A> 52.273
int_a = int(string_a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int_a = int(string_a)
ValueError: invalid literal for int() with base 10: '52.273'
output
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    output
NameError: name 'output' is not defined. Did you mean: 'output_a'?
output_a = str(52)
output_b = str(52.273)
print(type(output_a), output_a)
<class 'str'> 52
print(type(output_b), output_b)
<class 'str'> 52.273
raw_input = input("inch 단위의 숫자를 입력해주세요: ")
inch 단위의 숫자를 입력해주세요: 27
inch = int(raw_input)
cm = inch * 2.54
print(inch, "inch는 cm 단위로", cm, "cm입니다")
27 inch는 cm 단위로 68.58 cm입니다
"{".format(10)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    "{".format(10)
ValueError: Single '{' encountered in format string
"{}".format(10)
'10'
"{} {}".format(10, 20)
'10 20'
"{} {} {} {} {}".format(101, 202, 303, 404, 505)
'101 202 303 404 505'
string_a = "{}".format(10)
print(string_a)
10
print(type(string_a))
<class 'str'>
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하며 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)
print(format_a)
5000만 원
print(format_b)
파이썬 열공하며 첫 연봉 5000만 원 만들기
print(format_c)
3000 4000 5000
print(format_d)
1 문자열 True
"{} {}".format(1, 2, 3, 4, 5)
'1 2'
"{} {} {}".format(1, 2)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    "{} {} {}".format(1, 2)
IndexError: Replacement index 2 out of range for positional args tuple
output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)
print("# 기본")
# 기본
print(output_a)
52
print("# 특정 칸에 출력하기")
# 특정 칸에 출력하기
print(output_b)
   52
print(output_c)
        52
print("# 빈칸을 0으로 채우기")
# 빈칸을 0으로 채우기
print(output_d)
00052
print(output_e)
-0052
output_f = "{:+d}".format(52)
output_g = "{+d}".format(-52)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    output_g = "{+d}".format(-52)
KeyError: '+d'
output_g = "{:+d}".format(-52)
output_h = "{: d}".format(52)
output_i = "{: d}".format(-52)
print(output_f)
+52
print(output_g)
-52
print(output_h)
 52
print(output_i)
-52
output_h = "{:5d}'.format(52)
SyntaxError: unterminated string literal (detected at line 1)
output_h = "{:5d}".format(52)
output_i = "{:5d}".format(-52)
output_j = "{:=+5d}".format(52)
output_k = "{:=+5d}".format(-52)
output_l = "{:+05d}".format(52)
output_m = "{:+05d}".format(-52)
print(output_h)
   52
print(output_i)
  -52
print(output_j)
+  52
print(output_k)
-  52
print(output_l)
+0052
print(output_m)
-0052
output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)
output_c = "{:+15f}".format(52.273)
output_d = "{:015f}".format(52.273)
print(output_a)
52.273000
print(output_b)
      52.273000
print(output_c)
     +52.273000
print(output_d)
00000052.273000
output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format952.273)
SyntaxError: unmatched ')'
output_c = "{:15.1f}".format(52.273)
print(output_a)
         52.273
print(output_b)
          52.27
print(output_c)
           52.3
output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_a)
52.0
print(output_b)
52
a = "Hello Python Programming...!"
a.upper()
'HELLO PYTHON PROGRAMMING...!'
a.lower()
'hello python programming...!'
input_a = """
안녕하세요
문자열의 함수를 알아봅시다
"""
print(input_a)

안녕하세요
문자열의 함수를 알아봅시다

print(input_a.strip())
안녕하세요
문자열의 함수를 알아봅시다
print("TrainA10".isalnum())
True
print("10".isdigit())
True
output_a = "안녕안녕하세요".find("안녕")
print(output_a)
0
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)
2
print("안녕" in "안녕하세요")
True
print("잘자" in "안녕하세요")
False
a = "10 20 30 40 50".split(" ")
print(a)
['10', '20', '30', '40', '50']
"3+4="+str(3+4)
'3+4=7'
"3+4 = {}".format(3+4)
'3+4 = 7'
"[}".format(10)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    "[}".format(10)
ValueError: Single '}' encountered in format string
"{}".format(10)
'10'
f'{10}'
'10'
f"3+4={3+4}"
'3+4=7'
f"""1+2 = {1+2}
2+3={2+3}
3+4={3+4}"""
'1+2 = 3\n2+3=5\n3+4=7'
name = "구름"
age = 7
>>> """#문자열이 너무 긴 경우
... 문자열이 너무 긴 상황에서
... 데이터 {}을/를 출력해야 하는 경우가 있습니다.
... 
... 이때 f-문자열을 사용하면
... 어떤 위치에 어떤 데이터 {}가 출력되는지 확인하기 위해서
... 문자열 전체를 읽어야 하는 경우가 있습니다.
... 이러한 경우 format() 함수를 사용한느 것이 편리합니다.
... 문자열이 아무리 길어도 다음 줄만 보면
... 어떤 데이터를 출력하는지 쉽게 알 수 있습니다.
... """.format(name, age)
'#문자열이 너무 긴 경우\n문자열이 너무 긴 상황에서\n데이터 구름을/를 출력해야 하는 경우가 있습니다.\n\n이때 f-문자열을 사용하면\n어떤 위치에 어떤 데이터 7가 출력되는지 확인하기 위해서\n문자열 전체를 읽어야 하는 경우가 있습니다.\n이러한 경우 format() 함수를 사용한느 것이 편리합니다.\n문자열이 아무리 길어도 다음 줄만 보면\n어떤 데이터를 출력하는지 쉽게 알 수 있습니다.\n'
>>> ['별', 2, 'M', '서울특별시 강서구', 'Y']
['별', 2, 'M', '서울특별시 강서구', 'Y']
>>> data = ['별', 2, 'M', '서울특별시 강서구', 'Y']
>>> f"""이름: {data[0]}
...     나이: {data[1]}
...     지역: {data[2]}
...     성별: {data[3]}
...     중성화 여부: {data[4]}"""
'이름: 별\n    나이: 2\n    지역: M\n    성별: 서울특별시 강서구\n    중성화 여부: Y'
>>> data = ['별', 2, 'M', '서울특별시 강서구', 'Y']
>>> """이름: {}
...    나이: {}
...    성별: {}
...    지역: {}
...    중성화 여부: {}""".format(*data)
'이름: 별\n   나이: 2\n   성별: M\n   지역: 서울특별시 강서구\n   중성화 여부: Y'
