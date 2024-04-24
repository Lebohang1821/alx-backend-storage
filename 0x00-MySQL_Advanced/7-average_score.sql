-- Average score
--
delimiter //
CREATE PROCEDURE ComputeAverageScoreForUser (
	IN user_id INT
)
BEGIN
	UPDATE users
	SET average_score = (SELECT SUM(score) / COUNT(*)
   						 FROM corrections AS c
   						 WHERE c.user_id = user_id)
	WHERE id = user_id;
END;
//
