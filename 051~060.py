# https://wikidocs.net/7023

#051 ~ 055
"""
#051
# 리스트명 = [원소1, 원소2, 원소3, ...]
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

#052
# .append("추가할 원소")
movie_rank.append("배트맨")
print(movie_rank)

#053
# .insert(요소 위치, "추가할 원소")
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

#054
# .remove("삭제할 원소")
movie_rank.remove("럭키")
print(movie_rank)
# del 리스트[원소 위치]
movie_rank2 = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank2[3]
print(movie_rank2)

#055
# .remove("삭제할 원소")
movie_rank.remove("스플릿")
movie_rank.remove("배트맨")
print(movie_rank)
# del 리스트[원소 위치]
movie_rank2 = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank2[2]
del movie_rank2[2]
print(movie_rank2)
"""

#056
"""
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)
"""

#057
"""
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))
"""

#058
"""
nums = [1, 2, 3, 4, 5]
print(sum(nums))
"""

#059
# len(리스트) : 리스트의 원소 총 개수를 세는 합수
"""
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
"""

#060
# 평균 = sum(리스트) / len(리스트)
"""
nums = [1, 2, 3, 4, 5]
print(sum(nums) / len(nums))
"""