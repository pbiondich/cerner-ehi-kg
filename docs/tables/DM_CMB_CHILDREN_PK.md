# DM_CMB_CHILDREN_PK

> Stores primary key information for child tables of LOCATION, ORGANIZATION, HEALTH_PLAN and PRSNL

**Description:** data management combine children primary key  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_TABLE` | VARCHAR(30) | NOT NULL |  | Name of child table that will be updated by the combine process |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time when the child table was added to the list |
| 3 | `PK_COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Name of column on the child table that is part of the primary key |
| 4 | `PK_COLUMN_POS` | DOUBLE | NOT NULL |  | Position of child table's column that is part of primary key |
| 5 | `PK_COLUMN_TYPE` | VARCHAR(20) | NOT NULL |  | Data type of child table's primary key column |
| 6 | `PK_IND` | DOUBLE | NOT NULL |  | Indicates if index is primary key. |
| 7 | `PK_INDEX_NAME` | VARCHAR(30) | NOT NULL |  | Name of primary key index on the child table |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

