# DEPARTMENT

> Sub Table to Service Resource. Contains only those resource which are departments. Departments are children of Institutions and parent of Sections

**Description:** Department  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHARGE_COST_RATIO` | DOUBLE |  |  | Charge Cost Ratio. Currently not in use. Will be deleted |
| 2 | `EXAMONLY_HOLD_TIME_HRS` | DOUBLE |  |  | This column defines the number of hours (from exam complete) that exam-only procedures in this department are allowed to have a report attached to them. |
| 3 | `REIMBURSEMENT_COST_RATIO` | DOUBLE |  |  | This column defines the number of hours (from exam complete) that exam-only procedures in this department are allowed to have a report attached to them. |
| 4 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The service resource code of the department. Internal identifier which the user is unaware. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

