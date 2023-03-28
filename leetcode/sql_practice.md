#### 595. Big Countries
Write an SQL query to report the name, population, and area of the big countries.
Return the result table in any order.
<pre>
SELECT name,population,area
FROM world
WHERE area >=3000000 OR population>=25000000;
</pre>

#### 183. Customers Who Never Order
Write an SQL query to report all customers who never order anything.
Return the result table in any order.\

##### 3 ways solutions
###### NOT EXISTS
<pre>SELECT Name AS Customers
FROM Customers
WHERE NOT EXISTS
(SELECT CustomerID FROM Orders WHERE Customers.ID=Orders.CustomerID);</pre>
###### NOT IN
<pre>SELECT Name AS Customers FROM Customers  WHERE Id NOT IN (SELECT CustomerId FROM Orders);</pre>
###### LEFT JOIN
<pre>SELECT  name Customers
FROM customers
LEFT JOIN orders 
ON customers.id = orders.customerId
WHERE customerId IS NULL</pre>
