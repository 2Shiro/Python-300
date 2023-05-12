# https://wikidocs.net/7044

#291
# 경로는 / 나 \\로 바꿔줘야한다
"""
f = open("C:/Users/Shiro/Desktop/Job/Python/Python-300/buying1.txt", mode="wt", encoding="utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420")
f.close()
"""

#292
"""
f = open("C:/Users/Shiro/Desktop/Job/Python/Python-300/buying2.txt", mode="wt", encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER")
f.close()
"""

#293
# mode="wt"는 "w"로 생략가능하고 "wb"는 오디오 같은 미디어일때 사용한다
# encoding="cp949"는 csv 파일일때 사용한다
# 원래는 한줄씩 띄워서 적용되기때문에 newline = '' 해주면 바로 붙여서 쓰기가 가능하다
"""
import csv

f = open("C:/Users/Shiro/Desktop/Job/Python/Python-300/buying.csv", mode="wt", encoding="cp949", newline='')
writer = csv.writer(f)
writer.writerow(["종목명", "종목코드", "PER"])
writer.writerow(["삼성전자", "005930", 15.59])
writer.writerow(["NAVER", "035420", 55.82])
f.close()
"""

#294
# 읽어올때는 mode="rt" 이렇게 바꿔준다. 생략도 가능하다
"""
f = open("C:/Users/Shiro/Desktop/Job/Python/Python-300/buying1.txt", mode="rt", encoding="utf-8")
lines = f.readlines()

codes = []
for line in lines:
    code = line.strip()  # 공백 제거
    codes.append(code)

print(codes)

f.close()
"""

#295
"""
f = open("C:/Users/Shiro/Desktop/Job/Python/Python-300/buying2.txt", mode="rt", encoding="utf-8")
lines = f.readlines()   # 읽어들이는 함수

data = {}
for line in lines:
    line = line.strip()     # 공백 제거
    k, v = line.split()
    #print(k, v)
    data[k] = v   # 키와 값을 추가한다

print(data)
f.close()
"""

#296
"""
per = ["10.31", "", "8.00"]

for i in per:
    try:      # 실행할 코드
        print(float(i))
    except:   #예외가 발생했을 때 처리하는 코드
        print(0)
"""

#297
"""
per = ["10.31", "", "8.00"]

a = []
for x in per:
    try:      # 실행할 코드
        a.append(float(x))
    except:   #예외가 발생했을 때 처리하는 코드
        a.append(0)
print(a)
# 다른 방법
new_per = []

for i in per:
    try:
        v = float(i)
    except:   # 모든 에러에 대해서 예외처리한다
        v = 0
    new_per.append(v)

print(new_per)
"""

#298
"""
try:
    b = 3 / 0
except ZeroDivisionError:   # 특정 에러에 대해서만 설정할 때 에러 이름을 설정할 수 있다
    print("0으로 나누면 안되요")
"""

#299
"""
SyntaxError : 잘못된 문법
NameError : 참조변수 없음
ZeroDivisionError : 0으로 나눌 수 없음
IndexError : 인덱스 범위 벗어남
ValueError : 참조 값이 없음
KeyError : 키 없음 에러 (주로 딕셔너리 사용시)
AttributeError : 모듈, 클래스의 잘못된 속성 사용함
FileNotFoundError : 파일 못 찾음
TypeError : 타입 안 맞음
"""
"""
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as a:
        print(a)
"""

#300
# try, except, else, finally 구조
"""
try:
    실행 코드
except:
    예외가 발생했을 때 수행할 코드
else:
    예외가 발생하지 않았을 때 수행할 코드
finally:
    예외 발생 여부와 상관없이 항상 수행할 코드
"""
"""
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")
"""