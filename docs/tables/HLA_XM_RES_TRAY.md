# HLA_XM_RES_TRAY

> Relates an inventory lot and HLA crossmatch tray map selected for testing.

**Description:** HLA Crossmatch Result Tray  
**Table type:** ACTIVITY  
**Primary key:** `HLA_XM_RES_TRAY_ID`  
**Columns:** 21  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_DESC` | VARCHAR(30) |  |  | The description given an HLA Crossmatch result tray . This description will be used to identify the tray when selecting it. |
| 2 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where HLA Crossmatch tray result comments are stored. It is a foreign key reference to the primary key of the long_text table. |
| 3 | `COMPLEMENT` | VARCHAR(20) |  |  | Complement lot number or other information pertaining to the complement used on an HLA crossmatch tray. |
| 4 | `DONOR_ID` | DOUBLE | NOT NULL | FK→ | Id of the donor of the HLA crossmatch tray. |
| 5 | `HLA_XM_RES_TRAY_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies a HLA crossmatch tray record. |
| 6 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the inventory lot of the HLA crossmatch tray being used. It is a foreign key reference to the primary key of the lot_number_info table. |
| 7 | `MAGNETIC_BEADS` | VARCHAR(20) |  |  | Magnetic beads lot number or other information pertaining to the magnetic beads used on an HLA crossmatch tray. |
| 8 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | ID of the order that the donor is associated to |
| 9 | `PLATED_DT_TM` | DATETIME |  |  | The Date the HLA crossmatch tray was plated. |
| 10 | `PLATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Id of the person who plated the HLA crossmatch tray. |
| 11 | `READ_DT_TM` | DATETIME |  |  | The date the HLA crossmatch tray was reviewed. |
| 12 | `READ_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Id of the person who read the HLA crossmatch tray. |
| 13 | `SEPARATED_DT_TM` | DATETIME |  |  | Date the cells were separated for the HLA crossmatch tray. |
| 14 | `SEPARATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Id of the person who separated the cells for the HLA crossmatch tray. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `VIABILITY` | DOUBLE |  |  | Viability percentage for the cells placed on an HLA crossmatch tray. |
| 21 | `WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | Identifies the worklist associated to the HLA crossmatch tray being used. It is a foreign key reference to the primary key of the worklist table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DONOR_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `LOT_NUMBER_ID` | [HLA_XM_TRAY_MAP](HLA_XM_TRAY_MAP.md) | `LOT_NUMBER_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PLATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `READ_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SEPARATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `WORKLIST_ID` | [WORKLIST](WORKLIST.md) | `WORKLIST_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HLA_XM_TRAY_WELL_SCORE](HLA_XM_TRAY_WELL_SCORE.md) | `HLA_XM_RES_TRAY_ID` |
| [PERSON_HLA_XM](PERSON_HLA_XM.md) | `HLA_XM_RES_TRAY_ID` |

