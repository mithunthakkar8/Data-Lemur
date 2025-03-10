with OrderedData as (
    select searches
        , sum(num_users) over () as total_users
        , sum(num_users) over (order by searches) as cumulative_users
    from search_frequency
)
select round(avg(searches),1) as median
from OrderedData
where cumulative_users between total_users*1.0/2
    and total_users*1.0/2+1 

