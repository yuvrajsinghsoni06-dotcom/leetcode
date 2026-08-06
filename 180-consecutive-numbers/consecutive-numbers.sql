-- Write your PostgreSQL query statement below
with ranklogs as (
    select num,
    lead(num,1) over(order by id) as next_num,
    lag(num,1) over(order by id ) as prev_num
    from logs
)
select distinct num as ConsecutiveNums
from ranklogs
where num = next_num and num = prev_num;




 