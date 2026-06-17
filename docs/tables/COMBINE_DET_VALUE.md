# COMBINE_DET_VALUE

> Stores values of columns that have been modified as part of the combine process.

**Description:** Combine Detail Values  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Name of the column that is being saved in this table during combine |
| 2 | `COLUMN_TYPE` | VARCHAR(5) |  |  | Type of the column that is being saved in this table during combine |
| 3 | `COMBINE_DET_VALUE_ID` | DOUBLE | NOT NULL |  | Primary key. |
| 4 | `COMBINE_ID` | DOUBLE | NOT NULL |  | Identifier for row referenced from one of the three parent combine tables. |
| 5 | `COMBINE_PARENT` | VARCHAR(30) | NOT NULL |  | Parent table for the kind of combine. |
| 6 | `ENTITY_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ENTITY_NAME table. |
| 7 | `ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | This is the name of the table that contains data to be combined. |
| 8 | `FROM_VALUE` | VARCHAR(2000) |  |  | Old value of the column that is being saved in this table during combine |
| 9 | `PARENT_ENTITY` | VARCHAR(30) | NOT NULL |  | Parent table for the kind of combine. |
| 10 | `TO_VALUE` | VARCHAR(2000) |  |  | New value of the column that is being saved in this table during combine |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

