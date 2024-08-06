-- Desplay the avarage temperature by city ordered by temperature.
SELECT `city`, AVG(`value`) as `avg_temp`
	GROUP BY `city`
	ORDER BY `avg_temp` DESC
