# MIC_QC_NODE

> This reference table contains QC schedules and their relationships to other QC schedules/rules.

**Description:** Microbiology Quality Control Node  
**Table type:** REFERENCE  
**Primary key:** `NODE_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COND_SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the parent MIC_QC_COND_SCHEDULE table. |
| 6 | `DISPLAY_ORDER` | DOUBLE | NOT NULL |  | This field contains the display order of the individual nodes. |
| 7 | `NODE_ID` | DOUBLE | NOT NULL | PK | This field contains the internal identification code that uniquely identifies the 'schedule step' and its associated parameters. |
| 8 | `PARENT_NODE_ID` | DOUBLE | NOT NULL |  | This field contains the reference to the parent MIC_QC_NODE row. This field defines relationships to schedule nodes within a conditional schedule pathway. |
| 9 | `SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the schedule. A schedule_id only exist once within a pathway of a conditional schedule. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COND_SCHEDULE_ID` | [MIC_QC_COND_SCHEDULE](MIC_QC_COND_SCHEDULE.md) | `COND_SCHEDULE_ID` |
| `SCHEDULE_ID` | [MIC_QC_SCHEDULE](MIC_QC_SCHEDULE.md) | `SCHEDULE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_QC_RESULT](MIC_QC_RESULT.md) | `CURRENT_NODE_ID` |
| [MIC_QC_RESULT](MIC_QC_RESULT.md) | `PREVIOUS_NODE_ID` |

