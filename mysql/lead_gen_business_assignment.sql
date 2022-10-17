-- 1 -- complete
SELECT sum(amount), monthname(charged_datetime) FROM billing
WHERE charged_datetime >= '2012/03/01' AND charged_datetime <= '2012/03/31';


-- 2 -- complete
SELECT clients.client_id, sum(amount) AS total_revenue FROM clients
JOIN billing ON clients.client_id = billing.client_id
WHERE clients.client_id = 2;


-- 3 -- complete
SELECT sites.client_id, domain_name AS website FROM clients
JOIN sites ON clients.client_id = sites.client_id
WHERE sites.client_id = 10;


-- 4 -- complete
SELECT sites.client_id, monthname(sites.created_datetime) AS month , year(sites.created_datetime) AS year FROM clients
JOIN sites ON clients.client_id = sites.client_id
WHERE sites.client_id IN (1 , 20)
ORDER BY sites.client_id;


-- 5 -- complete
SELECT sites.domain_name AS website, count(leads.leads_id) AS leads  FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE registered_datetime >= '2011/01/01' AND registered_datetime <= '2011/02/15'
GROUP BY clients.client_id;


-- 6 -- complete
SELECT concat(clients.first_name,' ', clients.last_name) AS client_name, count(leads.leads_id) AS leads  FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE registered_datetime >= '2011/01/01' AND registered_datetime <= '2011/12/31'
GROUP BY clients.client_id;


-- 7 -- complete
SELECT concat(clients.first_name,' ', clients.last_name) AS client_name, count(leads.leads_id) AS leads, monthname(leads.registered_datetime) AS month_generated  FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE registered_datetime >= '2011/01/01' AND registered_datetime <= '2011/6/30'
GROUP BY leads.registered_datetime;


-- 8a -- complete
SELECT concat(clients.first_name,' ', clients.last_name) AS client_name, count(leads.leads_id) AS leads, domain_name AS website FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE registered_datetime >= '2011/01/01' AND registered_datetime <= '2011/12/31'
GROUP BY sites.domain_name
ORDER BY clients.client_id, domain_name;


-- 8b -- complete
SELECT concat(clients.first_name,' ', clients.last_name) AS client_name, domain_name AS website, count(leads.leads_id) FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY sites.domain_name
ORDER BY clients.client_id, domain_name;


-- 9a
SELECT concat(clients.first_name,' ', clients.last_name) AS client_name, sum(billing.amount), MONTH(billing.charged_datetime), YEAR(charged_datetime) FROM clients
JOIN billing ON clients.client_id = billing.client_id
GROUP BY monthname(billing.charged_datetime)
order by clients.client_id, charged_datetime;


select billing_id, concat(clients.first_name,' ', clients.last_name) AS client_name, amount, month(charged_datetime), year(charged_datetime) from billing
JOIN clients ON billing.client_id = clients.client_id
order by billing_id, month(charged_datetime);
-- where 
-- 	exists ( select client_id, sum(amount) FROM billing
--     order by billing.client_id);




-- this one i think if i can sub query it
select  clients.first_name, amount,  MONTH(charged_datetime) AS month, YEAR(charged_datetime) AS year from billing
join clients on billing.client_id = clients.client_id
order by billing.client_id, charged_datetime asc;




select billing_id, clients.first_name, amount,  MONTH(charged_datetime) AS month_billed, YEAR(charged_datetime) AS year_billed from billing
join clients on billing.client_id = clients.client_id
WHERE MONTH(billing.charged_datetime)  IN (
	SELECT MONTH(charged_datetime)
	FROM billing
    GROUP BY MONTH(charged_datetime) )
    order by billing.client_id, charged_datetime asc; 
    
    
  


select *
From (select billing_id, concat(clients.first_name,' ', clients.last_name) AS client_name, amount,  MONTH(charged_datetime) AS month_charged, YEAR(charged_datetime) AS year_charged from billing
join clients on billing.client_id = clients.client_id
order by billing.client_id, charged_datetime asc) a
where month_charged in (select month(charged_datetime) from billing group by month(charged_datetime) );





-- 9b




-- 10 -- complete
SELECT concat(clients.first_name,' ', clients.last_name) AS client_name, group_concat(replace(replace(domain_name, '\\', '\\\\'), '|', '\\|') SEPARATOR '/')
 AS website FROM clients
left JOIN sites ON clients.client_id = sites.client_id
group by client_name
order by clients.client_id;






