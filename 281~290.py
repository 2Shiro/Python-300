# https://wikidocs.net/7041

#281
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

car = 차(2, 1000)
print(car.바퀴)
print(car.가격)
"""

#282
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차:
    pass
"""

#283
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

bicycle = 자전차(2, 100)
print(bicycle.가격)
"""

#284
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
# super()는 상속 관계에서 상속의 대상인 부모 클래스를 호출하는 함수
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

bicycle = 자전차(2, 100, "시마노")
print(bicycle.구동계)
print(bicycle.바퀴)
"""

#285
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)


car = 자동차(4, 1000)
car.정보()
"""

#286
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()
"""

#287
# 부모 클래스 함수에 없는 값을 출력할려면 자식 클래스 함수에 추가하면 된다
"""
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

    def 정보(self):
        super().정보()
        print("구동계 ", self.구동계)

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()
"""

#288
# 자식호출
"""
class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")

나 = 자식()
나.호출()
"""

#289
# 자식생성
"""
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")

나 = 자식()
"""

#290
"""
자식생성
부모생성
"""
"""
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()
"""