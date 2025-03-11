select pt1.topping_name 
      || ',' || pt2.topping_name 
      || ',' || pt3.topping_name 
        as pizza
      , pt1.ingredient_cost 
      + pt2.ingredient_cost 
      + pt3.ingredient_cost 
        as total_cost
from pizza_toppings pt1
cross join pizza_toppings pt2
cross join pizza_toppings pt3
where pt1.topping_name < pt2.topping_name
 and pt2.topping_name < pt3.topping_name
order by pt1.ingredient_cost 
      + pt2.ingredient_cost 
      + pt3.ingredient_cost desc, 
      pt1.topping_name 
      || ',' || pt2.topping_name 
      || ',' || pt3.topping_name 
