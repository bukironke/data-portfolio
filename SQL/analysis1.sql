use sql_analysis1;
#Query to display all the information of all 'USB-C Charging Cable' orders
SELECT * FROM salesda WHERE Product = "USB-C Charging Cable";
#Query to display all the purchases from NYC
SELECT * FROM salesda WHERE `Purchase Address` LIKE '%New York City%';
#Query to display all the orders made AFTER December 1st 2019
SELECT * FROM salesda WHERE DATE(`Order Date`) > '2019-12-01';
#Query to find total sales for each product in dataset
SELECT Product, SUM(Sales) AS total_sales
FROM salesda
GROUP BY Product
ORDER BY total_sales DESC;
#Query to display the average price sale for each product
SELECT Product, AVG (`Price Each`) as average_price
FROM salesda
GROUP BY Product
ORDER BY average_price DESC;
#Query to display the top products by quantity ordered + to show the top 5
SELECT Product, SUM(`Quantity Ordered`) as total_quantity_ordered
FROM salesda
GROUP by Product
Order by total_quantity_ordered DESC
LIMIT 5;
#Cleaning query - checking to identify any missing values
SELECT
    COUNT(*) AS total_rows,
    SUM(CASE WHEN `Product` IS NULL THEN 1 ELSE 0 END) AS missing_product,
    SUM(CASE WHEN `Quantity Ordered` IS NULL THEN 1 ELSE 0 END) AS missing_quantity,
    SUM(CASE WHEN `Price Each` IS NULL THEN 1 ELSE 0 END) AS missing_price_each,
    SUM(CASE WHEN `Order Date` IS NULL THEN 1 ELSE 0 END) AS missing_order_date,
    SUM(CASE WHEN `Purchase Address` IS NULL THEN 1 ELSE 0 END) AS missing_purchase_address,
    SUM(CASE WHEN `Month` IS NULL THEN 1 ELSE 0 END) AS missing_month,
    SUM(CASE WHEN `Sales` IS NULL THEN 1 ELSE 0 END) AS missing_sales,
    SUM(CASE WHEN `City` IS NULL THEN 1 ELSE 0 END) AS missing_city,
    SUM(CASE WHEN `Hour` IS NULL THEN 1 ELSE 0 END) AS missing_hour
    FROM salesda;
    