WITH ranked_spends AS (
    SELECT category,
           product,
           SUM(spend) AS total_spend,
           ROW_NUMBER() OVER (PARTITION BY category ORDER BY SUM(spend) DESC) AS spend_rank
    FROM product_spend
    WHERE transaction_date >= DATE '2022-01-01' 
      AND transaction_date < DATE '2023-01-01'
    GROUP BY category, product
)
SELECT category, product, total_spend
FROM ranked_spends
WHERE spend_rank <= 2;
