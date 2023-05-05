# https://wikidocs.net/7022

#021
#한글자씩 가져오는 것을 인덱싱이라고 한다. 순서는 0부터 시작.
"""
letters = 'python'
print(letters[0], letters[2])
"""

#022
#문자열에서 여러 글자를 가져오는 것을 슬라이싱이라고 한다.
"""
license_plate = "24가 2210"
print(license_plate[-4:])
"""

#023
#슬라이싱할 때 [시작인덱스:끝인덱스:보폭]을 지정할 수 있다.
"""
string = "홀짝홀짝홀짝"
print(string[::2])
"""

#024
"""
string = "PYTHON"
print(string[::-1])
"""

#025
#replace("변경 대상 문자", "변경 결과 문자")
"""
phone_number = "010-1111-2222"
number = phone_number.replace("-", " ")
print(number)
"""

#026
"""
phone_number = "010-1111-2222"
number = phone_number.replace("-", "")
print(number)
"""

#027
"""
url = "http://sharebook.kr"
print(url[-2:])

url_split = url.split('.')  # 문자열 구분자
print(url_split[-1])
"""

#028
"""
lang = 'python'
lang[0] = 'P'
print(lang)
#문자열은 불변이기 때문에 오류가 뜬다.
"""

#029
"""
string = 'abcdfe2a354a32a'
A_string = string.replace("a", "A")
print(A_string)
"""

#030
"""
string = 'abcd'
string.replace('b', 'B')
print(string)
#문자열은 변경할 수 없는 자료형이기 때문에 abcd 그대로 출력된다.
string = 'abcd'
string = string.replace('b', 'B')
print(string)
#이렇게 변경하면 바꿀수 있다.
"""