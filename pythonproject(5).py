import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

# Load the Excel File
df=pd.read_csv("C:/Users/Rahul/Documents/python project/INT327 (2) (1).csv")

# Show the first few rows of the data
print("First few rows of the dataset:")
print(df.head())

# Print the columns and their data types in the dataset
print("\nColumns and their data types:")
print(df.dtypes)

# Check for basic info about the dataset
print("\nBasic info about the dataset:")
print(df.info())

# 1. DATA CLEANING
print("Initial Shape:", df.shape)

# Check for missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Drop rows with missing pollutant data
df_clean = df.dropna(subset=['pollutant_min', 'pollutant_max', 'pollutant_avg'])

# Check data types and info
print("\nCleaned Data Info:")
print(df_clean.info())

# 2. BASIC STATISTICS(Describe the dataset)
print("\nSummary Statistics:")
print(df_clean.describe(include='all'))

# 3. POLLUTANT DISTRIBUTION
plt.figure(figsize=(10, 6))
sns.countplot(data=df_clean, y='pollutant_id',hue='pollutant_id', order=df_clean['pollutant_id'].value_counts().index, palette='viridis')
plt.title('Pollutant Count Distribution')
plt.xlabel('Count')
plt.ylabel('Pollutant ID')
plt.tight_layout()
plt.show()
# 4. CORRELATION BETWEEN POLLUTANT VALUES
corr = df_clean[['pollutant_min', 'pollutant_max', 'pollutant_avg']].corr()
plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation between Pollutant Values')
plt.tight_layout()
plt.show()
# 5. AVERAGE POLLUTION LEVEL BY POLLUTANT TYPE
plt.figure(figsize=(10, 6))
avg_pollutant = df_clean.groupby('pollutant_id')['pollutant_avg'].mean().sort_values(ascending=False).reset_index()
sns.barplot(data=avg_pollutant, x='pollutant_avg', y='pollutant_id', hue='pollutant_id', palette='magma', legend=False)
plt.title("Average Pollution Level by Pollutant")
plt.xlabel("Average Value")
plt.ylabel("Pollutant")
plt.tight_layout()
plt.show()

# 6. TOP 10 POLLUTED CITIES (by average pollutant level)
top_cities = df_clean.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(10).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=top_cities, x='pollutant_avg', y='city', hue='city', palette='rocket', legend=False)
plt.title("Top 10 Polluted Cities (Avg Level)")
plt.xlabel("Average Pollution")
plt.ylabel("City")
plt.tight_layout()
plt.show()



# 7. COUNT OF DIFFERENT POLLUTANTS THROGH COUNTPLOT
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='pollutant_id',hue='pollutant_id', palette='Set2',legend=False)
plt.title('Count of Different Pollutants')
plt.xlabel('Pollutant ID')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
# 8. Pair Plot Colored by Pollutant Type
sns.pairplot(df, hue='pollutant_id', 
             vars=['pollutant_min', 'pollutant_max', 'pollutant_avg'], 
             diag_kind='kde', corner=True, plot_kws={'alpha': 0.7})
plt.suptitle("Pair Plot Colored by Pollutant Type", y=1.02)
plt.show()
# 9. STATES WITH HIGHEST AVERAGE POLLUTION
top_states = df_clean.groupby('state')['pollutant_avg'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_states.values, y=top_states.index, palette='coolwarm')
plt.title("Top 10 Polluted States (Avg Level)")
plt.xlabel("Average Pollution")
plt.ylabel("State")
plt.tight_layout()
plt.show()








# 10. INSIGHT SUMMARY
print("\n--- INSIGHTS ---")
print(f"Most common pollutant: {df_clean['pollutant_id'].value_counts().idxmax()}")
print(f"Total stations: {df_clean['station'].nunique()}")
print(f"Cities monitored: {df_clean['city'].nunique()}")
print(f"States monitored: {df_clean['state'].nunique()}")
print(f"Highest average pollution level: {df_clean['pollutant_avg'].max()}")
