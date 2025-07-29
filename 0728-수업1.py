##dict = {"coding":"코딩","soccer":"축구","loop":"반복문","condition":"조건"}
##print("영어 단어 뜻 맞추기")
##for key in dict.keys():
##    text = input(f"{key}: ")
##    if text == dict[key]:
##        print("정답입니다!")
##    elif text != dict[key]:
##        print("틀렸습니다.")
##        break

##dict = {}
##dict["leesam0044"] = "1234567"
##dict["lee"] = "11223344"
##text=input("아이디: ")
##if text in dict.keys():
##    text2 = input("패스워드: ")
##    if text2 == dict[text]:
##        print("로그인 성공!")
##    else:
##        print("로그인 실패!")
##else:
##    print("로그인 실패!")

##registeration = {}

##while True:
##    choice = input('1.회원가입, 2.로그인, 3.종료 중 입력 : ')
##    choice = int(choice)
##
##    if choice == 1:
##        print('회원가입을 시작합니다.')
##        reg_id = input('아이디 입력: ')
##        reg_pw = input('패스워드 입력: ')
##        reg_pw2 = input('패스워드 다시 입력: ')
##
##        if reg_id in registeration.keys():
##            print('아이디 중복됨, 다른아이디로 회원가입하세요')
##            continue
##
##        registeration[reg_id] = reg_pw
##        print('회원가입 성공')
##    elif choice == 2:
##        print(';로그인을 시작합니다.')
##        login_id = input('아이디입력: ')
##        login_pw = input('패스워드 입력: ')
##
##        if login_id in registeration.keys():
##            if registeration[login_id] == login_pw:
##                print('로그인 성공')
##            else:
##                print('패스워드 틀림')
##        else:
##            print('아이디 없음')
##    elif choice == 3:
##        print('종료하겠습니다.')

##vocabulary = {}
##vocabulary['abstract'] = '추상화'
##vocabulary['variable'] = '변수'
##vocabulary['fuction'] = '함수'
##vocabulary['loop'] = '반복문'
##
##for key, value in vacabulary.items():
##    word = input(f'{key}의 뜻은?: ')
##
##    if word == value:
##        print('정답입니다')
##    else:
##        print('틀렸습니다ㅜㅜ')
##    print()

##import random
##vocabulary = {}
##vocabulary['abstract'] = '추상화'
##vocabulary['variable'] = '변수'
##vocabulary['fuction'] = '함수'
##vocabulary['loop'] = '반복문'
##
##vocab_shuffled = list(vocabulary.keys())
##random.shuffle(vocab_shuffled)
##for key in vocab_shuffled:
##    word = input(f'{key]의 뜻은? : ')
##
##    if word == vocabulary[key]:
##        print('정답입니다')
##    else:
##        print('틀렸습니다ㅜㅜ')
##    print()

print("continue는 다시 위로 가기 (while True로)")

        
