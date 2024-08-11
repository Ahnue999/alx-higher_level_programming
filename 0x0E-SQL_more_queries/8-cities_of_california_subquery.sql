-- list the cities of california.
SELECT cities.id AS id, cities.name AS name
FROM cities, states
WHERE states.id = cities.id
ORDER BY cities.id
