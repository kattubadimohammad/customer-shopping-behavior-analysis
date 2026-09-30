-- Inventory & Sales Performance Dashboard KPI queries

-- Overall KPIs
SELECT
    SUM(Sales) AS total_sales,
    SUM([Closing Stock]) AS closing_stock,
    SUM([Filled Qty]) * 100.0 / NULLIF(SUM(Demand), 0) AS fill_rate,
    SUM(CASE WHEN [Closing Stock] > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS instock_pct,
    SUM([Filled Qty]) * 100.0 /
      NULLIF(SUM([Filled Qty]) + SUM([Closing Stock]), 0) AS sell_through_pct
FROM inventory_sales_demo;

-- Sales by category
SELECT Category, SUM(Sales) AS sales
FROM inventory_sales_demo
GROUP BY Category
ORDER BY sales DESC;

-- Sales by location
SELECT Location, SUM(Sales) AS sales
FROM inventory_sales_demo
GROUP BY Location
ORDER BY sales DESC;

-- Top products
SELECT Product, SUM(Sales) AS sales, SUM([Closing Stock]) AS closing_stock
FROM inventory_sales_demo
GROUP BY Product
ORDER BY sales DESC;
