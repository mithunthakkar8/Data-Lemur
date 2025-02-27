with salaries_ranked as (
select salary
  , dense_rank() over (order by salary desc) as rnk 
from employee
)
select distinct salary
from salaries_ranked
where rnk = 2
