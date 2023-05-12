# https://wikidocs.net/7040

import datetime
import time
import os
import numpy

#241
# datetime.datetime.now()를 사용하면 현재시간
"""
a = datetime.datetime.now()
print(a)
"""

#242
"""
a = datetime.datetime.now()
print(type(a))
"""

#243
"""
datetime.timedelta()는 두 날짜의 차이를 계산할 때 사용하는 함수이다
days = 일
seconds = 초
microseconds = 마이크로 초
milliseconds = 밀리 초(1밀리 초는 1000마이크로 초)
minutes = 분
hours = 시간
weeks = 주
"""
"""
a = datetime.datetime.now()
for x in range(5, 0, -1):
    delta = datetime.timedelta(days=x)
    date = a - delta
    print(date)
"""

#244
# 날짜 형식을 문자열로 변환할때 strftime
"""
%d : 0을 채운 10진수 표기로 날짜를 표시
%m : 0을 채운 10진수 표기로 월을 표시
%y : 0을 채운 10진수 표기로 2자리 년도
%Y : 0을 채운 10진수 표기로 4자리 년도
%H : 0을 채운 10진수 표기로 시간 (24시간 표기)
%I : 0을 채운 10진수 표기로 시간 (12시간 표기)
%M : 0을 채운 10진수 표기로 분
%S : 0을 채운 10진수 표기로 초
%f : 0을 채운 10진수 표기로 마이크로 초 (6자리)
%A : locale 요일
%a : locale 요일 (단축 표기)
%B : locale 월
%b : locale 월 (단축 표기)
%j : 0을 채운 10진수 표기로 년중 몇 번째 일인지 표시 
%U : 0을 채운 10진수 표기로 년중 몇 번째 주인지 표시 (일요일 시작 기준)
%W : 0을 채운 10진수 표기로 년중 몇 번째 주인지 표시 (월요일 시작 기준)
"""
"""
a = datetime.datetime.now()
print(a.strftime("%H:%M:%S"))
"""

#245
# 문자열을 날짜 형식으로 변환할때 strptime
"""
d = "2020-05-04"
a = datetime.datetime.strptime(d, "%Y-%m-%d")
print(type(a))
"""

#246
"""
while (1):
    a = datetime.datetime.now()
    print(a)
    time.sleep(1)
"""

#247
# 나중에 한번 더 보기 잘모르겠음
"""
import os               # os.rename()
from os import rename   # rename()
from os import *        # getcwd(), rename(), ...
import os import myos   # myos.getcwd()
"""

#248
"""
a = os.getcwd()
print(a)
"""

#249
"""
os.rename("C:/Users/Shiro/Desktop/Job/Python/Python-300/a.txt",
          "C:/Users/Shiro/Desktop/Job/Python/Python-300/b.txt")
"""

#250
# round(a, n) 함수는 소수(a)점 밑에 자리수(n)를 조절 할 수 있다
"""
for a in numpy.arange(0, 5.1, 0.1):
    print(round(a, 1))
"""