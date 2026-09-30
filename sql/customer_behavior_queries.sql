-- Customer Shopping Behavior Analysis
-- Public educational dataset

-- 1. Overall KPIs
SELECT COUNT(*) AS transactions,
       SUM(purchase_amount_usd) AS total_sales,
       AVG(purchase_amount_usd) AS average_purchase,
       AVG(review_rating) AS average_rating
FROM customer_shopping_behavior;

-- 2. Sales by category
SELECT category, SUM(purchase_amount_usd) AS sales, COUNT(*) AS transactions
FROM customer_shopping_behavior
GROUP BY category
ORDER BY sales DESC;

-- 3. Subscription mix
SELECT subscription_status, COUNT(*) AS customers, AVG(purchase_amount_usd) AS avg_purchase
FROM customer_shopping_behavior
GROUP BY subscription_status;

-- 4. Top locations
SELECT location, SUM(purchase_amount_usd) AS sales
FROM customer_shopping_behavior
GROUP BY location
ORDER BY sales DESC;

-- 5. Top products
SELECT item_purchased, COUNT(*) AS purchases, SUM(purchase_amount_usd) AS sales
FROM customer_shopping_behavior
GROUP BY item_purchased
ORDER BY sales DESC;

-- 6. Discount usage
SELECT discount_applied, COUNT(*) AS transactions, AVG(purchase_amount_usd) AS avg_purchase
FROM customer_shopping_behavior
GROUP BY discount_applied;

-- 7. Purchase frequency
SELECT frequency_of_purchases, COUNT(*) AS customers, AVG(purchase_amount_usd) AS avg_purchase
FROM customer_shopping_behavior
GROUP BY frequency_of_purchases
ORDER BY customers DESC;

-- 8. Payment method mix
SELECT payment_method, COUNT(*) AS transactions, SUM(purchase_amount_usd) AS sales
FROM customer_shopping_behavior
GROUP BY payment_method
ORDER BY sales DESC;

-- 9. Gender analysis
SELECT gender, COUNT(*) AS customers, SUM(purchase_amount_usd) AS sales
FROM customer_shopping_behavior
GROUP BY gender;

-- 10. High-value customers
SELECT customer_id, SUM(purchase_amount_usd) AS total_spend, COUNT(*) AS purchases
FROM customer_shopping_behavior
GROUP BY customer_id
ORDER BY total_spend DESC;
