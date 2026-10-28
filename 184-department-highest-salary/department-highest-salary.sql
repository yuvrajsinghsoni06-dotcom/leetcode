-- Write your PostgreSQL query statement below
WITH rankingsalary AS (
    SELECT 
        id, 
        name, 
        salary, 
        departmentId, 
        RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rk 
    FROM employee
) 
SELECT 
    d.name AS Department, 
    e.name AS Employee, 
    e.salary AS Salary 
FROM rankingsalary e 
JOIN department d ON d.id = e.departmentId 
WHERE e.rk = 1;