/*
   Sunday, January 16, 20226:55:03 PM
   User: 
   Server: .
   Database: TheCryptoYouFindBaby
   Application: 
*/

/* To prevent any potential data loss issues, you should review this script in detail before running it outside the context of the database designer.*/
BEGIN TRANSACTION
SET QUOTED_IDENTIFIER ON
SET ARITHABORT ON
SET NUMERIC_ROUNDABORT OFF
SET CONCAT_NULL_YIELDS_NULL ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
COMMIT
BEGIN TRANSACTION
GO
CREATE TABLE dbo.BABY
	(
	NAME nvarchar(20) NULL,
	HASH_ID nvarchar(200) NOT NULL,
	LEVEL_NUMBER nvarchar(1) NULL,
	TOTAL_SCORE nvarchar(3) NULL,
	DAMAGE_TYPE nvarchar(10) NULL,
	ROLE nvarchar(10) NULL,
	RARITY nvarchar(3) NULL,
	STRENGHT nvarchar(2) NULL,
	DEXTERITY nvarchar(2) NULL,
	VITALITY nvarchar(2) NULL,
	MENTALITY nvarchar(2) NULL,
	GRIT nvarchar(2) NULL,
	STAMINA nvarchar(2) NULL,
	MAIN_STAT nvarchar(2) NULL,
	SUB_STAT nvarchar(2) NULL,
	PRICE_DOLLAR nvarchar(10) NULL,
	PRICE_BABY nvarchar(10) NULL,
	ESTIMATED_PROFIT_BABY nvarchar(10) NULL,
	ESTIMATED_PROFIT_DOLLAR nvarchar(10) NULL,
	PAYBACK nvarchar(5) NULL,
	ROI nvarchar(2) NULL,
	LEVEL_UP nvarchar(1) NULL,
	URL_BUY nvarchar(200) NULL
	)  ON [PRIMARY]
GO
ALTER TABLE dbo.BABY ADD CONSTRAINT
	PK_BABY PRIMARY KEY CLUSTERED 
	(
	HASH_ID
	) WITH( STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

GO
ALTER TABLE dbo.BABY SET (LOCK_ESCALATION = TABLE)
GO
COMMIT
select Has_Perms_By_Name(N'dbo.BABY', 'Object', 'ALTER') as ALT_Per, Has_Perms_By_Name(N'dbo.BABY', 'Object', 'VIEW DEFINITION') as View_def_Per, Has_Perms_By_Name(N'dbo.BABY', 'Object', 'CONTROL') as Contr_Per 