WITH transactions_consecutive_check AS (
    SELECT user_id,
           transaction_date,
           amount,
           transaction_date - INTERVAL '1 day' * ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date) AS check_consecutive
    FROM transactions
),
consecutive_dates_marked AS (
    SELECT user_id, 
           COUNT(*) AS consecutive_window
    FROM transactions_consecutive_check
    GROUP BY user_id, check_consecutive
    HAVING COUNT(*) >= 3
)
SELECT DISTINCT user_id 
FROM consecutive_dates_marked
ORDER BY user_id;
