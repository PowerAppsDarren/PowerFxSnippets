USE [master];
GO

DECLARE @DB_USER		VARCHAR(50)		= 'Student01';
DECLARE @DB_PASSWORD	VARCHAR(50)		= 'P@ssword134#';
DECLARE @DB_NAME		NVARCHAR(100)	= 'MyFirstDB';
DECLARE @SQL_STRING		NVARCHAR(1000);

-- Create a new login on the server.
CREATE LOGIN 
	@DB_USER									-- NEW LOGIN HERE
	WITH PASSWORD = @DB_PASSWORD;				-- PASSWORD HERE
GO

-- =======================================
-- THE DATABASE TO USE!
-- =======================================
USE MyFirstDB;									-- SPECIFY DB NAME
GO

-- Create a new SQL Server user.
CREATE USER 
	LOGIN_NAME									-- NEW LOGIN HERE
	FOR LOGIN 
	LOGIN_NAME									-- NEW LOGIN HERE
	WITH DEFAULT_SCHEMA = [dbo];				-- DIFFERENT SCHEMA?
GO

-- Add the user to the dbo role.
ALTER ROLE 
	[db_reader]
	--[db_owner]									-- SHOULD THEY REALLY BE A DBO?
	ADD MEMBER LOGIN_NAME;
GO

ALTER ROLE 
	[db_writer]
	--[db_owner]									-- SHOULD THEY REALLY BE A DBO?
	ADD MEMBER LOGIN_NAME;
GO