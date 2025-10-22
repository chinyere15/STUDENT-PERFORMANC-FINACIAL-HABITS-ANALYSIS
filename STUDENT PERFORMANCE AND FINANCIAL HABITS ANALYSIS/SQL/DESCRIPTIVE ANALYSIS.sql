--OVERALL AVERAGES
SELECT 
    ROUND(AVG(Income), 2) AS avg_income,
    ROUND(AVG([TOTAL EXPENSES]), 2) AS avg_expenses,
    ROUND(AVG(Savings), 2) AS avg_savings
FROM MERGED_DATASET;

--AVERAGES BY ACADEMIC LEVEL
SELECT 
    level,
    ROUND(AVG(income), 2) AS avg_income,
    ROUND(AVG([TOTAL EXPENSES]), 2) AS avg_expenses,
    ROUND(AVG(savings), 2) AS avg_savings
FROM MERGED_DATASET
GROUP BY level
ORDER BY level;