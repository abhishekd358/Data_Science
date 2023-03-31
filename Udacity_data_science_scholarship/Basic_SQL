--1 (SELECT -> Use to Display Data, * -> extract all information) 
/* Getting all details from the Order table from the Parch & Posey Database*/
SELECT *
FROM orders;

--2 
/* Getting specific Columns details as id, account_id, and occurred_at from the Order table*/
SELECT id,account_id,standard_qty
FROM orders;

--3 (LIMIT -> LIMIT always at end of query)
/* Displays all the data in the occurred_at, account_id, and channel columns of the web_events table,
 and limits the output to only the first 15 rows.*/
SELECT occurred_at,
       account_id,
        channel
FROM web_events;

--3 (ORDER BY -> Sort the result data in ascending and decending order. By Default it set to ASC ascending order.)
/*Write a query to return the 10 earliest orders in the orders table. Include the id, occurred_at, and total_amt_usd.*/
SELECT id,
       occurred_at,
       total_amt_usd
FROM orders
LIMIT 10;

/*Write a query to return the top 5 orders in terms of the largest total_amt_usd. Include the id, account_id, and total_amt_usd.*/
SELECT id,
       occurred_at,
       total_amt_usd
FROM orders
ORDER BY total_amt_usd DESC
LIMIT 5;

/*Write a query to return the lowest 20 orders in terms of the smallest total_amt_usd. Include the id, account_id, and total_amt_usd.*/
SELECT id,
       occurred_at,
       total_amt_usd
FROM orders
ORDER BY total_amt_usd ASC
LIMIT 20;

--ORDER BY Part II -> WE can use DESC|ASC on specific columns. Let in below example the DESC applied to total_amt_usd column 
but eventually the data of account_id column change respective to total_amt_usd column because DESC applied to only total_amt_usd.*/
SELECT  account_id,
        total_amt_usd
FROM orders
ORDER By total_amt_usd DESC, account_id;

/*Write a query that displays the order ID, account ID, and total dollar amount for all the orders, 
sorted first by the account ID (in ascending order it set by default), and then by the total dollar amount (in descending order).*/
SELECT  id,
        account_id,
        total_amt_usd
FROM orders
ORDER By account_id, total_amt_usd DESC;
/* write a query that again displays order ID, account ID, and total dollar amount for each order, but this time 
sorted first by total dollar amount (in descending order), and then by account ID (in ascending order it set by default).*/
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd DESC, account_id;

/*Compare the results of these two queries above. How are the results different when you switch the column you sort on first? 
In query #1, all of the orders for each account ID are grouped together, and then within each of those groupings,
 the orders appear from the greatest order amount to the least. 
In query #2, since you sorted by the total dollar amount first, the orders appear from greatest to least regardless of which account ID they were from. 
Then they are sorted by account ID next.*/

--4 (WHERE -> Filter the data.)
/*Pulls the first 5 rows and all columns from the orders table that have a dollar amount of gloss_amt_usd greater than or equal to 1000.*/
SELECT *
FROM orders
WHERE gloss_amt_usd >= 1000
LIMIT 5;

/* Pulls the first 10 rows and all columns from the orders table that have a total_amt_usd less than 500.*/
SELECT *
FROM orders
WHERE gloss_amt_usd <= 500
LIMIT 10;

--*WHERE Part II -> WHERE with Non-Numeric Data
/*WHERE with non-numeric data fields, we use the LIKE, NOT, or IN operators. */

/*Filter the accounts table to include the company name, website, and the primary point of contact (primary_poc) just 
for the Exxon Mobil company in the accounts table.*/
SELECT name,
       website
       primary_poc
FROM accounts
WHERE name = 'Exxon Mobil';

--5 (Arithmetic Operations)
/*Create a column that divides the standard_amt_usd by the standard_qty to find the unit price for standard paper for each order.
Limit the results to the first 10 orders, and include the id and account_id fields.*/



/*Write a query that finds the percentage of revenue that comes from poster paper for each order. You will need to use only the columns that end with _usd.
(Try to do this without using the total column.) Display the id and account_id fields also. NOTE - you will receive an error with the correct solution to this question.
This occurs because at least one of the values in the data creates a division by zero in your formula. There are ways to better handle this.
For now, you can just limit your calculations to the first 10 orders, as we did in question #1, and you'll avoid that set of data that causes the problem.*/

--6 (Introduction to Logical Operators)
/*LIKE -> allows you to perform operations similar to using WHERE and =, but for cases when you might not know exactly what you are looking for.
IN -> allows you to perform operations similar to using WHERE and =, but for more than one condition.
NOT -> is used with IN and LIKE to select all of the rows NOT LIKE or NOT IN a certain condition.
AND & BETWEEN -> allow you to combine operations where all combined conditions must be true.
OR -> you to combine operations where at least one of the combined conditions must be true.*/

/*All the companies whose names start with 'C'.*/
SELECT *
FROM accounts
WHERE name = 'c%';

/*All companies whose names contain the string 'one' somewhere in the name.*/
SELECT name
FROM accounts
WHERE name LIKE '%one%';

/*All companies whose names end with 's'.*/
SELECT name
FROM accounts
WHERE name LIKE '%s';

--7 (IN)
/*Use the accounts table to find the account name, primary_poc, and sales_rep_id for Walmart, Target, and Nordstrom.*/
SELECT name, 
       primary_poc,
       sales_rep_id
FROM accounts
WHERE name IN ('Wallmart', 'Target', 'Nordstorm');


/*Use the web_events table to find all information regarding individuals who were contacted via the channel of organic or adwords*/
SELECT *
FROM web_events
WHERE channel IN ('organic', 'adwords');

--8 (NOT)
/*Use the accounts table to find the account name, primary poc, and sales rep id for all stores except Walmart, Target, and Nordstrom.*/
SELECT name, 
       primary_poc,
       sales_rep_id
FROM accounts
WHERE name NOT IN ('Wallmart', 'Target', 'Nordstorm');

/*Use the web_events table to find all information regarding individuals who were contacted via any method except using organic or adwords methods.*/

--9 (AND & BETWEEN)
/*AND -> used within a WHERE statement to consider more than one logical clause at a time.
BETWEEN -> used to select values within a given range*/

/*Write a query that returns all the orders where the standard_qty is over 1000, the poster_qty is 0, and the gloss_qty is 0.*/
SELECT *
FROM orders
WHERE standard_qty > 1000 AND poster_qty = 0 AND gloss_qty = 0;

/*Using the accounts table, find all the companies whose names do not start with 'C' and end with 's'.*/
SELECT name
FROM accounts
WHERE name NOT LIKE 'C%' AND name LIKE '%s';

/*Use the web_events table to find all information regarding individuals who were contacted
 via the organic or adwords channels, and started their account at any point in 2016, sorted from newest to oldest.*/
 SELECT *
 WHERE channels IN ('organic', 'adwords') occurred_at BETWEEN '2016-01-01' AND '2017-01-01'
 FROM web_events
ORDER BY ocuurred_at DESC;

--10 (OR -> used with WHERE to include rows where either condition is true)
/*Find list of orders ids where either gloss_qty or poster_qty is greater than 4000. Only include the id field in the resulting table.*/
SELECT id
FROM orders
WHERE gloss_qty > 4000 or poster_qty > 4000;

/*Write a query that returns a list of orders where the standard_qty is zero and either the gloss_qty or poster_qty is over 1000.*/
SELECT *
FROM orders
WHERE standard_qty = 0 AND (gloss_qty > 1000 OR poster_qty > 1000);

/*Find all the company names that start with a 'C' or 'W', and the primary contact contains 'ana' or 'Ana', but it doesn't contain 'eana'.*/
SELECT *
FROM accounts
WHERE (name LIKE 'C%' OR name LIKE 'W%') 
           AND ((primary_poc LIKE '%ana%' OR primary_poc LIKE '%Ana%') 
           AND primary_poc NOT LIKE '%eana%');






