import random
class RockScisscorPaper:
    def __init__(self,me,other):
        self.me=me
        self.other=other
    def get_result(self):
        win=[[rock,scissor],[paper,rock],[scissor,paper]]
        if self.me==self.other:
            return f"(무승부)"
        elif [self.me,self.other] in win:
            return f"(승리)"
        else:
            return f"(패배)"
    def random_create(self):
        myList = [rock,scicsor,paper]
        self.me = myList[random.randint(0,2)]
        self.other = myList[random.randint(0,2)]
