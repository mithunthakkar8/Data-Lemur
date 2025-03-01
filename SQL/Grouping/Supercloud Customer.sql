select cc.customer_id
from customer_contracts cc
join products p
on cc.product_id = p.product_id
group by cc.customer_id
having count(distinct p.product_category) = 
(select count(distinct product_category)
from products)
