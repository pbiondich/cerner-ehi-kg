# OMF_PV_BATCH

> Top level information of PowerVision scheduled views result sets.

**Description:** OMF PV BATCH  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_ID` | DOUBLE | NOT NULL |  | Unique key. |
| 2 | `DELETE_ON_DT_TM` | DATETIME |  |  | Date when the result set should be deleted. |
| 3 | `ERROR_IND` | DOUBLE |  |  | Indicates whether an error occurred while retrieving result set. |
| 4 | `ERROR_MSG1` | VARCHAR(255) |  |  | Text of error message. |
| 5 | `ERROR_MSG2` | VARCHAR(255) |  |  | Text of error message. |
| 6 | `ERROR_MSG3` | VARCHAR(255) |  |  | Text of error message. |
| 7 | `FINISH_DT_TM` | DATETIME |  |  | Date/time when the result set finished running. |
| 8 | `HASH_KEY` | DOUBLE |  |  | Hash value which represents the facts, dimensions and filtering done in this saved view. |
| 9 | `NUMBER_COLS` | DOUBLE |  |  | Number of facts and dimensions in this result set. |
| 10 | `NUMBER_ROWS` | DOUBLE |  |  | Number of rows retuned in this result set. |
| 11 | `OMF_PV_ITEM_ID` | DOUBLE | NOT NULL |  | Saved view id which this result set is for. |
| 12 | `START_DT_TM` | DATETIME |  |  | Date/time when the result set was started being retrieved. |
| 13 | `TOTAL_IND` | DOUBLE |  |  | Not currently used. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `USER_ID` | DOUBLE | NOT NULL |  | Users person_id which owns the saved view being run. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

