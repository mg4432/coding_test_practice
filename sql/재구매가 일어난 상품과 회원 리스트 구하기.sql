SELECT user_id, product_id 
FROM online_sale 
GROUP BY user_id, product_id
HAVING count(user_id, product_id) > 1 
ORDER BY user_id ASC, product_id DESC ;