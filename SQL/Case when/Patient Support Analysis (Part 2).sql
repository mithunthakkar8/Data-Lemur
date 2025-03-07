select round(round(sum(case when call_category is null or call_category = 'n/a'
          then 1 else 0 end),1)*100/count(*),1) as uncategorised_call_pct
from callers
