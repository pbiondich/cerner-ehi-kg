# HLA_AB_SCREEN_RESULT

> Records the raw result data specific to an HLA antibody screen for an order included in the screen's batch.

**Description:** HLA Antibody Screen Result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_ID` | DOUBLE | NOT NULL | FK→ | References the batch to which the Antibody Screen results apply. Orders may be placed in multiple batches or in the same batch multiple times. It is a foreign key reference to the primary key of the hla_ab_screen_batch table. |
| 2 | `BATCH_NUMBER` | DOUBLE |  |  | References the batch to which the Antibody Screen results apply. Orders may be placed in multiple batches or in the same batch multiple times. It is a foreign key reference to the primary key of the hla_ab_screen_batch table. |
| 3 | `BATCH_TRAY_NUMBER` | DOUBLE | NOT NULL |  | The Antibody Screen tray within the batch that the order was placed on. This will only be populated when inventory is mapped by well and is tested by tray. |
| 4 | `BATCH_X_POS` | DOUBLE | NOT NULL |  | The horizontal coordinate of a well on an Antibody Screen tray within the batch that the order was placed on. This will only be populated when inventory is mapped by row and tested by column or when it is mapped by tray and tested by well. |
| 5 | `BATCH_Y_POS` | DOUBLE | NOT NULL |  | The vertical coordinate of a well on an Antibody Screen tray within the batch that the order was placed on. This will only be populated when inventory is mapped by column and tested by row or when it is mapped by tray and tested by well. |
| 6 | `B_CELL_PRA` | DOUBLE |  |  | The B-Cell percentage Panel Reactive Antibody for the order at this batch placement. PRA = Positive Wells / Total Wells Scored. |
| 7 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where antibody screen result comments are stored. It is a foreign key reference to the primary key of the long_text table. |
| 8 | `COMPLEMENT` | VARCHAR(20) |  |  | Complement lot number or other information pertaining to the complement used on an HLA antibody screen tray. |
| 9 | `DILUTION_CD` | DOUBLE | NOT NULL |  | The code for the dilution that used for the order at this batch placement. |
| 10 | `METHODOLOGY_CD` | DOUBLE | NOT NULL |  | The code for the methodology that used for the order at this batch placement. |
| 11 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates results for the Antibody Screen batch placement to a specific order. It is a foreign key reference to the primary key of the orders table. |
| 12 | `PLATED_DT_TM` | DATETIME |  |  | The date the HLA antibody screen tray was plated. |
| 13 | `PLATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Id of the person who plated the HLA antibody screen tray. |
| 14 | `READ_DT_TM` | DATETIME |  |  | The date the HLA Antibody screen tray was reviewed. |
| 15 | `READ_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Id of the person who read the HLA antibody screen tray. |
| 16 | `T_CELL_PRA` | DOUBLE |  |  | The T-Cell percentage Panel Reactive Antibody for the order at this batch placement. PRA = Positive Wells / Total Wells Scored. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `VIABILITY` | DOUBLE |  |  | Viability percentage for the serum placed on an HLA antibody screen tray. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_ID` | [HLA_AB_SCREEN_BATCH](HLA_AB_SCREEN_BATCH.md) | `BATCH_ID` |
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PLATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `READ_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

