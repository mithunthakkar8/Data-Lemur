select round(round(sum(case when signup_action = 'Confirmed' then 1 else 0 end),2)
      /count(distinct user_id),2) as confirm_rate
from emails e
left join texts t
on e.email_id = t.email_id
