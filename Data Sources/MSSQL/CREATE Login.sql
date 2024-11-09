USE [master]
GO

CREATE 
	LOGIN [Kurtaroo] 
	WITH PASSWORD=N'p@ssw00rd1869', 
	DEFAULT_DATABASE=[master], 
	CHECK_EXPIRATION=OFF, 
	CHECK_POLICY=OFF
GO

USE [SampleDB]
GO

CREATE USER [Kurtaroo] 
	FOR LOGIN [Kurtaroo]
GO

USE [SampleDB]
GO

ALTER ROLE [db_owner] ADD MEMBER [Kurtaroo]
GO
