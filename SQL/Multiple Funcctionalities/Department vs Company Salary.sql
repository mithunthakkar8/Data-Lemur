with average_salaries as (
select e.department_id
      , to_char(s.payment_date, 'MM-YYYY') as payment_date
      , avg(s.amount) over (partition by e.department_id) as avg_dept_salary
      , avg(s.amount) over () as company_avg_salary
from employee e
join salary s
on e.employee_id = s.employee_id
where s.payment_date<= '03-31-2024' and s.payment_date>='03-01-2024'
)
select distinct department_id
      , payment_date
      , case when avg_dept_salary<company_avg_salary then 'lower'
            when avg_dept_salary>company_avg_salary then 'higher'
            else 'same' end as comparison
from average_salaries
