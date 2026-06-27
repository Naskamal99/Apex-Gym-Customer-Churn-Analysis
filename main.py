import pandas as pd

# TASK 1: DATA AUDIT
print("=== TASK 1: DATA AUDIT ===")
df = pd.read_csv('gym_churn.csv')
print(f"Dataset Dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
print("\nMissing Values Per Column:")
print(df.isnull().sum())

# TASK 2: CHURN BASELINE
print("\n=== TASK 2: CHURN BASELINE ===")
churn_percentage = ((df['Churn'] == 1).mean()) * 100 
print(f"Overall Churn Percentage: {churn_percentage:.2f}%")
print("\nAverage Churn Rate by Contract Length:")
churn_contract = df.groupby('Contract_period')['Churn'].mean()
print(churn_contract)

# TASK 3: FEATURE ENGINEERING
print("\n=== TASK 3: FEATURE ENGINEERING ===")
bins = [0, 24, 35, 150]
labels = ['Under 25', '25-35', 'Above 35']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
df['Total_Visits_Estimated'] = (df['Lifetime'] * df['Avg_class_frequency_total']).round(2)

output_file = 'gym_churn_processed.csv'
df.to_csv(output_file, index=False)
print(f"Success! Exported processed file to {output_file}")
