# https://wikidocs.net/78564

#181
# 이차원 리스트란 리스트를 원소로 갖는 리스트이다. ex) a = [ ["준석", 26], ["예림", 30] ]
#apart = [ ["101호", "102호"], ["201호", "202호"], ["301호", "302호"] ]

#182
#stock = [ ["시가", 100, 200, 300], ["종가", 80, 210, 330] ]

#183
#stock = {"시가" : [100, 200, 300], "종가" : [80, 210, 330]}

#184
#stock = {"10/10" : [80, 110, 70, 90], "10/11" : [210, 230, 190, 200]}

#185
#185 ~ 190
apart = [ [101, 102], [201, 202], [301, 302] ]
"""
for a in apart:
    print(a[0], "호")
    print(a[1], "호")
# 다른 방법
for a in apart:
    for x in a:
        print(x, "호")
"""

#186
"""
for a in apart[::-1]:
    print(a[0], "호")
    print(a[1], "호")
# 다른 방법
for a in apart[::-1]:
    for x in a:
        print(x, "호")
"""

#187
"""
for a in apart[::-1]:
    print(a[1], "호")
    print(a[0], "호")
# 다른 방법
for a in apart[::-1]:
    for x in a[::-1]:
        print(x, "호")
"""

#188
"""
for a in apart:
    for x in a:
        print(x, "호")
        print("-----")
"""

#189
"""
for a in apart:
    for x in a:
        print(x, "호")
    print("-----")
"""

#190
"""
for a in apart:
    for x in a:
        print(x, "호")
print("-----")
"""