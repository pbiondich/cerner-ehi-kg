# DM_PURGE_HISTORY

> Holds changes made to purge jobs like when it was activated and when answers to questions were changed.

**Description:** DM Purge History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHANGE_TYPE` | VARCHAR(12) | NOT NULL |  | Which value changed regarding the purge job. Must be one of the following: 'ACTIVE_FLAG', 'PURGE_FLAG', 'MAX_ROWS', or 'TOKEN'. |
| 2 | `DM_PURGE_HISTORY_ID` | DOUBLE | NOT NULL |  | Primary Key from sequence DM_CLINICAL_SEQ |
| 3 | `JOB_ID` | DOUBLE | NOT NULL | FK→ | The purge job ID that his change was made to. FK from DM_PURGE_JOB |
| 4 | `NEW_TOKEN_STRING_VALUE` | VARCHAR(255) | NOT NULL |  | The value of a character token after it was changed in Purge Job Manager. |
| 5 | `NEW_VALUE` | DOUBLE | NOT NULL |  | The value of a numeric token after it was changed in Purge Job Manager |
| 6 | `OLD_TOKEN_STRING_VALUE` | VARCHAR(255) | NOT NULL |  | The value of a character token before it was changed in Purge Job Manager. |
| 7 | `OLD_VALUE` | DOUBLE | NOT NULL |  | The value of a numeric token before it was changed in Purge Job Manager |
| 8 | `TOKEN_STR` | VARCHAR(255) |  |  | If the change type is 'TOKEN' this will be filled out with the token_str from DM_PURGE_JOB_TOKEN that is changing. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `JOB_ID` | [DM_PURGE_JOB](DM_PURGE_JOB.md) | `JOB_ID` |

