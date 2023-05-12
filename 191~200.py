# https://wikidocs.net/78565

#191 ~ 194
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
#191
"""
for a in data:
    for x in a:
        y = x * 1.00014
        print(y)
"""

#192
"""
for a in data:
    for x in a:
        y = x * 1.00014
        print(y)
    print("----")
"""

#193
"""
result = []
for a in data:
    for x in a:
        y = x * 1.00014
        result.append(y)
print(result)
"""

#194
"""
result = []
for a in data:
    result2 = []
    for x in a:
        y = x * 1.00014
        result2.append(y)
    result.append(result2)
print(result)
"""

#195 ~ 200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
#195
"""
for a in ohlc[1:]:
    print(a[3])
"""

#196
"""
for a in ohlc[1:]:
    if a[3] > 150:
        print(a[3])
"""

#197
"""
for a in ohlc[1:]:
    if a[3] >= a[0]:
        print(a[3])
"""

#198
"""
volatility = []
for a in ohlc[1:]:
    x = a[1] - a[2]
    volatility.append(x)
print(volatility)
"""

#199
"""
for a in ohlc[1:]:
    if a[3] > a[0]:
        print(a[1] - a[2])
"""

#200
"""
sum = 0
for a in ohlc[1:]:
    x = a[0] - a[3]
    sum += x
print(sum)
"""