# DM_CB_REQUEST_PROCESSING

> Holds requests to be activated or inactivated for the customized object drop/build process.

**Description:** DM conditional build request processing.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FORMAT_SCRIPT` | VARCHAR(30) | NOT NULL |  | SCRIPT THE REQUEST WILL EXECUTE |
| 3 | `QUESTION_NBR` | DOUBLE | NOT NULL | FK→ | QUESTION NUMBER THE REQUEST BELONGS TO |
| 4 | `REQUEST_NUMBER` | DOUBLE | NOT NULL |  | NUMBER OF THE REQUEST |
| 5 | `REQUEST_STATUS` | VARCHAR(30) |  |  | STATUS OF THE REQUEST. (ACTIVE,INACTIVE) |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUESTION_NBR` | [DM_CB_QUESTIONS](DM_CB_QUESTIONS.md) | `QUESTION_NBR` |

