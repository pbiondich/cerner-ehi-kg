# HLA_TYP_RES_TRAY

> Relates an order to the inventory lot and HLA typing tray map selected for testing.

**Description:** HLA Typing Result Tray  
**Table type:** ACTIVITY  
**Primary key:** `LOT_NUMBER_ID`, `ORDER_ID`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where HLA Typing tray result comments are stored. It is a foreign key reference to the primary key of the long_text table. |
| 2 | `COMPLEMENT` | VARCHAR(20) |  |  | Complement lot number or other information pertaining to the complement used on an HLA typing tray. |
| 3 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies the inventory lot of the HLA Typing tray being used. It is a foreign key reference to the primary key of the lot_number_info table. |
| 4 | `MAGNETIC_BEADS` | VARCHAR(20) |  |  | Magnetic beads lot number or other information pertaining to the magnetic beads used on an HLA typing tray. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | PK FK→ | Relates results for the HLA Typing tray to a specific order. It is a foreign key reference to the primary key of the orders table. |
| 6 | `PLATED_DT_TM` | DATETIME |  |  | Date the HLA typing tray was plated. |
| 7 | `PLATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Id of the person who plated the HLA typing tray. |
| 8 | `READ_DT_TM` | DATETIME |  |  | Date the HLA typing tray was reviewed. |
| 9 | `READ_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Id of the person who read the HLA typing tray. |
| 10 | `SEPARATED_DT_TM` | DATETIME |  |  | Date the cells were separated for the HLA typing tray. |
| 11 | `SEPARATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Id of the person who separated the cells for the HLA typing tray. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VIABILITY` | DOUBLE |  |  | Viability percentage for the cells placed on an HLA typing tray. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `LOT_NUMBER_ID` | [HLA_TYP_TRAY_MAP](HLA_TYP_TRAY_MAP.md) | `LOT_NUMBER_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PLATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `READ_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SEPARATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HLA_TYP_TRAY_WELL_SCORE](HLA_TYP_TRAY_WELL_SCORE.md) | `LOT_NUMBER_ID` |
| [HLA_TYP_TRAY_WELL_SCORE](HLA_TYP_TRAY_WELL_SCORE.md) | `ORDER_ID` |

