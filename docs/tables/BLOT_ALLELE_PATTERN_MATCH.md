# BLOT_ALLELE_PATTERN_MATCH

> Records the alleles identified in HLA molecular blot testing as determined by pattern matching or as entered by the user for a specific order and blot.

**Description:** Blot Allele Pattern Match  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLELE_CD` | DOUBLE | NOT NULL |  | The code for an allele identified as a result of testing using an HLA molecular typing blot. |
| 2 | `BLOT_BATCH_ID` | DOUBLE | NOT NULL | FK→ | A number which identifies the blot batch to which the allele result relates. It is a foreign key reference to the primary key of the blot_batch table. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates the allele to a specific order. It is a foreign key reference to the primary key of the orders table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `X_POS` | DOUBLE | NOT NULL | FK→ | The column on the Blot Batch where the order is placed. |
| 10 | `Y_POS` | DOUBLE | NOT NULL | FK→ | The row on the Blot Batch where the order is placed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BLOT_BATCH_ID` | [BLOT_BATCH_RESULT](BLOT_BATCH_RESULT.md) | `BLOT_BATCH_ID` |
| `ORDER_ID` | [BLOT_BATCH_RESULT](BLOT_BATCH_RESULT.md) | `ORDER_ID` |
| `X_POS` | [BLOT_BATCH_RESULT](BLOT_BATCH_RESULT.md) | `X_POS` |
| `Y_POS` | [BLOT_BATCH_RESULT](BLOT_BATCH_RESULT.md) | `Y_POS` |

