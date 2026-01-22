##class Student:
##    def __init__(self,name,korean,math,english,science):
##        self.name = name
##        self.korean = korean
##        self.math = math
##        self.english = english
##        self.science = science
##    def get_sum(self):
##        return self.korean+self.math+\
##               self.english+self.science
##    def get_average(self):
##        return self.get_sum()/4\
##    def __==__(self,value):
##        return self.get_average()==value
##    def __!=__(self,value):
##        return self.get_average()!=value
##    def __>__(self,value):
##        return self.get_average()>value
##    def __>=__(self,value):
##        return self.get_average()>=value
##    def __<__(self,value):
##        return self.get_average()<value
##    def __<=__(self,value):
##        return self.get_average()<=value

##class Student:
##    def __init__(self,name,score):
##        self.name = name
##        self.score = score
##
##class StudentList:
##    def __init__(self):
##        self.students = []
##    def append(self,student):
##        self.students.append(student)
##    def get_average(self):
##        L=len(self.students)
##        total=0
##        for i in range(0,L):
##            total+=self.students[i].score
##        average = total / L
##        return average
##    def get_first_by_score(self):
##        scoreList = []
##        L=len(self.students)
##        for i in range(0,L):
##            scoreList.append(self.students[i].score)
##        M=scoreList.index(max(scoreList))
##        return self.students[M]
##    def get_last_by_score(self):
##        scoreList = []
##        L=len(self.students)
##        for i in range(0,L):
##            scoreList.append(self.students[i].score)
##        m=scoreList.index(min(scoreList))
##        return self.students[m]
##        
##
##students = StudentList()
##students.append(Student("구름",100))
##students.append(Student("별",49))
##students.append(Student("초코",81))
##students.append(Student("아지",90))
##
##print(f"학급의 평균 점수는 {students.get_average()}입니다.")
##print(f"가장 성적이 높은 학생은 {students.get_first_by_score().name}입니다.")
##print(f"가장 성적이 낮은 학생은 {students.get_last_by_score().name}입니다.")
    
class Stack:
    def __init__(self):
        self.list = []
    def push(self,item):
        self.list.append(item)
    def pop(self):
        x=self.list[-1]
        del self.list[-1]
        return x

    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
