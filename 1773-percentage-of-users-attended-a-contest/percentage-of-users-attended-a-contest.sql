select
r.contest_id,
round(
(count(r.contest_id)* 100.0 / (select count(*) from Users)) 
, 2) as percentage
from
Users as u,
Register as r
where
u.user_id = r.user_id
group by r.contest_id
order by
percentage desc,
contest_id asc;