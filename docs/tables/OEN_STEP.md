# OEN_STEP

> Holds list of all valid Open Engine STEPS.

**Description:** OEN STEP  
**Table type:** REFERENCE  
**Primary key:** `STEP_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `STEP_DESC` | VARCHAR(255) |  |  | Holds a description of this Step.Column |
| 3 | `STEP_ID` | DOUBLE | NOT NULL | PK | Holds a unique number representing this Step.Column |
| 4 | `STEP_VALUE` | VARCHAR(30) |  |  | Holds a single letter representing this Step.Column |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OEN_ERROR](OEN_ERROR.md) | `STEP_ID` |
| [OEN_SEQ_STEP_R](OEN_SEQ_STEP_R.md) | `STEP_ID` |

