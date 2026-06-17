# GRACE_PERIOD_RANGE

> Stores grace period ranges for future orders.

**Description:** GRACE_PERIOD_RANGE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GRACE_PERIOD_IN_DAYS` | DOUBLE | NOT NULL |  | The grace period in days. |
| 2 | `GRACE_PERIOD_RANGE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the GRACE_PERIOD_RANGE table. |
| 3 | `MAX_NUMBER_OF_DAYS` | DOUBLE | NOT NULL |  | The maximum number of days. |
| 4 | `MIN_NUMBER_OF_DAYS` | DOUBLE | NOT NULL |  | The minimum number of days. |
| 5 | `TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Denotes the type of grace period range. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

