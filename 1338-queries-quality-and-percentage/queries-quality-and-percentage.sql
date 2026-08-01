-- Write your PostgreSQL query statement below
select  query_name,
     ROUND(
        AVG(rating::numeric / position)
        ,2) AS quality,
    ROUND(AVG(CASE WHEN rating < 3 THEN 100.0 ELSE 0.0 END), 2) AS poor_query_percentage
from Queries
group by query_name;
