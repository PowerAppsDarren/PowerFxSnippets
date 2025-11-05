-- =============================================
-- Create basic stored procedure template
-- =============================================

-- Drop stored procedure if it already exists
IF EXISTS (
  SELECT * 
    FROM INFORMATION_SCHEMA.ROUTINES 
   WHERE SPECIFIC_SCHEMA = N'dbo'
     AND SPECIFIC_NAME = N'usp_SayHello' 
)
   DROP PROCEDURE dbo.usp_SayHello
GO

CREATE PROCEDURE dbo.usp_SayHello
	@UserName		varchar(255),
	@FavoriteFood	varchar(255)
AS
	--SELECT 'Hello ' + @UserName + '! I see that you like ' + @FavoriteFood
	SELECT *
	FROM [dbo].[Model]
GO

-- =============================================
-- Example to execute the stored procedure
-- =============================================
EXECUTE dbo.usp_SayHello 
	@UserName = 'Darren', 
	@FavoriteFood = 'Pizza'
GO
