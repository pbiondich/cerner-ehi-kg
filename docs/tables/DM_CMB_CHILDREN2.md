# DM_CMB_CHILDREN2

> Stores list of child tables to facilitate the combine process for LOCATION, ORGANIZATION, HEALTH_PLAN and PRSNL

**Description:** Data management Combine Children table 2  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_COLUMN` | VARCHAR(30) | NOT NULL |  | Name of column on the child table that will be updated by the combine process. Usually this column references the parent table. |
| 2 | `CHILD_CONS_NAME` | VARCHAR(30) | NOT NULL |  | Name of foreign key constraint on the child table that references the parent table |
| 3 | `CHILD_TABLE` | VARCHAR(30) | NOT NULL |  | Name of child table that will be updated by the combine process |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | The date and time when the child table was added to the list |
| 5 | `PARENT_TABLE` | VARCHAR(30) | NOT NULL |  | Name of combine parent table, such as LOCATION etc. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

