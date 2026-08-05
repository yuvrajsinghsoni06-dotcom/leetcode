-- Write your PostgreSQL query statement below
select *, 
case
when greatest(x,y,z) >= (x + y + z - greatest(x,y,z))
then 'No'
else 'Yes' end as triangle
from triangle;