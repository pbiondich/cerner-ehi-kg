# DM_REFCHG_PKW_PARM

> Stores the parameters which will be used in the REFCHG_PK_WHERE_ _[1,2] functions. These values will be used to create the DM_CHG_LOG.PK_WHERE value.

**Description:** Data Management reference change PK where function parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Name of the column that needs to be passed into the REFCHG_PK_WHERE* function. |
| 2 | `PARM_NBR` | DOUBLE | NOT NULL |  | Order that this column needs to be placed when call the REFCHG_PK_WHERE* function. |
| 3 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of the table which has a filter requirement on it. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

