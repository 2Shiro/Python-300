# https://wikidocs.net/7031

#121
# 문자.islower() 은 소문자일때 True, 대문자일때 False를 반환한다
"""
a = input("문자 한 개를 입력해주세요 : ")
if a.islower():
    print(a.upper())
else:
    print(a.lower())
"""

#122
"""
a = int(input("점수를 입력해주세요 : "))
if 80 < a <= 100:
    print("grade is A")
elif 60 < a <= 80:
    print("grade is B")
elif 40 < a <= 60:
    print("grade is C")
elif 20 < a <= 40:
    print("grade is D")
elif 0 <= a <= 20:
    print("grade is E")
else:
    print("0 ~ 100 범위내에서만 입력해주세요")
"""

#123
# b, c = a.split()을 사용하면 2개로 나누어 바인딩할 수 있고 그 이상도 가능하다.
"""
w = {"달러" : 1167, "엔" : 1.096, "유로" : 1268, "위안" : 171}
a = input("금액 통화명(ex> 100 달러) 을 입력해주세요 : ")
num, currency = a.split(" ")
print(float(num) * w[currency], "원")
"""

#124
"""
a = int(input("input number1 : "))
b = int(input("input number2 : "))
c = int(input("input number3 : "))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
"""

#125
"""
print("예시) 010-0000-0000")
a = input("휴대전화 번호 입력 : ")
t = a[:3]
if (t == "011"):
    print("당신은 SKT 사용자입니다.")
elif (t == "016"):
    print("당신은 KT 사용자입니다.")
elif (t == "019"):
    print("당신은 LGU 사용자입니다.")
else:
    print("당신은 알 수 없는 사용자입니다.")
"""
# 다른 방법
"""
number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")
"""

#126
"""
a = input("우편번호: ")
u = a[:3]
if (u == "010" or u == "011" or u == "012"):
    print("강북구")
elif (u == "013" or u == "014" or u == "015"):
    print("도봉구")
elif (u == "016" or u == "017" or u == "018" or u == "019"):
    print("노원구")
else:
    print("우편번호를 확인해주세요")
"""
# 다른 방법 : if문에서 변수 in 리스트 사용
"""
우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")
"""

#127
"""
a = input("주민등록번호: ")
b = a.split("-")[1]
if b[0] == "1" or b[0] == "3":
    print("남자")
elif b[0] == "2" or b[0] == "4":
    print("여자")
else:
    print("주민번호를 확인해주세요.")
"""

#128
"""
a = input("주민등록번호: ")
b = (a.split("-")[1])
if 0 <= int(b[1:3]) <= 8:
    print("서울")
else:
    print("서울이 아닙니다.")
"""

#129
"""
a = input("주민등록번호: ")
cal1 = ((int(a[0])*2 + int(a[1])*3 + int(a[2])*4 + int(a[3])*5 + int(a[4])*6 + int(a[5])*7
        + int(a[7])*8 + int(a[8])*9 + int(a[9])*2 + int(a[10])*3 + int(a[11])*4 + int(a[12])*5) % 11)
cal2 = 11 - cal1
if cal2 == int(a[13]):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
"""

#130
"""
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

start = float(btc["opening_price"])
between = float(btc["max_price"]) - float(btc["min_price"])
max = float(btc["max_price"])

if (start + between) > max:
    print("상승장")
else:
    print("하락장")
"""