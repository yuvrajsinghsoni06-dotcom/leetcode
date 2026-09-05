-- Write your PostgreSQL query statement below
select Department , Employee, Salary from
(select d.name as Department , e.name as Employee , e.salary as Salary,
DENSE_RANK() over(
    partition by e.departmentId
    order by e.salary desc 
) as drk
from employee e
inner join department d
on e.departmentID = d.id)
where drk <= 3;