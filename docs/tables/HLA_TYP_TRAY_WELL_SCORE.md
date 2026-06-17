# HLA_TYP_TRAY_WELL_SCORE

> Records the individual well scores as part of the raw result data specific to HLA typing for an order.

**Description:** HLA Typing Tray Well Score  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FALSE_NEG_IND` | DOUBLE |  |  | Indicates whether the well was falsely scored as negative based on the antigens identified in the interpretation of the HLA Tping tray. NOT CURRENTLY IMPLEMENTED. |
| 2 | `FALSE_POS_IND` | DOUBLE |  |  | Indicates whether the well was falsely scored as positive based on the antigens identified in the interpretation of the HLA Tping tray. NOT CURRENTLY IMPLEMENTED. |
| 3 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the inventory lot of the HLA Typing tray for which the well score is being recorded. It is a foreign key reference to the primary key of the lot_number_info table. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates well scores for the HLA Typing tray to a specific order. It is a foreign key reference to the primary key of the orders table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `WELL_SCORE_CD` | DOUBLE | NOT NULL |  | The code for the well score given to this HLA Typing tray well. |
| 11 | `X_POS` | DOUBLE | NOT NULL |  | Horizontal coordinate of the well being scored. |
| 12 | `Y_POS` | DOUBLE | NOT NULL |  | Vertical coordinate of the well being scored. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [HLA_TYP_RES_TRAY](HLA_TYP_RES_TRAY.md) | `LOT_NUMBER_ID` |
| `ORDER_ID` | [HLA_TYP_RES_TRAY](HLA_TYP_RES_TRAY.md) | `ORDER_ID` |

