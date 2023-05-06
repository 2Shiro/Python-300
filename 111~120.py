# https://wikidocs.net/7030

#111
"""
a = input("출력할 문자열을 입력해주세요 : ")
print(a + a)
"""
# 다른 방법
"""
a = input("출력할 문자열을 입력해주세요 : ")
print(a * 2)
"""

#112
"""
a = int(input("숫자를 입력하세요 : "))
print(a + 10)
"""

#113
# 나머지 연산자 %
"""
a = int(input("숫자를 입력해주세요 : "))
if(a%2 == 0):
    print("짝수입니다.")
else:
    print("홀수입니다.")
"""

#114
"""
a = int(input("숫자를 입력해주세요 : "))
num = a + 20
if(num <= 255):
    print(num)
else:
    print(255)
"""

#115
"""
a = int(input("숫자를 입력해주세요 : "))
num = a - 20
if((num) < 0):
    print(0)
elif(num > 255):
    print(255)
else:
    print(num)
"""
    
#116
"""
a = input("현재시간 : ")
t = a[-2:]
if(t == "00"):
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")
"""

#117
# 리스트에 있는지 없는지 확인할려면 in 또는 not in 을 사용한다
"""
fruit = ["사과", "포도", "홍시"]
a = input("좋아하는 과일은? ")
if a in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")
"""

#118
"""
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
a = input("투자 종목은 무엇인가요? ")
if a in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")
"""

#119
"""
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
a = input("제가좋아하는계절은: ")
if a in fruit.keys():
    print("정답입니다.")
else:
    print("오답입니다.")
"""

#120
"""
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
a = input("제가좋아하는과일은: ")
if a in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
"""