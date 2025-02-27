WITH activity_summary AS (
  SELECT 
    ab.age_bucket
    , SUM(CASE WHEN a.activity_type = 'send' THEN time_spent ELSE 0 END) AS send_time
    , SUM(CASE WHEN a.activity_type = 'open' THEN time_spent ELSE 0 END) AS open_time
    , SUM(CASE WHEN a.activity_type IN ('send', 'open') THEN time_spent ELSE 0 END) AS total_time
  FROM activities a
  JOIN age_breakdown ab ON a.user_id = ab.user_id
  GROUP BY ab.age_bucket
)
SELECT 
  age_bucket
  , ROUND(send_time * 100.0 / NULLIF(total_time, 0), 2) AS send_perc
  , ROUND(open_time * 100.0 / NULLIF(total_time, 0), 2) AS open_perc
FROM activity_summary;
