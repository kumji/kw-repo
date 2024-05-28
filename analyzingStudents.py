import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#matplotlib
# 파이썬으로 기본적인 차트들을 쉽게 그릴 수 있도록 도와주는 시각화 라이브러리
# seaborn
# matplotlib 기반으로 만들어진 통계 데이터 시각화 라이브러리

data = pd.read_csv("student_data.csv")

# 영어, 수학, 과학 학점 평균값 구하기 (1교시 예제)
data['average'] = data[['english', 'math', 'sciences']].mean(axis=1)

# 총 과목 평균을 A/B/C/D 학점 환산해서 'final_grade' 열 추가하기
# 조건
# 2.5 미만일 경우, 'E'
# 2.8 미만일 경우, 'D'
# 3.0 미만일 경우, 'C'
# 3.2 미만일 경우, 'C+'
# 3.5 미만일 경우, 'B'
# 3.8 미만일 경우, 'B+'
# 3.8 이상일 경우, 'A'

print(data['average'])

temp = []
for i in data['average']:
    if i < 2.5:
        temp.append('E')
    elif i < 2.8:
        temp.append('D')
    elif i < 3.0:
        temp.append('C')
    elif i < 3.2:
        temp.append('C+')
    elif i < 3.5:
        temp.append('B')
    elif i < 3.8:
        temp.append('B+')
    else:
        temp.append('A')

data['grade'] = temp

print(data)

# Top3 학생 이름 출력하기
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
df1 = data.sort_values('average', ascending=False).head(3)['name']
print(df1)

# # 학생 수가 많은 나라 10개국을 그래프로 표시해보자.
# # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html

# plt.figure(1)
# top_10 = (data['nationality'].value_counts()).iloc[:10]
# print(top_10)
# colors = ['#1b9e77', '#a9f971', '#fdaa48','#6890F0','#A890F0']
# graph1 = top_10.plot(kind='barh', color = colors)

# # 성별 학생수를 그래프로 표시해보자.
# plt.figure(2)
# graph2 = data['gender'].value_counts().plot(kind='bar', color = ['red', 'blue'])


# # 등급별 학생수를 그래프로 표시해보자.
# plt.figure(3)
# graph3 = data['grade'].value_counts().plot(kind='bar', xlabel='grade', ylabel='num of students')


# # 등급별 남/녀 비율을 그래프로 표시해보자.
# # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
# plt.figure(4)
# test = data.groupby('grade')['gender'].value_counts().unstack()
# test.plot(kind='bar')

# plt.show()

