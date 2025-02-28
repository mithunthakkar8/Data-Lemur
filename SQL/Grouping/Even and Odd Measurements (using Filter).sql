WITH measurements_ranked AS (
    SELECT date_trunc('day', measurement_time) AS measurement_day,
           measurement_value,
           ROW_NUMBER() OVER (
               PARTITION BY date_trunc('day', measurement_time) 
               ORDER BY measurement_time
           ) AS rnk
    FROM measurements
)
SELECT measurement_day,
       SUM(measurement_value) FILTER (WHERE rnk % 2 = 1) AS odd_sum,
       SUM(measurement_value) FILTER (WHERE rnk % 2 = 0) AS even_sum
FROM measurements_ranked
GROUP BY measurement_day;
