# DM_DCM_WORK_PLAN

> A table to track work plan items for the change management solution

**Description:** Data Change Management Work Plan  
**Table type:** ACTIVITY  
**Primary key:** `DM_DCM_WORK_PLAN_ID`  
**Columns:** 12  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADHOC_FLAG` | DOUBLE | NOT NULL |  | 0 - Work plan added manually, 1 - User added work plan on the fly, 2 - Application added work plan on the fly |
| 3 | `DM_DCM_WORK_PLAN_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `EXTERNAL_IDENT` | VARCHAR(50) |  |  | Identifier from data being imported from external system |
| 5 | `NOTE_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates if the user is forced to fill out comments when selecting a work plan |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `WORK_PLAN_NAME` | VARCHAR(100) | NOT NULL |  | A column to hold a name or summary of the work plan |
| 12 | `WORK_PLAN_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Points to the LONG_TEXT table for work plan details |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORK_PLAN_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [DM_DCM_UOW](DM_DCM_UOW.md) | `DM_DCM_WORK_PLAN_ID` |
| [DM_DCM_WP_LOG](DM_DCM_WP_LOG.md) | `DM_DCM_WORK_PLAN_ID` |
| [DM_DCM_WP_PRSNL_R](DM_DCM_WP_PRSNL_R.md) | `DM_DCM_WORK_PLAN_ID` |
| [DM_DCM_WP_STATUS_HIST](DM_DCM_WP_STATUS_HIST.md) | `DM_DCM_WORK_PLAN_ID` |

