# MM_GL_LOG_HMW

> GL Log header table for HMW

**Description:** MM GL LOG HMW  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_NBR` | DOUBLE |  |  | Batch Number |
| 2 | `BATCH_SELECTION` | VARCHAR(500) |  |  | Batch Selection |
| 3 | `COMMENTS` | VARCHAR(100) |  |  | Comments |
| 4 | `FILENAME` | VARCHAR(100) |  |  | Filename |
| 5 | `LOG_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 6 | `OUTPUT_DIST` | VARCHAR(100) |  |  | Output Destination |
| 7 | `REV_FILENAME` | VARCHAR(100) |  |  | Reversal Filename |
| 8 | `TOTAL_AMT` | DOUBLE |  |  | Total Amount |
| 9 | `TOTAL_CREDIT_AMT` | DOUBLE |  |  | Total Credit Amount |
| 10 | `TOTAL_CREDIT_LINES` | DOUBLE |  |  | Number of credit lines |
| 11 | `TOTAL_DEBIT_AMT` | DOUBLE |  |  | Total Debit Amount |
| 12 | `TOTAL_DEBIT_LINES` | DOUBLE |  |  | Total Debit Lines |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

