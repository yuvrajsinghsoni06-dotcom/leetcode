WITH mount AS (
    SELECT 
        visited_on, 
        SUM(amount) AS daily_expense 
    FROM customer 
    GROUP BY visited_on
),
second_half AS (
    SELECT 
        visited_on,
        SUM(daily_expense) OVER (
            ORDER BY visited_on 
            RANGE BETWEEN INTERVAL '6 days' PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(
            AVG(daily_expense) OVER (
                ORDER BY visited_on 
                RANGE BETWEEN INTERVAL '6 days' PRECEDING AND CURRENT ROW
            ), 2
        ) AS average_amount
    FROM mount
)
SELECT visited_on, amount, average_amount
FROM second_half
WHERE visited_on >= (SELECT MIN(visited_on) + INTERVAL '6 days' FROM customer)
ORDER BY visited_on ASC;