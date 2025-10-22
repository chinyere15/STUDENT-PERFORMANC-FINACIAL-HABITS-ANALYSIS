--GPA VS SPENDING RATE
SELECT 
    level,
    ROUND(AVG(gpa), 2) AS avg_gpa,
    ROUND(AVG(Savings), 2) AS avg_saving_rate,
    ROUND(AVG(expense_to_income_ratio), 2) AS avg_expense_ratio
FROM MERGED_DATASET
GROUP BY level
ORDER BY level;

-- GPA categories vs financial discipline
SELECT 
    CASE 
        WHEN gpa >= 4.0 THEN 'High GPA'
        WHEN gpa BETWEEN 3.0 AND 3.99 THEN 'Average GPA'
        ELSE 'Low GPA'
    END AS gpa_category,
    ROUND(AVG(savings), 2) AS avg_savings,
    ROUND(AVG([TOTAL EXPENSES]), 2) AS avg_expenses,
    ROUND(AVG(Savings), 2) AS avg_saving_rate
FROM MERGED_DATASET
GROUP BY gpa
ORDER BY avg_saving_rate DESC;

-- Campus status vs GPA
SELECT 
    Residence_Type,
    ROUND(AVG(gpa), 2) AS avg_gpa,
    ROUND(AVG(Savings), 2) AS avg_saving_rate
FROM MERGED_DATASET
GROUP BY Residence_Type;