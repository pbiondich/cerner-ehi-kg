# EVENTSET_TASK_RLTN

> Table to map event sets to tasks

**Description:** EVENTSET TASK RLTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENTSET_TASK_RLTN_ID` | DOUBLE | NOT NULL |  | unique sequence numberColumn |
| 2 | `GROUP_EVENT_SET_CD` | DOUBLE | NOT NULL |  | Event set code of the groupColumn |
| 3 | `POSITION_CD` | DOUBLE | NOT NULL |  | Position codeColumn |
| 4 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL |  | Task type from the order_task tableColumn |
| 5 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether task_assay_cd is requiredColumn |
| 6 | `SPECIALTY_EVENT_SET_CD` | DOUBLE | NOT NULL |  | Event set code of the specialty flowsheetColumn |
| 7 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The code value for the discrete task assayColumn |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

