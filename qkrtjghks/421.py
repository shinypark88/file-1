#1) 2

#2)math 수학과 관련된 함수를 불러온다
#   datetime 날짜와 관련된 함수를 불러온다
#   OS 운영체제와 관련된 동작을 수행하는 함수
# random 임의의 숫자들을 불러온다 

import

import os

def read_folder(path):
    output = os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_folder(path+"/"+item)
        else:
            print("파일:",item)
read_folder(".")
