# https://wikidocs.net/7028

#101
# bool
"""
불 자료형은 다음 2가지 값만을 가질 수 있다.
 - True - 참 : 값이 비어있지 않으면 참, 1은 참
 - False - 거짓 : 값이 비어있으면 거짓, 0과 None은 거짓
"""

#102
# False
#print(3 == 5)

#103
# True
#print(3 < 5)

#104
# True
"""
x = 4
print(1 < x < 5)
"""

#105
# True
#print ((3 == 3) and (4 != 3))

#106
#print(3 >= 4)

#107
# 결과값을 만족하지 않기에 아무것도 출력되지 않는다
"""
if 4 < 3:
    print("Hello World")
"""

#108
# "Hi, there."
"""
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
"""

#109
"""
1
2
4
"""
"""
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
"""

#110
"""
3
5
"""
"""
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
"""