# DM_TRANSACTION_DATA

> 1 row per field modified for each transactions

**Description:** Stores the data that was modified.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FIELD_CHAR_VALUE` | VARCHAR(255) |  |  | Contains the data value if field modified is VARCHAR, CHAR or VARCHAR2. |
| 2 | `FIELD_DATE_VALUE` | DATETIME |  |  | Contains the data value if field modified is DATE. |
| 3 | `FIELD_LONGRAW_ID` | DOUBLE | NOT NULL |  | Contains the id for the long raw data modified. |
| 4 | `FIELD_LONG_ID` | DOUBLE | NOT NULL |  | ID of LONG data field that was modified |
| 5 | `FIELD_NAME` | VARCHAR(32) | NOT NULL |  | The name of the column modified by this transaction |
| 6 | `FIELD_NUM_VALUE` | DOUBLE |  |  | The data value for the field modified by this transaction if the field is of type NUMBER or FLOAT. |
| 7 | `TRANSACTION_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Parent record for this transaction. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRANSACTION_ACTIVITY_ID` | [DM_TRANSACTION_ACTIVITY](DM_TRANSACTION_ACTIVITY.md) | `TRANSACTION_ACTIVITY_ID` |

