CREATE VIEW student_finance_summary AS
SELECT 
    student_id,
    gender,
    level,
    Residence_Type,
    gpa,
    month,
    income,
    [TOTAL EXPENSES],
    savings,
    expense_to_income_ratio
FROM MERGED_DATASET;
