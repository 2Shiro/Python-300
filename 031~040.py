# https://wikidocs.net/7024

#031
"""
a = "3"
b = "4"
print(a + b)
# 34
"""

#032
#print("Hi" * 3)
# HiHiHi

#033
#print("-" * 80)

#034
"""
t1 = 'python'
t2 = 'java'
print(t1, t2, t1, t2, t1, t2, t1, t2, sep = " ")

t3 = t1 + " " + t2 + " "
print(t3 * 4)
"""

#035 ~ 037
"""
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

#035
# % formtatting이라 함은 자료형에 따라 값을 대입하는 것임
# print("%s %d %f" % (문자열, 정수, 실수))
# %s : 문자열 / %d : 정수 / %f : 실수
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

#036
# print("{} {} {}".format(문자열, 정수, 실수))
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

#037
# 변수 = 값
# print(f"{변수}")
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
"""

#038
"""
상장주식수 = "5,969,782,550"
stock_str = 상장주식수.replace(",", "")
stock_num = int(stock_str)
print(stock_num, type(stock_num))
"""

#039
"""
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
"""

#40
# .strip("제거할 문자")
"""
data = "   삼성전자    "
print(data.strip(" "))
"""