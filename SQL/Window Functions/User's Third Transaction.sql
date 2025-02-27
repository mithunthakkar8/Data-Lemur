with transactions_ranked as (
select user_id
  , spend
  , transaction_date
  , row_number() over (partition by user_id order by transaction_date) as rnk
from transactions)
select user_id
  , spend
  , transaction_date
from transactions_ranked
where rnk = 3

