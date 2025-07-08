Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
dict_a = {
    "name": "어벤져스 엔드게임",
    "type": "히어로 무비"
    }

dict_a
{'name': '어벤져스 엔드게임', 'type': '히어로 무비'}
dict_a["name"]
'어벤져스 엔드게임'
dict_a["type"]
'히어로 무비'
dict_b = {
    "director": ["안소니 루소", "조 루소"]
    "cast": ["아이언맨", "타노스", "토르", "닥터스트레인지", "헐크"]
    
SyntaxError: '{' was never closed
dict_b = {
    "director": ["안소니 루소", "조 루소"]
    "cast": ["아이언맨", "타노스", "토르", "닥터스트레인지", "헐크"]
    
SyntaxError: '{' was never closed

============= RESTART: /Users/seohwanpark/Desktop/python/0708-1.py =============
dict_b
    
{'director': ['안소니 루소', '조 루소'], 'cast': ['아이언맨', '타노스', '토르', '닥터스트레인지', '헐크']}
dict_b["director"]
    
['안소니 루소', '조 루소']
dictionary = {
    "name": "70 건조 망고",
    "type":"당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
    }
    

print("name:", dictionary["name"])
    
name: 70 건조 망고
print("type:", dictionary["type"])
    
type: 당절임
print("ingredient:", dictionary["ingredient"])
    
ingredient: ['망고', '설탕', '메타중아황산나트륨', '치자황색소']
print("origin", dictionary["origin"])
    
origin 필리핀
print("origin:", dictionary["origin"])
    
origin: 필리핀
print()
    


dictionary["name"] = "80 건조 망고"
    
print("name:", dictionary["name"])
    
name: 80 건조 망고
dictionary["ingredient"]
    
['망고', '설탕', '메타중아황산나트륨', '치자황색소']
dictionary["ingredient"][1]
    
'설탕'
dict_key = {
    name: "70 건조 망고",
    type: "당절임"
    }
    
Traceback (most recent call last):
  File "<pyshell#36>", line 2, in <module>
    name: "70 건조 망고",
NameError: name 'name' is not defined

============= RESTART: /Users/seohwanpark/Desktop/python/0708-1.py =============
dict_key
    
{'이름': '70 건조 망고', <class 'type'>: '당절임'}

============= RESTART: /Users/seohwanpark/Desktop/python/0708-1.py =============
Traceback (most recent call last):
  File "/Users/seohwanpark/Desktop/python/0708-1.py", line 29, in <module>
    dictionary["price"] = 5000
NameError: name 'dictionary' is not defined

============= RESTART: /Users/seohwanpark/Desktop/python/0708-1.py =============
dictionarydictionary = {
    "name": "70 건조 망고",
    "type":"당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
    }
    
dictionary
    
{'name': '70 건조 망고', 'type': '당절임', 'ingredient': ['망고', '설탕', '메타중아황산나트륨', '치자황색소'], 'origin': '필리핀', 'price': 5000}
dictionary["name"] = "80 건조 파인애플"
    
dictionary
    
{'name': '80 건조 파인애플', 'type': '당절임', 'ingredient': ['망고', '설탕', '메타중아황산나트륨', '치자황색소'], 'origin': '필리핀', 'price': 5000}
del dictionary["ingredient"]
    
dictionary
    
{'name': '80 건조 파인애플', 'type': '당절임', 'origin': '필리핀', 'price': 5000}
dictionary = {}
    
print("요소 추가 이전:", dictionary())
    
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print("요소 추가 이전:", dictionary())
TypeError: 'dict' object is not callable
print("요소 추가 이전:", dictionary)
    
요소 추가 이전: {}
dictionary["name"] = "새로운 이름"
    
dictionary["head"] = "새로운 정신"
    
dictionary["body"] = "새로운 몸"
    
print("요소 추가 이후:", dictionary)
    
요소 추가 이후: {'name': '새로운 이름', 'head': '새로운 정신', 'body': '새로운 몸'}
dictionary = {
    "name": "70 건조 망고",
    "type": "당절임"
    }
    
print("요소 제거 이전:", dictionary)
    
요소 제거 이전: {'name': '70 건조 망고', 'type': '당절임'}
del dictionary["name"]
    
del dictionary["type"]
    
print("요소 제거 이후:", dictionary)
    
요소 제거 이후: {}
dictionary = {}
    
dictionary["Key"]
    
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    dictionary["Key"]
KeyError: 'Key'
del dictionary["Key"]
    
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    del dictionary["Key"]
KeyError: 'Key'
dictionary = {
    "name": "70 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
    }
    
key = input(">접근하고자 하는 키: ")
    
>접근하고자 하는 키: name

============= RESTART: /Users/seohwanpark/Desktop/python/0708-1.py =============
>접근하고자 하는 키: name
Traceback (most recent call last):
  File "/Users/seohwanpark/Desktop/python/0708-1.py", line 39, in <module>
    if key in dictionary:
NameError: name 'dictionary' is not defined

============= RESTART: /Users/seohwanpark/Desktop/python/0708-1.py =============
>접근하고자 하는 키: name
70 건조 망고

============= RESTART: /Users/seohwanpark/Desktop/python/0708-1.py =============
>접근하고자 하는 키: ㅇㅂㅇ
존재하지 않는 키에 접근하고 있습니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아확산나트륨", "치자황색소"],
    "origin": "필리핀"
    }
    
value = dictionary.get("존재하지 않는 키")
    

============= RESTART: /Users/seohwanpark/Desktop/python/0708-1.py =============
값: None
존재하지 않는 키에 접근하였습니다

============= RESTART: /Users/seohwanpark/Desktop/python/0708-1.py =============
값: 7D 건조 망고
>>> 
============= RESTART: /Users/seohwanpark/Desktop/python/0708-1.py =============
name : 7D 건조 망고
type : 당절임
ingredient : ['망고', '설탕', '메타중아황산나트륨', '치자황색소']
origin : 필리핀
>>> a=range(5)
...     
>>> a
...     
range(0, 5)
>>> list(range(5))
...     
[0, 1, 2, 3, 4]
>>> list(range(0, 5))
...     
[0, 1, 2, 3, 4]
>>> list(range(5, 10))
...     
[5, 6, 7, 8, 9]
>>> list(range(0, 10, 2))
...     
[0, 2, 4, 6, 8]
>>> list(range(0, 10, 3))
...     
[0, 3, 6, 9]
