-- Write your PostgreSQL query statement below
SELECT p.product_name , 
s.year , price 
from Sales s 
join Product p
on s.product_id = p.product_id;
