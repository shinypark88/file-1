num1 = str(input("첫번째 숫자를 입력하세요: "))
num2 = str(input("두번째 숫자를 입력하세요: "))
num3 = str(input("세번째 숫자를 입력하세요: "))
output = int(num1)+int(num2)+int(num3)
print(f"총합은 {output}")

upper = str(input("윗변을 입력하세요: "))
lower = str(input("밑변을 입력하세요: "))
height = str(input("높이를 입력하세요: "))
area = (int(upper)+int(lower)) * int(height) / 2
print(f"사다리꼴의 넓이는 {area}")

id = str(input("아이디: "))
pw = str(input("비밀번호: "))
message = '당신의 아이디는 '+'"'+id+'"'+'이며, '+'비밀번호는'+'"'+str(pw)+'"'+"입니다."
print(message)

r = str(input("반지름을 입력하세요: "))
pi=3.14
area = int(r) ** 2 * pi
length = int(r) * 2 * pi
print(f"원의 넓이는 {area}")
print(f"원의 둘레길이는 {length:.1f}")
