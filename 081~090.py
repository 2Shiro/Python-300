# https://wikidocs.net/22000

#081 ~ 083
# 나머지를 바인딩 하는 변수 앞에 *를 붙여준다
# 별 표현식 변수를 제외한 변수부터 채우기 때문에 위치를 잘 봐야한다
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
#081
"""
*valid_score, a, b = scores
print(valid_score)
"""

#082
"""
a, b, *valid_score = scores
print(valid_score)
"""

#083
"""
a, *valid_score, b = scores
print(valid_score)
"""

#084
# 딕셔너리는 키(key)와 값(value)이 한 쌍이 하나의 대응 관계를 가지고 있는 자료형
"""
temp = {}
print(type(temp))
# <class 'dict'>
"""

#085 ~ 086
#085
"""
ice = {"메로나" : 1000, "폴라포" : 1200, "빵빠레" : 1800}
#print(ice)

#086
ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice)
"""

#087 ~ 089
ice = {"메로나" : 1000, "폴라포" : 1200, "빵빠레" : 1800, "죠스바" : 1200, "월드콘" : 1500}
#087
#print("메로나 가격: ", ice["메로나"])

#088
# 값변경할 때는 딕셔너리["key"] = 수정할 value
"""
ice["메로나"] = 1300
print("메로나 가격: ", ice["메로나"])
"""

#089
"""
del ice["메로나"]
print(ice)
"""

#090
"""
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(icecream['누가바'])
# 없는 key를 사용했으니 오류가 발생하는 것이다
"""