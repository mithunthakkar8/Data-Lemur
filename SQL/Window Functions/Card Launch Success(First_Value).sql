select distinct card_name
      , first_value(issued_amount)
      over (partition by card_name 
      order by MAKE_DATE(issue_year, issue_month, 1)) as issued_amount
from monthly_cards_issued
order by issued_amount desc


