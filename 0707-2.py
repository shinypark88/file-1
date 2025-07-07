Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
list_a = [1, 2, 3]
print("# 리스트 뒤에 요소 추가하기")
# 리스트 뒤에 요소 추가하기
list_a.append(4)
list_a.append(5)
print(list_a)
[1, 2, 3, 4, 5]
print()

print("# 리스트 중간에 추가하기")
# 리스트 중간에 추가하기
list_a.insert(0, 10)
print(list_a)
[10, 1, 2, 3, 4, 5]
list_a = [1, 2, 3]
list_a.append(4)
list_a.append(5)
list_a.insert(0, 10)
list_a.extend([4, 5, 6])
print(list_a)
[10, 1, 2, 3, 4, 5, 4, 5, 6]
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a +list_b
[1, 2, 3, 4, 5, 6]
list_a
[1, 2, 3]
list_b
[4, 5, 6]
list_a.extend(list_b)
list_a
[1, 2, 3, 4, 5, 6]
list_b
[4, 5, 6]
list_a = [0, 1, 2, 3, 4, 5]
print("# 리스느트이 요소 하나 제거하기")
# 리스느트이 요소 하나 제거하기
del list_a[1]
print("del list_a[1]:", list_a)
del list_a[1]: [0, 2, 3, 4, 5]
list_a.pop(2)
3
print("pop(2):", list_a)
pop(2): [0, 2, 4, 5]
list_a = [0,1,2,3,4,5]
del list_a[1]
print(list_a)
[0, 2, 3, 4, 5]
list_a = [0,1,2,3,4,5]
list_a.pop(2)
2
print(list_a)
[0, 1, 3, 4, 5]
list_b = [0,1,2,3,4,5,6]
del list_b[3:6]
list_b
[0, 1, 2, 6]
list_c = [0,1,2,3,4,5,6]
del list_c[:3]
list_c
[3, 4, 5, 6]
list_d = [0,1,2,3,4,5,6]
del list_d[3:]
list_d
[0, 1, 2]
list_c = [1,2,1,2]
list_c.remove(2)
list_c
[1, 1, 2]
list_d = [0,1,2,3,4,5]
list_d.clear()
list_d
[]
list_e = [52, 273, 103, 32, 257, 1, 7]
list_e.sort()
list_e
[1, 7, 32, 52, 103, 257, 273]
list_e.sort(reverse=True)
list_e
[273, 257, 103, 52, 32, 7, 1]
list_a = [273, 32, 103, 57, 22]
273 in list_a
True
99 in list_a
False
100 in list_a
False
52 in list_a
False
list_a = [273, 32, 103, 57, 52]
52 in list_a
True
273 not in list_a
False
99 not in list_a
True
100 not in list_a
True
52 not in list_a
False
not 273 in list_a
False
for i in range(100):
    print("출력")

출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
출력
array = [273, 32, 103, 57, 52]
for element in array:
    print(element)

    
273
32
103
57
52
for character in "안녕하세요":
    print("-", character)

    
- 안
- 녕
- 하
- 세
- 요
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7,],
    [8, 9]
    ]



list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7,],
    [8, 9]
]


for items in list_of_list:
    print(items)

    
[1, 2, 3]
[4, 5, 6, 7]
[8, 9]
for items in list_of_list:
    for item in items:
        print(items)

        
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[4, 5, 6, 7]
[4, 5, 6, 7]
[4, 5, 6, 7]
[4, 5, 6, 7]
[8, 9]
[8, 9]
>>> a = [1, 2, 3, 4]
>>> print(*a)
1 2 3 4
>>> a=[1,2,3,4]
>>> b=[*a,*a]
>>> b
[1, 2, 3, 4, 1, 2, 3, 4]
>>> a=[1,2,3,4]
>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]
>>> b = [1,2,3,4]
>>> c = [*b,5]
>>> b
[1, 2, 3, 4]
>>> b
[1, 2, 3, 4]
>>> c
[1, 2, 3, 4, 5]
