-- Desplay the avarage temperature by city ordered by temperature.
USE hbtn_0c_0
SELECT `city`, AVG(`value`) as `avg_temp`
	GROUP BY `city`
	ORDER BY `avg_temp` DESC
