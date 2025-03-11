select case when a.user_id is not null then a.user_id
          else dp.user_id end as user_id
      , case when a.status = 'NEW' 
          and dp.paid is not null then 'EXISTING'
          when dp.paid is null then 'CHURN'
          when a.status = 'EXISTING'
          and dp.paid is not null then 'EXISTING'
          when a.status = 'CHURN'
          and dp.paid is not null then 'RESURRECT'
          when a.status = 'RESURRECT'
          and dp.paid is not null then 'EXISTING'
          when a.status = 'RESURRENT'
          and dp.paid is null then 'CHURN' 
          when a.user_id is null then 'NEW' end as new_status
from advertiser a 
full outer join daily_pay dp
on a.user_id = dp.user_id
order by user_id
