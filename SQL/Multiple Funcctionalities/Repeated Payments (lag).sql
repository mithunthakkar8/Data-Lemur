with timestamps_organized as (
select transaction_id
    ,  merchant_id
    , credit_card_id
    , amount
    , transaction_timestamp
    , lag(transaction_timestamp) over 
    (partition by merchant_id
    , credit_card_id
    , amount order by transaction_timestamp) as previous_transaction_timestamp
from transactions
), 

repeated_transactions_count as
(
select count(*) as count_repeat_payments
from timestamps_organized
where extract (epoch from (transaction_timestamp 
    - previous_transaction_timestamp))/60 <= 10
group by merchant_id
    , credit_card_id
    , amount)
    
select sum(count_repeat_payments) as payment_count
from repeated_transactions_count
