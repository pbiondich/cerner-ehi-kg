# BLOT_POSITIVE_PROBE

> Indicates whether a positive reaction occured for a specific probe number in an HLA molecular typing blot.

**Description:** Blot Positive Probe  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOT_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Identifies the blot batch of the Molecular Blot being used to arrive at the results. It is a foreign key reference to the primary key of the blot batch table. |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates results for the Molecular Blot to a specific order. It is a foreign key reference to the primary key of the orders table. |
| 3 | `PROBE_NUMBER` | DOUBLE | NOT NULL |  | Number of the molecular blot probe which had a positive reaction |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `X_POS` | DOUBLE | NOT NULL | FK→ | Defines the column on a Blot Batch that an order is placed on. |
| 10 | `Y_POS` | DOUBLE | NOT NULL | FK→ | Defines the row on a Blot Batch that an order is placed on. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BLOT_BATCH_ID` | [BLOT_BATCH_RESULT](BLOT_BATCH_RESULT.md) | `BLOT_BATCH_ID` |
| `ORDER_ID` | [BLOT_BATCH_RESULT](BLOT_BATCH_RESULT.md) | `ORDER_ID` |
| `X_POS` | [BLOT_BATCH_RESULT](BLOT_BATCH_RESULT.md) | `X_POS` |
| `Y_POS` | [BLOT_BATCH_RESULT](BLOT_BATCH_RESULT.md) | `Y_POS` |

