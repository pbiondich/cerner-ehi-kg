# SN_COST_REF

> This table holds the reference information for costing of roles and prsnl.

**Description:** SN COST REF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AREA_CD` | DOUBLE | NOT NULL |  | The surgical area for the cost. |
| 2 | `COST_PER_MIN` | DOUBLE |  |  | The cost per minute of time. |
| 3 | `COST_REF_ID` | DOUBLE | NOT NULL |  | Primary KeyColumn |
| 4 | `COST_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | The cost type meaningColumn |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent foreign key for this cost |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Parent table for this cost |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

