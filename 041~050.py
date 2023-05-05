# https://wikidocs.net/78558

#041
# .upper() 대문자로 치환
"""
ticker = "btc_krw"
print(ticker.upper())
"""

#042
# .lower() 소문자로 치환
"""
ticker = "BTC_KRW"
print(ticker.lower())
"""

#043
# .capitalize() 첫자리만 대문자로 치환
"""
h = 'hello'
print(h.capitalize())
"""

#044
# .endswith("확인할 문자열")
"""
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
"""

#045
# .endswith("확인할 문자열")
"""
file_name = "보고서.xlsx"
# 함께 쓰려면 괄호 한번 더 해주기
print(file_name.endswith(("xlsx", "xls")))
"""

#046
# .startswith("확인할 문자열")
"""
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))
# .startswith() 함수도 가능함
print(file_name.startswith(("2020", "보고서")))
"""

#047
# .split("구분의 기준이 될 문자")
"""
a = "hello world"
print(a.split(" "))
"""

#048
# .split("구분의 기준이 될 문자")
"""
ticker = "btc_krw"
print(ticker.split("_"))
"""

#049
# .split("구분의 기준이 될 문자")
"""
date = "2020-05-01"
print(date.split("-"))
"""

#050
# .strip("제거할 문자") : 양쪽 제거
# .rstrip("제거할 문자") : 오른쪽 제거
# .lstrip("제거할 문자") : 왼쪽 제거
"""
data = "039490     "
print(data.rstrip(" "))
"""