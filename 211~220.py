# https://wikidocs.net/23907

#211
"""
안녕
Hi
"""
"""
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")
"""

#212
"""
7
15
"""
"""
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)
"""

#213
# 문자열을 입력해주지 않아서 오류가 발행하고 있다
"""
def 함수(문자열) :
    print(문자열)
함수()
"""

#214
# 같은 타입의 값을 받아서 출력하는 함수인데
# 다른 타입의 문자열과 숫자열을 바인딩했기때문에 오류가 발생하는 것이다
"""
def 함수(a, b) :
    print(a + b)

함수("안녕", 3)
"""

"""
#215
def print_with_smile(a):
    print (a + ":D")


#216
print_with_smile("안녕하세요")
"""

#217
"""
def print_upper_price(a):
    print(a * 1.3)
print_upper_price(300)
"""

#218
"""
def print_sum(a, b):
    print (a + b)
print_sum(8, 4)
"""

#219
"""
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)
print_arithmetic_operation(3, 4)
"""

#220
"""
def print_max(a, b, c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    elif c >= a and c >= b:
        print(c)
print_max(1, 2, 3)
# 다른 방법
def print_max2(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)
print_max2(1, 2, 3)
"""