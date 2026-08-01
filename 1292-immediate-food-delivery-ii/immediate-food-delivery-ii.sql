-- Write your PostgreSQL query statement below



select 
ROUND(
AVG(CASE WHEN order_date = customer_pref_delivery_date then 100.0 else 0.0 end),2) AS immediate_percentage
from Delivery
where(customer_id,order_date) in (
    select customer_id , min(order_date) 
    from Delivery
    group by customer_id
);
