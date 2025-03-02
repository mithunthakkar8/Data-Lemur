with transactions_counted as (
select transaction_date
      , user_id
      , count(product_id) over 
          (partition by user_id, transaction_date
          ) as purchase_count
      , row_number() over 
          (partition by user_id 
          order by transaction_date desc) as rnk
from user_transactions
)
select transaction_date
      , user_id
      , purchase_count
from transactions_counted
where rnk = 1
order by transaction_date 
