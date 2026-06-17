# BR_DELETE_HIST

> Stores the primary keys of items that have been deleted. This is for Lighthouse Reporting.

**Description:** Bedrock Delete History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DELETE_HIST_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_DELETE_HIST table. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date that this row was created. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary key that was deleted. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The table that the primary key being deleted was from. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

