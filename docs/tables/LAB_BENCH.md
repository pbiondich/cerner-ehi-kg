# LAB_BENCH

> Resources which are laboratory benches (compared to instruments).

**Description:** Lab Bench  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTAINER_IND` | DOUBLE |  |  | Container Indicator. Will be deleted |
| 2 | `GATE_IND` | DOUBLE |  |  | Gate indicator. Will be deleted |
| 3 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The internal identifier for the bench. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `WORKLIST_BUILD_FLAG` | DOUBLE |  |  | Indicates how worklists should be built. Valid values are Automatically, Manually, Not used. Functionality is not available as of March 1997. |
| 10 | `WORKLIST_HOURS` | DOUBLE |  |  | The maximum number of hours that a worklist is valid for accepting new accessions. Functionality is not available as of March 1997 |
| 11 | `WORKLIST_MAX` | DOUBLE |  |  | The maximum number of accessions for a worklist. Functionality is not available as of March 1997 |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

