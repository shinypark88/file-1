Python 3.13.4 (tags/v3.13.4:8a526ec, Jun  3 2025, 17:46:04) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
str1= "Hello string!"
str2= "안녕 문자열!"
str3= """안녕 변수!
안녕 문자열!
안녕 파이썽!"""
str1 = "Hello String!"
str1[0] = "안녕 문자열"
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str1[0] = "안녕 문자열"
TypeError: 'str' object does not support item assignment
str1 = "안녕 문자열"
str1 = "파이썬"
str2 = "참 쉽다"
str3 = str1 + ", " +str2 +"!!"
print(str3)
파이썬, 참 쉽다!!
str1 = "파이썬 Lvup!"
str2 = str1 * 3
print(str2)
파이썬 Lvup!파이썬 Lvup!파이썬 Lvup!
nut1 = "밤양갱"
nut2 = "달디단 밤양갱"
nut3 = "달디달고 달디달고,
SyntaxError: unterminated string literal (detected at line 1)
달디단 밤양갱 밤양갱
SyntaxError: invalid syntax
nut3 = """달디달고 달디달고,
달디단 밤양갱 밤양갱
내가 먹고 싶었던 건,
달디단, 밤양갱, 밤양갱이야"""
sweat = "달디"
sweat2 = sweat * 10
number = 255
message = sweat2 + " " + "단 밤양갱" + str(number) + "개"
print(message)
달디달디달디달디달디달디달디달디달디달디 단 밤양갱255개
line = "=" * 20
header = "밤양갱 대박 세일"
footer = "놓치지 마세요!"
message = line + "\n" + header + "\n" + line + "\n" + footer + "\n" + line
print(message)
====================
밤양갱 대박 세일
====================
놓치지 마세요!
====================
print(str1[0])
파
print(str1[4])
L
str1 ="파이썬 문자열을 골라보자"
print(str1[0])
파
print(str1[4])
문
print(str1[9])
골
print(str1[2])
썬
print(str1[6])
열
print(str1[12])
자
str2 = "이샘코딩학원"
print(str2[1:3])
샘코
print(str2[2:])
코딩학원
print(str2[:2])
이샘
print(str2[::2])
이코학
print(str2[::-2])
원딩샘
print(word[0])
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(word[0])
NameError: name 'word' is not defined. Did you mean: 'ord'?
word = "문자열과 인덱스"
print(word[0])
문
print(word[3])
과
print(word[5])
인
print(word[-1])
스
snack = "떡볶이 순대 튀김"
setmenu = snack[0] +snack[4] + snack[7]
print(setmenu)
떡순튀
word = "부분만 바꾸려고 하면 에러가 나요"
ㅔ갸ㅜㅅ(잭ㅇ)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    ㅔ갸ㅜㅅ(잭ㅇ)
NameError: name 'ᅦ갸ᅮᄉ' is not defined
>>> print(word)
부분만 바꾸려고 하면 에러가 나요
>>> word[0] = "수"
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    word[0] = "수"
TypeError: 'str' object does not support item assignment
>>> word = "새로 만들어 덮어쓰기는 가능"
>>> print(word)
새로 만들어 덮어쓰기는 가능
>>> word = "슬라이싱으로 다양하게 문자를 잘라봅시다"
>>> print(word[0:4])
슬라이싱
>>> print(word[7:9])
다양
>>> print(word[5:])
로 다양하게 문자를 잘라봅시다
>>> print(word[:12])
슬라이싱으로 다양하게 
>>> print(word[::3])
슬싱 하문 봅
>>> print(word[::-3])
다라를 양로이
>>> song = "록도닳 고르마 이산두백 과물해동"
>>> reverse = song[::-1]
>>> print(reverse)
동해물과 백두산이 마르고 닳도록
>>> song = "동해물과 백두산이 마르고 닳도록"
>>> part_song = song[:4]
>>> print(part_song)
동해물과
>>> part_song = song[5:13]
>>> print(part_song)
백두산이 마르고
>>> part_song = song[14:]
>>> print(part_song)
닳도록
