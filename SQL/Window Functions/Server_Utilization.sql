with time_calc as (
select server_id
    , session_status
    , sum(extract(epoch from status_time)) as time_in_epoch
from server_utilization
group by server_id, session_status),
time_lapsed as (
select (time_in_epoch - lag(time_in_epoch) over 
      (partition by server_id order by session_status)) as total_lapsed_time
from time_calc)
select round(sum(total_lapsed_time)/86400,0) as total_uptime_days
from time_lapsed
