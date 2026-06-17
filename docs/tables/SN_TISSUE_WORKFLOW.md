# SN_TISSUE_WORKFLOW

> Tissue Workflow

**Description:** SN_TISSUE_WORKFLOW  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | date and time when the workflow started. |
| 2 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | id of the personnel who created this record |
| 3 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | code value of the location where this workflow occurred |
| 4 | `SN_TISSUE_WORKFLOW_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `STATUS_CD` | DOUBLE | NOT NULL |  | code value of workflow status (e.g. complete, inProgress, pending)of the workflow. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `WORKFLOW_TYPE_CD` | DOUBLE | NOT NULL |  | code value of the workflow type |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

