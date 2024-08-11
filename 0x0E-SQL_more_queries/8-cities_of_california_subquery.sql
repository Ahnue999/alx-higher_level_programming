-- list the cities of california.
SELECT cities.id AS id, cities.name AS name
FROM cities, states
WHERE states.name = california
ORDER BY cities.id
