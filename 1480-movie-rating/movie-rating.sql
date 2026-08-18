(
    SELECT u.name AS results
    FROM (
        SELECT user_id
        FROM MovieRating
        GROUP BY user_id
        ORDER BY COUNT(*) DESC, user_id ASC
    ) top_user
    JOIN Users u ON top_user.user_id = u.user_id
    ORDER BY (
        SELECT COUNT(*) 
        FROM MovieRating mr 
        WHERE mr.user_id = u.user_id
    ) DESC, u.name ASC
    LIMIT 1
)
UNION ALL
(
    SELECT m.title AS results
    FROM (
        SELECT movie_id, AVG(rating) AS avg_rating
        FROM MovieRating
        WHERE created_at >= '2020-02-01' 
          AND created_at < '2020-03-01'
        GROUP BY movie_id
    ) r
    JOIN Movies m ON r.movie_id = m.movie_id
    ORDER BY r.avg_rating DESC, m.title ASC
    LIMIT 1
);