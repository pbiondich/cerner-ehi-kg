# DM_TRANSACTION_KEY

> Primary key information for the row that was modified.

**Description:** DM TRANSACTION KEY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FIELD_CHAR_VALUE` | VARCHAR(255) |  |  | Data value for the primary key for the row being modified. |
| 2 | `FIELD_DATE_VALUE` | DATETIME |  |  | Data value for the primary key for the row being modified. |
| 3 | `FIELD_NAME` | VARCHAR(32) | NOT NULL |  | Column name for the primary key for the row being modified. |
| 4 | `FIELD_NUM_VALUE` | DOUBLE |  |  | Data value for the primary key for the row being modified. |
| 5 | `TRANSACTION_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Parent record for this transaction. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRANSACTION_ACTIVITY_ID` | [DM_TRANSACTION_ACTIVITY](DM_TRANSACTION_ACTIVITY.md) | `TRANSACTION_ACTIVITY_ID` |

