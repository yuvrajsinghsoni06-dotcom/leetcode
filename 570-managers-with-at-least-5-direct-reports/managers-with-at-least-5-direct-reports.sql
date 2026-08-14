-- Write your PostgreSQL query statement below
select a.name
from employee a
join employee b
     on a.id = b.managerId
group by a.name, a.id
having count(a.id) >= 5;