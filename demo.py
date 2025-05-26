import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#load the dataset
df=pd.read_csv("StudentsPerformance.csv")
#Show the first 5 rows
print(df.head())
#Show the last 5 rows
print(df.tail())
#print average maths score
print("Average math score:", df['math score'].mean())
#print Highest Reading Score
print("Highest reading score:", df['reading score'].max())
print("Students with 100 in writing:", df[df['writing score'] == 100])
#Histogram of maths score
sns.histplot(df['math score'], bins=20, color='red')
plt.title('Distribution of Math Scores')
plt.show()
#Boxplot By Gender
plt.figure(figsize=(8,5))
sns.boxplot(x='gender', y='math score', data=df)
plt.title('Math Score by Gender')
plt.show()

