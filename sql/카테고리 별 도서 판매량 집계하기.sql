SELECT A.category, SUM(B.sales) AS total_sales
FROM book A 
    JOIN book_sales B ON A.book_id = B.book_id 
WHERE B.sales_date between '2022-01-01' AND '2022-01-31'
GROUP BY A.category 
ORDER BY category ASC ;