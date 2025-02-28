with salaries_ranked as (
select e.name
  , d.department_name
  , e.salary
  , dense_rank() over (partition by d.department_id order by e.salary desc) as rnk
from employee e
join department d
on e.department_id = d.department_id
)
select name
  , department_name
  , salary
from salaries_ranked
where rnk <= 3
order by department_name,salary desc, name
