-- Write your PostgreSQL query statement below
select product_name, sum(o.unit) as unit
from products p
inner join orders o on p.product_id = o.product_id
where cast(order_date as varchar) like '2020-02-%'
group by product_name
having sum(o.unit) >= 100;

