Select title, description, rating from film where film_id in (Select film_id from film_category where category_id in (select category_id from category where name = 'Comedy'))
