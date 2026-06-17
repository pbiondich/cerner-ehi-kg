# OMF_RADEXAM_ST

> The detail level summary table for radiology management.

**Description:** OMF RADEXAM ST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREDIT_QUANTITY` | DOUBLE |  |  | Credited quantity. |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL |  | The unique identification number that pertains to the order. |
| 3 | `QUANTITY` | DOUBLE |  |  | The number completed/used (supplies) for this detail record. |
| 4 | `RAD_EXAM_ID` | DOUBLE | NOT NULL |  | Unique identification number for the radiology exam. |
| 5 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | The default result type for the exam. |
| 6 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The task assay code for the radiology exam. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

