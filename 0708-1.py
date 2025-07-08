"""dict_a = {
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
    "director": ["안소니 루소", "조 루소"],
    "cast": ["아이언맨", "타노스", "토르", "닥터스트레인지", "헐크"]
    }

dict_key = {
    name: "70 건조 망고",
    type: "당절임"
    }

name = "이름"
dict_key = {
    name: "70 건조 망고",
    type: "당절임"
    }

dictionary = {
    "name": "70 건조 망고",
    "type":"당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
    }
dictionary["price"] = 5000

key = input(">접근하고자 하는 키: ")
    
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아확산나트륨", "치자황색소"],
    "origin": "필리핀"
    }
    
value = dictionary.get("name")
    
print("값:", value)

if value == None:
    print("존재하지 않는 키에 접근하였습니다")"""

dictionary = {
        "name": "7D 건조 망고",
        "type": "당절임",
        "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
        "origin": "필리핀"
        }
for key in dictionary:
        print(key, ":", dictionary[key])


    


