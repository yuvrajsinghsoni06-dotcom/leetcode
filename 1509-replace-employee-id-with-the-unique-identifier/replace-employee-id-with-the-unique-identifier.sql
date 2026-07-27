-- Write your PostgreSQL query stat
SELECT b.unique_id , a.name
FROM Employees a
left JOIN
EmployeeUNI b
on a.id = b.id;
