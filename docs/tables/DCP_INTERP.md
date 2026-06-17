# DCP_INTERP

> Base table to drive interpretation of a result based on the value of other results.

**Description:** Base table to drive interpretation of a result based on the value of other resul  
**Table type:** REFERENCE  
**Primary key:** `DCP_INTERP_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGE_FROM_MINUTES` | DOUBLE | NOT NULL |  | beginning age for reference range. |
| 2 | `AGE_TO_MINUTES` | DOUBLE | NOT NULL |  | Ending age for reference range. |
| 3 | `DCP_INTERP_ID` | DOUBLE | NOT NULL | PK | Unique identifier for interp table. |
| 4 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Service Resource Cd for reference range. |
| 5 | `SEX_CD` | DOUBLE | NOT NULL |  | Sex Cd for reference range. |
| 6 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Task Assay Cd for which interpretation is defined. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DCP_INTERP_COMPONENT](DCP_INTERP_COMPONENT.md) | `DCP_INTERP_ID` |
| [DCP_INTERP_STATE](DCP_INTERP_STATE.md) | `DCP_INTERP_ID` |

