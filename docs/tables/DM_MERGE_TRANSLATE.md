# DM_MERGE_TRANSLATE

> Stores translated values for ID and CD columns

**Description:** DM Merge Translation Table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENV_SOURCE_ID` | DOUBLE | NOT NULL |  | Environment ID for the Source database |
| 2 | `ENV_TARGET_ID` | DOUBLE | NOT NULL |  | Target Environment ID |
| 3 | `ERROR_MSG` | VARCHAR(255) |  |  | Column containing any error message |
| 4 | `ERROR_NBR` | DOUBLE |  |  | Column containing the error number |
| 5 | `FROM_VALUE` | DOUBLE | NOT NULL |  | The value from the source environment. |
| 6 | `LOG_ID` | DOUBLE | NOT NULL |  | Row in the DM_CHG_LOG table which caused the translation to be made. |
| 7 | `MERGE_ID` | DOUBLE | NOT NULL |  | Merge_id VALUE |
| 8 | `STATUS_FLG` | DOUBLE |  |  | A status flag. |
| 9 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of the table. |
| 10 | `TO_VALUE` | DOUBLE | NOT NULL |  | Target value. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

