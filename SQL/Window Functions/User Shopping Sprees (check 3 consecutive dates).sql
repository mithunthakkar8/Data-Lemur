with transactions_consecutive_check as (
select *
      , transaction_date - Interval '1 day' * row_number() 
          over (partition by user_id order by transaction_date) as check_consecutive
from transactions),
consecutive_dates_marked as (
select user_id    
    , amount
    , transaction_date
    , count(*) over (partition by check_consecutive) as consecutive_window
from transactions_consecutive_check
)
select distinct user_id    
from consecutive_dates_marked
where consecutive_window >= 3
order by user_id
