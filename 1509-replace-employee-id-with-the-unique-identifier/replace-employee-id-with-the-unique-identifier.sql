-- Write your PostgreSQL query stat
SELECT unique_id , name
FROM Employees a
left JOIN
EmployeeUNI b
on a.id = b.id;
