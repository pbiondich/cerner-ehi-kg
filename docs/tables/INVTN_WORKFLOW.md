# INVTN_WORKFLOW

> Reference Data. Definition of invitation workflows which can be assigned to multiple programs. Workflows are used to define what tracking statuses and communication scheduling parameters should be used for a program.

**Description:** INVITATION WORKFLOW  
**Table type:** REFERENCE  
**Primary key:** `WORKFLOW_ID`  
**Columns:** 11  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `PREV_WORKFLOW_ID` | DOUBLE | NOT NULL | FK→ | Workflows are grouped by this identifier so that all versions of a workflow have the same prev_workflow_id. Type 2 versioning. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `WORKFLOW_ID` | DOUBLE | NOT NULL | PK | The unique identifier of the workflow |
| 11 | `WORKFLOW_NAME` | VARCHAR(250) | NOT NULL |  | The unique name of the workflow. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_WORKFLOW_ID` | [INVTN_WORKFLOW](INVTN_WORKFLOW.md) | `WORKFLOW_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [INVTN_PROGRAM](INVTN_PROGRAM.md) | `WORKFLOW_ID` |
| [INVTN_WORKFLOW](INVTN_WORKFLOW.md) | `PREV_WORKFLOW_ID` |
| [INVTN_WORKFLOW_STATUS](INVTN_WORKFLOW_STATUS.md) | `WORKFLOW_ID` |

