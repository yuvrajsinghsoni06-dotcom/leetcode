-- Write your PostgreSQL query statement below
select distinct num as ConsecutiveNums
from (
    select num,
    lead(num,1) over(order by id) as next_num,
    lag(num,1) over (order by id) as prev_num
    from logs
) as ranklogs
where num = next_num and num = prev_num





 