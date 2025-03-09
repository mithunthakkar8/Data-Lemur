with monthly_users as (
    select 
        extract(year from event_date) as year,
        extract(month from event_date) as month,
        count(distinct user_id) as number_of_users
    from user_actions
    where event_type in ('sign-in', 'like', 'comment')
    group by extract(year from event_date), extract(month from event_date)
    having extract(year from event_date) = 2022 
    and extract(month from event_date) in (6, 7)
), active_users_processed as (
    select 
        month,
        min(number_of_users) over () as monthly_active_users
    from monthly_users
)
select 
    month,
    monthly_active_users
from active_users_processed
where month = 7;
