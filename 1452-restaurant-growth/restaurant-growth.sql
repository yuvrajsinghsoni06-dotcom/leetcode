with daily_amount as(
    select visited_on , 
    sum(amount) as amount
    from customer
    group by visited_on
),
second_half as (
    select visited_on,
    SUM(amount) over(
        order by visited_on range between interval '6 days' preceding and current row
    ) as amount,
    round(
        Avg(amount) over( order by visited_on range between interval '6 days' preceding and current row),2
    ) as average_amount
    from daily_amount
)

select visited_on , amount , average_amount
from second_half
where visited_on >= (select min(visited_on) + interval '6 days' from customer)
order by visited_on asc;