import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("StudentsPerformance.csv")
print(df.head())
print("Average math score:", df['math score'].mean())
print("Highest reading score:", df['reading score'].max())
print("Students with 100 in writing:", df[df['writing score'] == 100])
sns.histplot(df['math score'], bins=20, color='red')
plt.title('Distribution of Math Scores')
plt.show()
plt.figure(figsize=(8,5))
sns.boxplot(x='gender', y='math score', data=df)
plt.title('Math Score by Gender')
plt.show()

