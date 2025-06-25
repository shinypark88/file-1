Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print('따옴표는 "역할'이 같아요")
      
SyntaxError: unterminated string literal (detected at line 1)
apple = "사과"
      
print(apple, 1, "상자")
      
사과 1 상자
apple = "사과"
      
print(apple, 1, "상자", sep = "++")
      
사과++1++상자

============ RESTART: C:/Users/sw_306/Desktop/수강생706/박서환/0625(5).py ============
이샘
코딩
학원

============ RESTART: C:/Users/sw_306/Desktop/수강생706/박서환/0625(6).py ============
이샘코딩학원!
print(type(myScore))
      
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(type(myScore))
NameError: name 'myScore' is not defined
myScore = 'B'
      
print(type(myScore))
      
<class 'str'>
\

============ RESTART: C:/Users/sw_306/Desktop/수강생706/박서환/0625(7).py ============
10 <class 'int'>
>>> num2 = 3.14
...       
>>> print(num2, type(num2))
...       
3.14 <class 'float'>
>>> m_str = "안녕하세요"
...       
>>> print(m_str, type(m_str))
...       
안녕하세요 <class 'str'>
>>> print(1+1, type(1+1))
...       
2 <class 'int'>
>>> print(0.3+2.04, type(0.3+2.04))
...       
2.34\ <class 'float'>
>>> print(1+2.3, type(1+2.3))
...       
3.3 <class 'float'>
>>> print("이샘코딩전문학원")
...       
이샘코딩전문학원
>>> print("이샘코딩학원")
...       
이샘코딩학원
>>> print
...       
<built-in function print>
>>> print(1,2,3,sep="+", end="=")
...       
1+2+3=
>>> print(1,2,3,sep="+", end="=6")
...       
1+2+3=6
>>> print(\"이샘코딩학원\")
...       
SyntaxError: unexpected character after line continuation character
>>> print('"이샘코딩학원"')
...       
"이샘코딩학원"
