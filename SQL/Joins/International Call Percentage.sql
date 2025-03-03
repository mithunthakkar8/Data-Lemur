with phone_calls_info as (
select pc.caller_id
      , pc.receiver_id
      , pc.call_time
      , pi1.country_id as caller_country_id
      , pi1.network as caller_network
      , pi1.phone_number as caller_phone_number
      , pi2.country_id as receiver_country_id
      , pi2.network as receiver_network
      , pi2.phone_number as receiver_phone_number
from phone_calls pc
join phone_info pi1
on pc.caller_id = pi1.caller_id
join phone_info pi2
on pc.receiver_id = pi2.caller_id)
select round((round(sum(case when caller_country_id <> receiver_country_id 
        then 1 else 0 end),2)*100)/count(*), 1) as international_calls_pct
from phone_calls_info
