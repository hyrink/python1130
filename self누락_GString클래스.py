# 전역변수
str = "Not Class Member"

# 클래스 생성
class GString:
    def __init__(self):
        # 인스턴스 멤버변수 초기화
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        # 버그발생 (self. 누락됨)
        print(self.str)

# 인스턴스(복사본) 생성
g = GString()
g.set("First Message")
g.print()
