--GENDER FINANCIAL BEHAVIOUR
SELECT 
    gender,
    ROUND(AVG(income), 2) AS avg_income,
    ROUND(AVG([TOTAL EXPENSES]), 2) AS avg_expenses,
    ROUND(AVG(savings), 2) AS avg_savings
FROM MERGED_DATASET
GROUP BY gender;

--MONTHLY TREND
SELECT 
    month,
    ROUND(AVG(income), 2) AS avg_income,
    ROUND(AVG([TOTAL EXPENSES]), 2) AS avg_expenses,
    ROUND(AVG([TOTAL EXPENSES]), 2) AS avg_savings
FROM MERGED_DATASET
GROUP BY month
ORDER BY Month ASC

--ON-CAMPUS VS OFF-CAMPUS
SELECT 
    Residence_Type,
    ROUND(AVG([TOTAL EXPENSES]), 2) AS avg_expenses,
    ROUND(AVG(savings), 2) AS avg_savings
FROM MERGED_DATASET
GROUP BY Residence_Type;