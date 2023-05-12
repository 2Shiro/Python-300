# https://wikidocs.net/7039

#221
"""
def print_reverse(a):
    print(a[::-1])
print_reverse("python")
"""

#222
"""
def print_score(a):
    for x in a:
        x += x
    print(x / len(a))
print_score ([1, 2, 3])
"""

#223
"""
def print_even(a):
    for x in a:
        if (x % 2) == 0:
            print(x)
print_even([1, 3, 2, 10, 12, 11, 15])
"""

#224
"""
def print_key(a):
    for x in a.keys():
        print(x)
print_key({"이름":"김말똥", "나이":30, "성별":0})
"""

#225
"""
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(my_dict, key):
    print(my_dict[key])
print_value_by_key(my_dict, "10/26")
"""

#226


#227


#228
"""
def calc_monthly_salary(annual_salary):
    month_salary = int(annual_salary / 12)
    print(month_salary)
calc_monthly_salary(12000000)
"""

#229
"""
왼쪽: 100
오른쪽 : 200
"""
"""
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)
"""

#230
"""
왼쪽: 200
오른쪽 : 100
"""
"""
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)
"""