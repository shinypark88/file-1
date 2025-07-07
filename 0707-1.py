array = [273, 32, 103, "문자열", True, False]
print(array)
[273, 32, 103, '문자열', True, False]
[1,2,3,4]
[1, 2, 3, 4]
["안","녕","하","세","요"]
['안', '녕', '하', '세', '요']
[273, 32, 103, "문자열", True, False]
[273, 32, 103, '문자열', True, False]
list_a = [273, 32, 103, "문자열", True, False]
list_a[0]
273
list_a[1]
32
list_a[2]
103
list_a[3]
'문자열'
list_a[4]
True
list_a[5]
False
list_a[1:3]
[32, 103]
list_a[0] = "변경"
list_a
['변경', 32, 103, '문자열', True, False]
list_a[-1]
False
list_a[-2]
True
list_a[-3]
'문자열'
list_a[3]
'문자열'
list_a[3][0]
'문'
list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9,]]
list_a[1]
[4, 5, 6]
list_a[1][1]
5
list_a = [273, 32, 103]
list_a[3]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list_a[3]
IndexError: list index out of range
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print("# 리스트")
# 리스트
print("list_a =", list_a)
list_a = [1, 2, 3]
print("list_b =", list_b)
list_b = [4, 5, 6]
print()

print("# 리스트 기본 연산자")
# 리스트 기본 연산자
print("list_a +list_b =", list_a + list_b)
list_a +list_b = [1, 2, 3, 4, 5, 6]
print("list_a + 3 =", list_a * 3)
list_a + 3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print()

print("# 길이 구하기")
# 길이 구하기
print("len(list_a) =", len(list_a))
len(list_a) = 3
