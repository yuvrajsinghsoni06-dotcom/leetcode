-- Write your PostgreSQL query statement below
select employee_id 
from employees e1
where salary < 30000 
and manager_id  is not null
and not exists (
    select 1
    from employees e2
    where e2.employee_id = e1.manager_id
)
order by employee_id;