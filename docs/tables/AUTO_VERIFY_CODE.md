# AUTO_VERIFY_CODE

> Stores processing and error codes encountered by autoverification while processing results.

**Description:** Automatic Verification Codes  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_VERIFY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific autoverification processing code sent by the GLB Result server while processing results. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the relationship between the autoverify codes and a parent result table (i.e. perform_result, qc_result). |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Defines the name of the parent result table in uppercase (i.e. PERFORM_RESULT, QC_RESULT) that relates to the autoverify code row. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

