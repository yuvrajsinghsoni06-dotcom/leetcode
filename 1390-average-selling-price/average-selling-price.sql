-- Write your PostgreSQL query statement below
select p.product_id,
ROUND(
    coalesce(
        sum(
            p.price * u.units):: numeric/NUllif(sum(u.units),0)
            ,0.00)
,2)  as average_price
from Prices p
left join UnitsSold u on p.product_id = u.product_id
and u.purchase_date BETWEEN P.start_date and p.end_date
group by p.product_id;
