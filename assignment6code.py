import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# load dataset
df = pd.read_csv("New_York_City_Leading_Causes_of_Death.csv")

# making columns more readable and processable by python; removing spaces and caps
df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns) 


# convert relevant columns to numeric (some are stored as text; learned from chatgpt because it was not working)
df["deaths"] = pd.to_numeric(df["deaths"], errors="coerce")
df["death_rate"] = pd.to_numeric(df["death_rate"], errors="coerce")
df["age_adjusted_death_rate"] = pd.to_numeric(df["age_adjusted_death_rate"], errors="coerce")

# drop the missing values
df = df.dropna()

## WHAT ARE THE TOP 10 LEADING CAUSES OF DEATH IN NYC?
# group by leading cause and sum of deaths
# top_causes = df.groupby("leading_cause")["deaths"].sum().nlargest(10)

# plt.figure(figsize=(12, 6))
# sns.barplot(x=top_causes.values, y=top_causes.index, palette="Reds_r")
# plt.xlabel("Number of Deaths")
# plt.ylabel("Leading Cause of Death")
# plt.title("Top 10 Leading Causes of Death in NYC since 2007")
# plt.show()



## HOW DO DEATH RATES VARY BY SEX FOR THE TOP CAUSES?
# filter for top causes
# top_causes_list = top_causes.index.tolist()
# filtered_df = df[df["leading_cause"].isin(top_causes_list)]

# # plot using seaborn
# plt.figure(figsize=(14, 6))
# sns.barplot(
#     data=filtered_df, 
#     x="leading_cause", 
#     y="death_rate", 
#     hue="sex", 
#     palette="coolwarm"
# )
# plt.xticks(rotation=45)
# plt.xlabel("Leading Cause")
# plt.ylabel("Death Rate")
# plt.title("Death Rate by Sex for Top 10 Causes of Death in NYC")
# plt.legend(title="Sex")
# plt.show()



## IS THERE A CORRELATION BETWEEN DEATH RATE AND AGE ADJUSTED DEATH RATE?
# scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df["death_rate"], y=df["age_adjusted_death_rate"], alpha=0.6, color="blue")
sns.regplot(x=df["death_rate"], y=df["age_adjusted_death_rate"], scatter=False, color="red")
plt.xlabel("Death Rate")
plt.ylabel("Age Adjusted Death Rate")
plt.title("Correlation Between Death Rate and Age Adjusted Death Rate")
plt.show()



print(df.columns)  # This will print all column names
print(df.head())   # This will show the first few rows of data

