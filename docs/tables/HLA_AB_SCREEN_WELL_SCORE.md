# HLA_AB_SCREEN_WELL_SCORE

> Records individual well scores as part of the raw result data specific to an HLA antibody screen for an order included in the screen's batch.

**Description:** HLA Antibody Screen Well Score  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_ID` | DOUBLE | NOT NULL | FK→ | References the batch to which the Antibody Screen well scores apply. Orders may be placed in multiple batches or in the same batch multiple times. It is a foreign key reference to the primary key of the hla_ab_screen_batch table. |
| 2 | `BATCH_NUMBER` | DOUBLE |  |  | References the batch to which the Antibody Screen well scores apply. Orders may be placed in multiple batches or in the same batch multiple times. It is a foreign key reference to the primary key of the hla_ab_screen_batch table. |
| 3 | `B_CELL_WELL_SCORE_CD` | DOUBLE | NOT NULL |  | The code for the well score given to this Antibody Screen well for the B-Cell reaction. |
| 4 | `FALSE_NEG_IND` | DOUBLE |  |  | Indicates whether the well was falsely scored as negative based on the antibodies identified in the interpretation of the Antibody Screen. NOT CURRENTLY IMPLEMENTED. |
| 5 | `FALSE_POS_IND` | DOUBLE |  |  | Indicates whether the well was falsely scored as positive based on the antibodies identified in the interpretation of the Antibody Screen. NOT CURRENTLY IMPLEMENTED. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates results for the Antibody Screen batch placement to a specific order. It is a foreign key reference to the primary key of the orders table. |
| 7 | `TRAY_NUMBER` | DOUBLE | NOT NULL |  | Tray number of the tray where the well being scored is located. |
| 8 | `T_CELL_WELL_SCORE_CD` | DOUBLE | NOT NULL |  | The code for the well score given to this Antibody Screen well for the T-Cell reaction. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `X_POS` | DOUBLE | NOT NULL |  | Horizontal coordinate of the well being scored. |
| 15 | `Y_POS` | DOUBLE | NOT NULL |  | Vertical coordinate of the well being scored. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_ID` | [HLA_AB_SCREEN_BATCH](HLA_AB_SCREEN_BATCH.md) | `BATCH_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

