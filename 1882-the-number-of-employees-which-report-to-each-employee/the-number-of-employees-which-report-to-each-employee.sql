SELECT 
    e.employee_id,
    e.name,
    r.reports_count,
    r.average_age
FROM (
    SELECT 
        reports_to,
        COUNT(*) AS reports_count,
        ROUND(AVG(age)) AS average_age
    FROM employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
) r
JOIN employees e 
    ON e.employee_id = r.reports_to
ORDER BY e.employee_id;