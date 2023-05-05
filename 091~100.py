# https://wikidocs.net/78563

#091 ~ 094
"""
#091
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory)

#092
print(inventory["메로나"][0], "원")

#093
print(inventory["메로나"][1], "개")

#094
# 딕셔너리에 데이터를 추가할 때는 딕셔너리[키] = [값]
inventory["월드콘"] = [500, 7]
print(inventory)
"""

#095 ~ 098
"""
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
#095
# key값만 추출할 때는 딕셔너리.keys()
print(icecream.keys())

#096
# value값만 추출할 때는 딕셔너리.values()
print(icecream.values())

#097
print(sum(icecream.values()))

#098
# 2개의 딕셔너리를 합칠 때는 딕셔너리.update({"업데이트 할 키" : 업데이트 할 값})
icecream.update({'팥빙수':2700, '아맛나':1000})
print(icecream)
"""

#099
# 두 그룹의 데이터를 엮어줄 때는 zip(첫번째 그룹, 두번째 그룹)
"""
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)
"""

#100
# 두 그룹의 데이터를 엮어줄 때는 zip(첫번째 그룹, 두번째 그룹)
"""
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
"""