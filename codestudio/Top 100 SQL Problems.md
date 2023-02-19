##### 1. IMDb Rating
From the IMDb dataset, print the **title** and **rating** of those movie which have a **genre** starting from **'C'** released in in 2014 with a budget higher than 4 crore.(Download the dataset from console)

<pre>
SELECT title, rating
FROM imdb JOIN genre ON imdb.movie_id = genre.movie_id
WHERE budget > 40000000 AND title LIKE '%2014%' AND genre LIKE 'C%';
</pre>
##### 2. IMDb Metacritic Rating
Print the title and ratings of the movies released in 2012 whose metacritic rating is more than 60 and Domestic collections exceed 10 crores.(Download the dataset from console)
<pre>
SELECT  title, rating
FROM imdb
JOIN earning
ON imdb.movie_id = earning.movie_id
WHERE metacritic > 60 AND domestic > 100000000 AND title LIKE '%2012%';
</pre>
