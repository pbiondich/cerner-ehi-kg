# PN_RECOVERY_DETAIL

> This table will serve as a detail table for PathNet recovery logic. It will be used to track detailed items about either the PN_RECOVERY or PN_RECOVERY_CHILD rows.

**Description:** PathNet Recovery Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_DESC` | VARCHAR(250) |  |  | Stores a description (string) value if the detail requires. |
| 2 | `DETAIL_DT_TM` | DATETIME |  |  | Stores a date/time value if the detail requires. |
| 3 | `DETAIL_ID` | DOUBLE | NOT NULL |  | Stores an ID value if the detail requires. Used for foreign key indexes. |
| 4 | `DETAIL_MEAN` | VARCHAR(40) | NOT NULL |  | Indicates the field that is being stored. |
| 5 | `DETAIL_VALUE` | DOUBLE |  |  | Stores a generic number value if the detail requires. |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique ID to the PARENT_ENTITY_NAME table. |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Table to which this row is linked. |
| 8 | `PN_RECOVERY_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique ID |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

