-- 1. Check total number of orders
SELECT COUNT(*) AS total_orders
FROM orders;


-- 2. Calculate revenue by product
SELECT
    product,
    SUM(total_amount) AS total_revenue
FROM orders
GROUP BY product
ORDER BY total_revenue DESC;


-- 3. Calculate total spending by customer
SELECT
    customer_name,
    SUM(total_amount) AS total_spent
FROM orders
GROUP BY customer_name
ORDER BY total_spent DESC;


-- 4. Count orders placed by each customer
SELECT
    customer_name,
    COUNT(*) AS total_orders
FROM orders
GROUP BY customer_name
ORDER BY total_orders DESC;