SELECT 
    pt1.topping_name || ',' || pt2.topping_name || ',' || pt3.topping_name AS pizza,
    pt1.ingredient_cost + pt2.ingredient_cost + pt3.ingredient_cost AS total_cost
FROM pizza_toppings pt1
JOIN pizza_toppings pt2 ON pt1.topping_name < pt2.topping_name
JOIN pizza_toppings pt3 ON pt2.topping_name < pt3.topping_name
ORDER BY total_cost DESC, pt1.topping_name, pt2.topping_name, pt3.topping_name;
