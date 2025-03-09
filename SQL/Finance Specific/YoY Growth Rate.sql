with yearly_spends as (
select extract(year from transaction_date) as spend_year
  , product_id
  , sum(spend) as total_spend
from user_transactions 
group by extract(year from transaction_date), 
  product_id)
select spend_year
  , product_id
  , total_spend as current_year_spend
  , lag(total_spend) over (partition by product_id order by spend_year) as previous_year_spend
  , round((total_spend/lag(total_spend) over (partition by product_id order by spend_year)-1)*100,2) as yoy_rate
from yearly_spends
order by product_id, spend_year
