-- Write your PostgreSQL query statement below
select
to_char(trans_date, 'YYYY-MM') as month , 
country,
count(*) as Trans_count,
count(case when state = 'approved' then 1 end) as approved_count,
sum(amount) as trans_total_amount,
coalesce(sum(amount) filter (where state = 'approved'),0) as approved_total_amount
from transactions
group by to_char(trans_date, 'YYYY-MM') , country;

