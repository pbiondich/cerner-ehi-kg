# EHI_TABLE_STMT_GTTP

> "Used to store parent/child table relationships and the SQL statements that will be used to extract activity data for EHI." ;

**Description:** EHI TABLE STATEMENT GLOBAL TEMPORARY TABLE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_COL_STR` | VARCHAR(200) | NOT NULL |  | Store Child column name |
| 2 | `CHILD_TABLE` | VARCHAR(30) | NOT NULL |  | The table that is the child table of this record |
| 3 | `COL_LIST` | VARCHAR(2000) |  |  | The list of columns to be queried |
| 4 | `DRR_CHILD_TABLE` | VARCHAR(30) | NOT NULL |  | The table that is the DRR child table of this record |
| 5 | `DRR_PARENT_TABLE` | VARCHAR(30) | NOT NULL |  | The table that is the DRR parent to this record |
| 6 | `DUP_IND` | DOUBLE |  |  | Flag duplicate records |
| 7 | `EHI_TABLE_STMT_ID` | DOUBLE | NOT NULL |  | This is a key column for the global temp table. It is not an official Primary Key. |
| 8 | `HIER_LEVEL_NBR` | DOUBLE | NOT NULL |  | The level within a hierachical structure that this record represents |
| 9 | `HIER_PATH` | VARCHAR(2000) |  |  | The path used to navigate to the level within the hierachical structure that this record represents |
| 10 | `INSERT_STMT` | VARCHAR(4000) |  |  | The sql statement used to insert data for the EHI Extract |
| 11 | `INS_ORDER` | DOUBLE | NOT NULL |  | Indicates table relationships order level |
| 12 | `PARENT_TABLE` | VARCHAR(30) | NOT NULL |  | The table that is the parent to this record |
| 13 | `PAR_COL_STR` | VARCHAR(200) | NOT NULL |  | Store parent column name |
| 14 | `SELECT_STMT` | VARCHAR(4000) |  |  | The sql statement used to select data for the EHI Extract |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

