-- 1
SELECT * FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE address.city_id = "312";


-- 2
SELECT film.film_id, title, description, release_year, rating, special_features, category.name AS genre FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
where category.name = "comedy";


-- 3
SELECT actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;


-- 4
SELECT customer.first_name,customer.last_name, customer.email, address.address FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE store_id = 1 AND address.city_id IN (1, 42, 312, 459);


-- 5
SELECT film.title,film.description,film.release_year,film.special_features FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.rating = "G" 
AND film.special_features LIKE "%behind the scenes%"
AND actor.actor_id = 15;


-- 6
SELECT film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name FROM film
JOIN film_actor on film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
where film.film_id = 369;


-- 7
SELECT film.title, film. description, film.release_year, film.rating, film.special_features, category.name AS genre FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
where category.name = "drama" and rental_rate = 2.99;


-- 8
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN film_actor on film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name ="action" AND actor.first_name = "sandra" AND actor.last_name = "kilmer";