# DM_TRANSACTIONS

> One row per transaction that should be tracked

**Description:** DM TRANSACTIONS  
**Table type:** REFERENCE  
**Primary key:** `TRANSACTION_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_END_DT_TM` | DATETIME |  |  | defines the ending of a transaction |
| 2 | `BATCH_START_DT_TM` | DATETIME |  |  | defines the beginning of a transaction |
| 3 | `DESCRIPTION` | VARCHAR(80) |  |  | description for the transaction |
| 4 | `TRANSACTION_CAT_CD` | DOUBLE |  |  | defines the type of transactions - not currently used |
| 5 | `TRANSACTION_ID` | DOUBLE | NOT NULL | PK | unique identifier for the row |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_TRANSACTION_ACTIVITY](DM_TRANSACTION_ACTIVITY.md) | `TRANSACTION_ID` |

