# DM_CMB_CHILDREN

> Stores Person and Encounter child tables

**Description:** DM CMB CHILDREN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_COLUMN` | VARCHAR(32) | NOT NULL |  | Name of foreign key attribute of child table |
| 2 | `CHILD_CONS_NAME` | VARCHAR(30) | NOT NULL |  | Name of the FK constraint on the child_table that references the parent_table. |
| 3 | `CHILD_PK` | VARCHAR(32) |  |  | Name of primary key attribute |
| 4 | `CHILD_TABLE` | VARCHAR(32) | NOT NULL |  | Name of child table that will be updated in the combine |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was inserted. |
| 6 | `PARENT_TABLE` | VARCHAR(32) | NOT NULL |  | Name of combine parent table, such as PERSON, etc. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

