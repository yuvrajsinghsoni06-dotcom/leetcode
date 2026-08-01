WITH TotalUsers AS (
    SELECT COUNT(*) AS total_cnt FROM Users
)
SELECT 
    r.contest_id,
    ROUND(COUNT(r.user_id) * 100.0 / t.total_cnt, 2) AS percentage
FROM Register r, TotalUsers t
GROUP BY r.contest_id, t.total_cnt
ORDER BY percentage DESC, contest_id ASC;