-- 1  
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE language like "%slovene%" 
ORDER BY languages.percentage desc;

-- 2
SELECT countries.name, COUNT(cities.name) FROM countries
JOIN cities ON countries.id = cities.country_id
Group BY countries.name
order by count(*)desc;

-- 3
SELECT countries.name, cities.population FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name like "%mexico%" AND cities.population > 500000;

-- 4
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY percentage desc;

-- 5
SELECT name, surface_area, population FROM countries
WHERE surface_area < 501 and population > 100000;


-- 6
SELECT name, government_form, capital, life_expectancy FROM countries
WHERE government_form LIKE "%monarchy" AND capital > 200 AND life_expectancy > 75;


-- 7
SELECT countries.name AS country_name, cities.name AS city_name, cities.district, cities.population AS population FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = "argentina" AND district = "buenos aires" and cities.population > 500000;


-- 8
SELECT region, COUNT(name) AS countries FROM countries
GROUP BY region
ORDER BY count(*)DESC;

