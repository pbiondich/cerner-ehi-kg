# BLOT_BATCH_RESULT

> Relates an order to the Blot Batch and HLA molecular typing blot selected for testing.

**Description:** Blot Batch Result  
**Table type:** ACTIVITY  
**Primary key:** `BLOT_BATCH_ID`, `ORDER_ID`, `X_POS`, `Y_POS`  
**Columns:** 10  
**Referenced by:** 12 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AMPLIFICATION_GEL` | VARCHAR(20) |  |  | Name or number of the Gel that was used to amplify the DNA with primers used in the Blot testing. |
| 2 | `BLOT_BATCH_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies the inventory lot of the Molecular Blot being used. It is a foreign key reference to the primary key of the lot_number_info table. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | PK FK→ | Relates results for the Molecular Blot to a specific order. It is a foreign key reference to the primary key of the orders table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `X_POS` | DOUBLE | NOT NULL | PK | Defines the column on a Blot Batch that an order is placed on. |
| 10 | `Y_POS` | DOUBLE | NOT NULL | PK | Defines the row on a Blot Batch that an order is placed on. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BLOT_BATCH_ID` | [BLOT_BATCH](BLOT_BATCH.md) | `BLOT_BATCH_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (12)

| From table | Column |
|------------|--------|
| [BLOT_ALLELE_PATTERN_MATCH](BLOT_ALLELE_PATTERN_MATCH.md) | `BLOT_BATCH_ID` |
| [BLOT_ALLELE_PATTERN_MATCH](BLOT_ALLELE_PATTERN_MATCH.md) | `ORDER_ID` |
| [BLOT_ALLELE_PATTERN_MATCH](BLOT_ALLELE_PATTERN_MATCH.md) | `X_POS` |
| [BLOT_ALLELE_PATTERN_MATCH](BLOT_ALLELE_PATTERN_MATCH.md) | `Y_POS` |
| [BLOT_POSITIVE_PROBE](BLOT_POSITIVE_PROBE.md) | `BLOT_BATCH_ID` |
| [BLOT_POSITIVE_PROBE](BLOT_POSITIVE_PROBE.md) | `ORDER_ID` |
| [BLOT_POSITIVE_PROBE](BLOT_POSITIVE_PROBE.md) | `X_POS` |
| [BLOT_POSITIVE_PROBE](BLOT_POSITIVE_PROBE.md) | `Y_POS` |
| [BLOT_SPEC_PATTERN_MATCH](BLOT_SPEC_PATTERN_MATCH.md) | `BLOT_BATCH_ID` |
| [BLOT_SPEC_PATTERN_MATCH](BLOT_SPEC_PATTERN_MATCH.md) | `ORDER_ID` |
| [BLOT_SPEC_PATTERN_MATCH](BLOT_SPEC_PATTERN_MATCH.md) | `X_POS` |
| [BLOT_SPEC_PATTERN_MATCH](BLOT_SPEC_PATTERN_MATCH.md) | `Y_POS` |

