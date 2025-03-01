select order_id
      , case when order_id%2=1 and order_id = 
          (select max(order_id) from orders) 
          then item
        when order_id%2=1 then lead(item) over (order by order_id)
        else lag(item) over (order by order_id) end as item
from orders 
