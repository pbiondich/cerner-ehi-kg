# HLA_AB_SCRN_WELL

> Defines what is contained in a single tray well located on a specific HLA antibody screen.

**Description:** HLA Antibody Screen Well  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CELL_ID` | DOUBLE | NOT NULL | FK→ | Identifies in conjunction with manufacturer the unique cells contained in an Antibody Screen tray well. Cell_id and manufacturer_cd are a foreign key reference to the primary key of the hla_ab_scrn_well_cell table. |
| 2 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Relates the Antibody Screen well to the inventory lot and related map. It is a foreign key reference to the primary key of the lot_number_info table. |
| 3 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | No longer used. |
| 4 | `TRAY_NUMBER` | DOUBLE | NOT NULL |  | Tray number of the Antibody Screen tray where the well or series of wells being defined are located. This will only be populated when inventory is mapped by column, row, or tray. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `X_POS` | DOUBLE | NOT NULL |  | The horizontal coordinate of a well or series of wells on an Antibody Screen which are being defined. This will only be populated when inventory is mapped by well or column. |
| 11 | `Y_POS` | DOUBLE | NOT NULL |  | The vertical coordinate of a well or series of wells on an Antibody Screen which are being defined. This will only be populated when inventory is mapped by well or row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CELL_ID` | [HLA_AB_SCRN_WELL_CELL](HLA_AB_SCRN_WELL_CELL.md) | `CELL_ID` |
| `LOT_NUMBER_ID` | [HLA_AB_SCREEN_TRAY_MAP](HLA_AB_SCREEN_TRAY_MAP.md) | `LOT_NUMBER_ID` |

