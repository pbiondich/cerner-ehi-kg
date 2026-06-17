# DM_COLSTRING_PARM

> Stores list of columns that go into DM_CHG_LOG.COLSTRING

**Description:** Database Management Column String Parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Holds column name |
| 2 | `DATA_TYPE` | VARCHAR(20) | NOT NULL |  | Holds the data type of the column |
| 3 | `PARM_NBR` | DOUBLE | NOT NULL |  | Indicates the order that the columns appear in COLSTRING |
| 4 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Holds table name |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

