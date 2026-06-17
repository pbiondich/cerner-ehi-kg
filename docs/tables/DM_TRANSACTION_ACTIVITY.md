# DM_TRANSACTION_ACTIVITY

> One row per row affected by this transaction.

**Description:** DM TRANSACTION ACTIVITY  
**Table type:** ACTIVITY  
**Primary key:** `TRANSACTION_ACTIVITY_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTITY_NAME` | VARCHAR(32) |  |  | This is the name of the entity being modified by this transaction. |
| 2 | `TRANSACTION_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | unique identifier for each row |
| 3 | `TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | foreign key to dm_transactions. |
| 4 | `TRANSACTION_TYPE` | VARCHAR(6) |  |  | INSERT,SELECT,DELETE,UPDATE |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRANSACTION_ID` | [DM_TRANSACTIONS](DM_TRANSACTIONS.md) | `TRANSACTION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DM_TRANSACTION_DATA](DM_TRANSACTION_DATA.md) | `TRANSACTION_ACTIVITY_ID` |
| [DM_TRANSACTION_KEY](DM_TRANSACTION_KEY.md) | `TRANSACTION_ACTIVITY_ID` |

