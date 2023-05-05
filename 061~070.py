# https://wikidocs.net/7025

#061
"""
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
"""

#062
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
"""

#063
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])
"""

#064
"""
# 리스트.reverse() 역방향 출력
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)
# 다른 방법
nums2 = [1, 2, 3, 4, 5]
print(nums2[::-1])
"""

#065
"""
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])
"""

#066
# "문자".join(리스트) 는 구분자와 같다
"""
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))
"""

#067
# "문자".join(리스트) 는 구분자와 같다
"""
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))
"""

#068
# "문자".join(리스트) 는 구분자와 같다
"""
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))
"""

#069
"""
# split("구분자", maxsplit = 정수)
#                  ㄴ> 생략하면 모든 구분자를 기준으로 나눈다
string = "삼성전자/LG전자/Naver"
string2 = string.split('/')
print(string2)
"""

#070
"""
# 리스트.sort() 는 리스트 원소들을 정렬한다
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
# 다른방법
data1 = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data1)
print(data2)
"""