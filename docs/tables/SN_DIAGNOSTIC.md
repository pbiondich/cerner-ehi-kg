# SN_DIAGNOSTIC

> The SurgiNet Diagnostics table

**Description:** The SurgiNet Diagnostics table contains the diagnostic tests for SurgiNet  
**Table type:** REFERENCE  
**Primary key:** `DIAGNOSTIC_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHK_DESCRIPTION` | VARCHAR(255) | NOT NULL |  | Describes the Check script |
| 6 | `COMMENT_TEXT` | VARCHAR(255) |  |  | A comment for the user |
| 7 | `DIAGNOSTIC_ID` | DOUBLE | NOT NULL | PK | The unique ID on the Table |
| 8 | `FIX_DESCRIPTION` | VARCHAR(255) |  |  | Describes the Fix portion of the Diagonostic Test |
| 9 | `LAST_CHK_DT_TM` | DATETIME |  |  | The date and time that the Diagnostic Rule was checked |
| 10 | `LAST_CHK_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the Last Check on the Diagonostic Rule. |
| 11 | `LAST_CHK_STATUS` | VARCHAR(1) | NOT NULL |  | The Status of the Last Check |
| 12 | `LAST_FIX_DT_TM` | DATETIME |  |  | The Date and Time the Fix was made using the Diagonostic Rule |
| 13 | `LAST_FIX_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the Last Fix using the Diagonostic Rule |
| 14 | `LAST_FIX_STATUS` | VARCHAR(1) | NOT NULL |  | The Status of the last Fix |
| 15 | `READ_ONLY_IND` | DOUBLE | NOT NULL |  | Specifies the Diagonostic is a Read only from the front-end |
| 16 | `TEST_NAME` | VARCHAR(50) | NOT NULL |  | The Test Name |
| 17 | `TEST_SCRIPT` | VARCHAR(30) | NOT NULL |  | The Script that will be executed for the Test |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_DIAGNOSTIC_REL](SN_DIAGNOSTIC_REL.md) | `DIAGNOSTIC_ID` |

