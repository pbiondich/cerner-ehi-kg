# DM_PK_WHERE_PARM

> Stores PK_WHERE parameters to be used by RDDS for each table

**Description:** Database Management PK_WHERE Parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Column name of parameter |
| 2 | `DATA_TYPE` | VARCHAR(20) | NOT NULL |  | Holds data type of column |
| 3 | `DELETE_IND` | DOUBLE | NOT NULL |  | Indicates if parameters are for delete or not |
| 4 | `EXIST_IND` | DOUBLE | NOT NULL |  | Indicates if column should exist in PTAM_MATCH_RESULT |
| 5 | `FUNCTION_TYPE` | VARCHAR(20) | NOT NULL |  | Differentiates if parameters are for PK_WHERE or PTAM_MATCH |
| 6 | `PARM_NBR` | DOUBLE | NOT NULL |  | Orders parameters |
| 7 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Holds table name that uses template |
| 8 | `TRANS_IND` | DOUBLE | NOT NULL |  | Indicates if column is translatable |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

