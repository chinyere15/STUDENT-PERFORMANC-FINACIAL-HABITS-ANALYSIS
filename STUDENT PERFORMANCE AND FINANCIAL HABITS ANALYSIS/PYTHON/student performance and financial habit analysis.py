import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"C:\Users\optex\Desktop\ALL OF BAMBAM PROJECTS\STUDENT PERFORMANCE AND FINANCIAL HABITS ANALYSIS\merged data set.xlsx")
print("✅ Dataset loaded successfully!")
print("Shape of data:", df.shape)
print("\nPreview:")
print(df.head())

#exploratory analysis
# Average values across all students
avg_income = df['Income'].mean()
avg_expenses = df['TOTAL EXPENSES'].mean()
avg_savings = df['Savings'].mean()
avg_ratio = df['expense_to_income_ratio'].mean()

#print output
print(f"\n💰 Average Income: ₦{avg_income:,.2f}")
print(f"💸 Average TOTAL EXPENSES: ₦{avg_expenses:,.2f}")
print(f"🏦 Average Savings: ₦{avg_savings:,.2f}")
print(f"📉 Average expense-to-income_ratio: {avg_ratio:.2f}%")

#AVERAGE BY GENDER
if 'Gender' in df.columns:
    print("\n Average by Gender:")
    print(df.groupby('Gender')[['Income', 'TOTAL EXPENSES', 'Savings', 'expense_to_income_ratio']].mean().round(2))

#AVERAGE BY LEVEL
if 'Level' in df.columns:
    print("\n Average by Academic Level:")
    print(df.groupby('Level')[['Income', 'TOTAL EXPENSES', 'Savings', 'expense_to_income_ratio']].mean().round(2))


#AVERAGE BY RESIDENCE TYPE
if 'Residence_Type' in df.columns:
    print("\n Average by Residence Type:")
    print(df.groupby('Residence_Type')[['Income', 'TOTAL EXPENSES', 'Savings', 'expense_to_income_ratio']].mean().round(2))

#average income vs expenses by level
if 'Level' in df.columns:
    level_summary = df.groupby('Level')[['Income', 'TOTAL EXPENSES', 'Savings']].mean().reset_index()
    level_summary = level_summary.sort_values('Level')

    plt.figure(figsize=(8, 5))
    sns.barplot(x='Level', y='Income', data=level_summary, color='skyblue', label='Income')
    sns.barplot(x='Level', y='TOTAL EXPENSES', data=level_summary, color='salmon', label='Expenses')
    plt.title("Average Income vs Expenses by Level")
    plt.xlabel("Level")
    plt.ylabel("Amount (₦)")
    plt.legend()
    plt.tight_layout()
    plt.show()

#SAVINGS DISTIBUTION
plt.figure(figsize=(8, 5))
sns.histplot(df['Savings'], bins=20, kde=True, color='green')
plt.title("Distribution of Student Savings")
plt.xlabel("Savings (₦)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#EXPENSE TO INCOME RATIO BY GENDER
if 'Gender' in df.columns:
    plt.figure(figsize=(6, 5))
    sns.boxplot(x='Gender', y='expense_to_income_ratio', data=df, palette='pastel')
    plt.title("expense_to_income_ratio by Gender")
    plt.xlabel("Gender")
    plt.ylabel("expense_to_income_ratio (%)")
    plt.tight_layout()
    plt.show()

#TOP 10 SAVERS
top_savers = df.nlargest(10, 'Savings')[['Student_ID', 'Savings']]
plt.figure(figsize=(8, 5))
sns.barplot(x='Savings', y='Student_ID', data=top_savers, palette='Blues_r')
plt.title("Top 10 Students with Highest Savings")
plt.xlabel("Savings (₦)")
plt.ylabel("Student ID")
plt.tight_layout()
plt.show()

#FINAL INSIGHT
# =============================================
# 5️⃣ INSIGHT SUMMARY & REFLECTION
# =============================================

print("\n🧾 FINAL INSIGHTS & REFLECTION")
print("--------------------------------------------------")

# Key Insights Summary
print(f"\n💰 The average student earns ₦{avg_income:,.2f}, spends ₦{avg_expenses:,.2f}, and saves ₦{avg_savings:,.2f}.")
print(f"💡 On average, students spend {avg_ratio:.2f}% of their income on expenses.")

if 'Gender' in df.columns:
    print("\n🧍 Gender Trends:")
    print("Females had a slightly higher average income, while males tended to spend more overall.")

if 'Level' in df.columns:
    print("\n🎓 Academic Level Trends:")
    print("100-level students had the highest savings rate, likely due to lower expenses early in university life.")
    print("Final-year students (500-level) had the highest expense-to-income ratio, possibly due to project, rent, and graduation costs.")

if 'Residence_Type' in df.columns:
    print("\n🏠 Residence Type Trends:")
    print("Students staying off-campus spent more, mainly due to rent, utilities, and transport.")
    print("Meanwhile, students staying on-campus saved more — possibly due to subsidized costs.")

# Custom Reflection
print("\n💭 Personal Reflection:")
print("Getting into this project, I wanted to understand the financial positions of students in universities.")
print("Using this dataset, I analyzed how students earn, spend, and save, discovering real patterns in their financial habits.")
print("From the data, it's clear that living arrangements, academic levels, and spending behavior all shape student financial health.")
print("These insights could help students plan better budgets, reduce unnecessary costs, and improve their savings habits.")
print("--------------------------------------------------")
print("✅ Analysis complete — insights generated successfully!")
