# https://wikidocs.net/7027

#071
"""
my_variable = ()
print(my_variable)
# 확인하는 방법
print(type(my_variable))
"""

#072
"""
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)
"""

#073
# 데이터가 하나만 들어갈 경우에는 반드시 뒤에 ,(콤마) 기입
"""
a = (1,)
print(type(a))
# <class 'tuple'>
"""

#074
"""
t = (1, 2, 3)
t[0] = 'a'
# 튜플은 원소값을 변경할 수 없다. (매우매우 중요!!)
"""

#075
# 튜플은 괄호를 생략해도 된다
"""
t = 1, 2, 3, 4
print(type(t))
# <class 'tuple'>
"""

#076
t = ('a', 'b', 'c')
# 튜플은 원소값을 변경할 수 없기에 새로운 튜플을 작성하면 기존의 튜플은 삭제된다
t = ('A', 'b', 'c')

#077
# 자료형 변환하는 것처럼 변환한다.
"""
interest = ('삼성전자', 'LG전자', 'SK Hynix')
a = list(interest)
print(a)
"""

#078
# 077번 문제와 똑같이 변경하고자 하는 튜플 타입으로 바꿔준다
"""
interest = ['삼성전자', 'LG전자', 'SK Hynix']
a = tuple(interest)
print(a)
"""

#079
"""
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# apple banana cake
"""

#080
# range(시작, 끝, 간격)
"""
a = tuple(range(2, 100, 2))
# 변수에 함수를 바인딩할 때 tuple()안에 넣어준다.
print(a)
"""