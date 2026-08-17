-- All employees with their explicitly marked primary department
SELECT employee_id, department_id
FROM employee
WHERE primary_flag = 'Y'

UNION

-- All employees who belong to only 1 department
SELECT employee_id, department_id
FROM employee
GROUP BY employee_id, department_id
HAVING employee_id IN (
    SELECT employee_id
    FROM employee
    GROUP BY employee_id
    HAVING COUNT(department_id) = 1
);