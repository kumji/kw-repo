import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#matplotlib
# 파이썬으로 기본적인 차트들을 쉽게 그릴 수 있도록 도와주는 시각화 라이브러리

data = pd.read_csv("student_data.csv")

# 영어, 수학, 과학 학점 평균값 구하기 (1교시 예제)
# print(data['average'])

# 총 과목 평균을 A/B/C/D 학점 환산해서 'grade' 열 추가하기
# 조건
# 2.5 미만일 경우, 'E'
# 2.8 미만일 경우, 'D'
# 3.0 미만일 경우, 'C'
# 3.2 미만일 경우, 'C+'
# 3.5 미만일 경우, 'B'
# 3.8 미만일 경우, 'B+'
# 3.8 이상일 경우, 'A'

# temp = []
# for i in data['average']:
    # 알맞은 if / elif / else 조건문을 완성하세요.
# data['grade'] = temp

print(data)

# Top3 학생 이름 출력하기
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html


# 학생 수가 많은 나라 10개국을 그래프로 표시해보자.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html

top_10 = (data['nationality'].value_counts()).iloc[:10]
print(top_10)
colors = ['#1b9e77', '#a9f971', '#fdaa48','#6890F0','#A890F0']
graph1 = top_10.plot(kind='barh', color = colors)
plt.show()


# 성별 학생수를 그래프로 표시해보자.


# 등급별 학생수를 그래프로 표시해보자.


# 등급별 남/녀 비율을 그래프로 표시해보자.
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

