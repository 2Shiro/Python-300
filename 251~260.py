# https://wikidocs.net/7035

#251
"""
클래스 : 객체를 만들어 내기 위한 설계도 혹은 틀
객체 : 클래스에 선언된 모양 그대로 생성된 실체
인스턴스 : 설계도를 바탕으로 소프트웨어 세계에 구현된 구체적인 실체
"""

#252
# 클래스 정의
"""
class Human:
    pass
"""

#253
# 인스턴스 생성
"""
class Human:
    pass
areum = Human()
"""

#254
# 클래스 생성자
"""
class Human:
    def __init__(self):
        print("응애응애")

areum = Human()
"""

"""
#255
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")

print(areum.name)

#256
print(areum.age)
print(areum.sex)
"""

#257
"""
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

areum = Human("아름", 25, "여자")   # 객체 생성
areum.who()
"""

#258
"""
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("불명", "미상", "모름")
areum.who()

areum.setInfo("아름", 25, "여자")   # setInfo()는 값을 다시 설정
areum.who()
"""

#259
"""
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
del(areum)
"""

#260
# print함수에는 인자가 없는데 print(mystock)을 불러오기 때문에 오류가 발생한다
"""
class OMG:
    def print():   # 그렇기에 self를 사용하는 것이다
        print("Oh my god")

mystock = OMG()
mystock.print()
"""