import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("data\\stud.csv")

# print(df.head(10))

# print(df.isna().sum())

# print(df.duplicated().sum())

#df.info()

# print(df.nunique())

# print(df.describe())

# print("Categories in 'gender' variable:     ",end=" " )
# print(df['gender'].unique())

# print("Categories in 'race_ethnicity' variable:  ",end=" ")
# print(df['race_ethnicity'].unique())

# print("Categories in'parental level of education' variable:",end=" " )
# print(df['parental_level_of_education'].unique())

# print("Categories in 'lunch' variable:     ",end=" " )
# print(df['lunch'].unique())

# print("Categories in 'test preparation course' variable:     ",end=" " )
# print(df['test_preparation_course'].unique())


# # define numerical & categorical columns
# numeric_features = [feature for feature in df.columns if df[feature].dtype == 'int64']
# categorical_features = [feature for feature in df.columns if df[feature].dtype == 'str']

# # print columns
# print('We have {} numerical features : {}'.format(len(numeric_features), numeric_features))
# print('\nWe have {} categorical features : {}'.format(len(categorical_features), categorical_features))


df['total score'] = df['math_score'] + df['reading_score'] + df['writing_score']
df['average'] = df['total score']/3
print(df.head())


reading_full = df[df['reading_score'] == 100]['average'].count()
writing_full = df[df['writing_score'] == 100]['average'].count()
math_full = df[df['math_score'] == 100]['average'].count()

print(f'Number of students with full marks in Maths: {math_full}')
print(f'Number of students with full marks in Writing: {writing_full}')
print(f'Number of students with full marks in Reading: {reading_full}')

reading_less_20 = df[df['reading_score'] <= 20]['average'].count()
writing_less_20 = df[df['writing_score'] <= 20]['average'].count()
math_less_20 = df[df['math_score'] <= 20]['average'].count()

print(f'Number of students with less than 20 marks in Maths: {math_less_20}')
print(f'Number of students with less than 20 marks in Writing: {writing_less_20}')
print(f'Number of students with less than 20 marks in Reading: {reading_less_20}')

# fig, axs = plt.subplots(1, 2, figsize=(15, 7))
# plt.subplot(121)
# sns.histplot(data=df,x='average',bins=30,kde=True,color='g')
# plt.subplot(122)
# sns.histplot(data=df,x='average',kde=True,hue='gender')
# plt.show()


# plt.subplots(1,3,figsize=(25,6))
# plt.subplot(141)
# sns.histplot(data=df,x='average',kde=True,hue='lunch')
# plt.subplot(142)
# sns.histplot(data=df[df.gender=='female'],x='average',kde=True,hue='lunch')
# plt.subplot(143)
# sns.histplot(data=df[df.gender=='male'],x='average',kde=True,hue='lunch')
# plt.show()

# plt.subplots(1,8,figsize=(35,25))
# plt.subplot(141)
# ax =sns.histplot(data=df,x='average',kde=True,hue='parental_level_of_education')
# plt.subplot(142)
# ax =sns.histplot(data=df[df.gender=='male'],x='average',kde=True,hue='parental_level_of_education')
# plt.subplot(143)
# ax =sns.histplot(data=df[df.gender=='female'],x='average',kde=True,hue='parental_level_of_education')
# plt.show()

plt.subplots(1,3,figsize=(25,6))
plt.subplot(141)
ax =sns.histplot(data=df,x='average',kde=True,hue='race_ethnicity')
plt.subplot(142)
ax =sns.histplot(data=df[df.gender=='female'],x='average',kde=True,hue='race_ethnicity')
plt.subplot(143)
ax =sns.histplot(data=df[df.gender=='male'],x='average',kde=True,hue='race_ethnicity')
plt.show()