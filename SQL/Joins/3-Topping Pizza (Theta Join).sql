select 
    pt1.topping_name || ',' || pt2.topping_name || ',' || pt3.topping_name as pizza
    , pt1.ingredient_cost + pt2.ingredient_cost + pt3.ingredient_cost as total_cost
from pizza_toppings pt1
join pizza_toppings pt2 on pt1.topping_name < pt2.topping_name
join pizza_toppings pt3 on pt2.topping_name < pt3.topping_name
order by total_cost desc
    , pt1.topping_name, pt2.topping_name, pt3.topping_name;
