
DELIMITER $$
DROP PROCEDURE IF EXISTS deleteNotEnabledAccount;
CREATE PROCEDURE deleteNotEnabledAccount ()
BEGIN
	DECLARE finished INTEGER DEFAULT 0;
    DECLARE userID INTEGER DEFAULT 0;
    
	-- declare cursor
	DECLARE notEnabledUserCursor
		CURSOR FOR
			SELECT user_id FROM user WHERE enabled = 0;
	-- declare NOT FOUND handler
    DECLARE CONTINUE HANDLER
    FOR NOT FOUND SET finished = 1;
    
    OPEN notEnabledUserCursor;
    
    deleteUser: LOOP
		FETCH notEnabledUserCursor INTO userID;
        IF finished = 1 THEN
			LEAVE deleteUser;
		END IF;
        SELECT userID;
        DELETE FROM token WHERE user_user_id = userID;
        DELETE FROM user WHERE user_id = userID;
	END LOOP deleteUser;
    
    CLOSE notEnabledUserCursor;
        
END $$
DELIMITER ;

CALL deleteNotEnabledAccount();