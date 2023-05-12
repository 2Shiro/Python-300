# https://wikidocs.net/78556

#231
# result는 함수내부에서 정의되었기 때문에 밖에서 사용 불가하다
"""
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print (result)
"""

#232
"""
def make_url(a):
    x = "www." + a + ".com"
    print(x)
    return x
make_url("naver")
"""

#233
"""
def make_list(a):
    a_list = []
    for x in a:
        a_list.append(x)
    print(a_list)
    return a_list
make_list("abcd")
# 다른 방법
def make_list2 (string):
    print(list(string))
    return list(string)
make_list2("abcd")
"""

#234
"""
def pickup_even(a):
    a_list = []
    for x in a:
        if (x % 2) == 0:
            a_list.append(x)
    return a_list
pickup_even([3, 4, 5, 6, 7, 8])
"""

#235
"""
def convert_int(a):
    x = int(a.replace(',', ''))
    print(x)
    return x
convert_int("1,234,567")
"""

#236
# 22
"""
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)
"""

#237
# 22
"""
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)
"""

#238
# 140
"""
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)
"""

#239
# 16
"""
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)
"""

#240
# 28
"""
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
"""