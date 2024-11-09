

CREATE TABLE dbo.ModelTable(
	ID					uniqueidentifier				NOT NULL,
	IsActive			bit								NULL,
	Name				nvarchar(255)					NULL,
	CreatedOn			datetime						NULL,
	CreatedBy			nvarchar(255)					NULL,
	LastModifiedOn		datetime						NULL,
	LastModifiedBy		nvarchar(255)					NULL,
	Notes				nvarchar(max)					NULL,

	CONSTRAINT PK_ModelTable 
	PRIMARY KEY CLUSTERED (
		ID ASC
	)

	WITH (
		STATISTICS_NORECOMPUTE = OFF, 
		IGNORE_DUP_KEY = OFF, 
		OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON PRIMARY
	) ON PRIMARY TEXTIMAGE_ON PRIMARY
GO

ALTER TABLE dbo.ModelTable 
	ADD  CONSTRAINT DF_ModelTable_ID  
	DEFAULT (newid()) FOR ID
GO

ALTER TABLE dbo.ModelTable 
	ADD  CONSTRAINT DF_ModelTable_LastModifiedOn  
	DEFAULT (getdate()) FOR LastModifiedOn
GO

ALTER TABLE dbo.ModelTable 
	ADD  CONSTRAINT DF_ModelTable_CreatedOn  
	DEFAULT (getdate()) FOR CreatedOn
GO


