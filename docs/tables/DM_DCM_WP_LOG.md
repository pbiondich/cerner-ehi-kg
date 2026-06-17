# DM_DCM_WP_LOG

> A table to old notes about a work plan for the change management solution

**Description:** Data Change Management Work Plan Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_DCM_WORK_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Points to the DM_DCM_WORK_PLAN table |
| 2 | `DM_DCM_WP_LOG_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `LOG_DESCRIPTION` | VARCHAR(50) |  |  | Holds a description of the type of information in LOG_TEXT |
| 4 | `LOG_TEXT` | VARCHAR(4000) |  |  | Holds the text user chose to store |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_DCM_WORK_PLAN_ID` | [DM_DCM_WORK_PLAN](DM_DCM_WORK_PLAN.md) | `DM_DCM_WORK_PLAN_ID` |

