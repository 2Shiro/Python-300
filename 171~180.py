# https://wikidocs.net/25315

#171 ~ 174
price_list = [32100, 32150, 32000, 32500]
#171
"""
for a in range(4):
    print(price_list[a])
"""

#172
"""
for a in range(4):
    print(a, price_list[a])
"""

#173
"""
for a in range(4):
    print(3 - a, price_list[a])
"""

#174
"""
for a in range(1, 4):
    print(a*10 + 90, price_list[a])
"""

#175
"""
my_list = ["가", "나", "다", "라"]
for a in range(1, 4):
    print(my_list[(a - 1)], my_list[a])
"""

#176
"""
my_list = ["가", "나", "다", "라", "마"]
for a in range(2, 5):
    print(my_list[(a - 2)], my_list[(a - 1)], my_list[a])
"""

#177
"""
my_list = ["가", "나", "다", "라"]
for a in range(3, 0, -1):
    print(my_list[a], my_list[(a - 1)])
"""

#178
"""
my_list = [100, 200, 400, 800]
for a in range(1, 4):
    print(my_list[a] - my_list[(a - 1)])
"""

#179
"""
my_list = [100, 200, 400, 800, 1000, 1300]
for a in range(2, 6):
    print((my_list[(a - 2)] + my_list[(a - 1)] + my_list[a]) / 3)
"""

#180
"""
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for a in range(5):
    volatility.append(high_prices[a] - low_prices[a])
print(volatility)
"""