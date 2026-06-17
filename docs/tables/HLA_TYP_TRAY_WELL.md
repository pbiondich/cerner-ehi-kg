# HLA_TYP_TRAY_WELL

> Defines what is contained in a single tray well located on a specific HLA typing tray.

**Description:** HLA Typing Tray Well  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Relates the HLA Typing tray well to the inventory lot and related map. It is a foreign key reference to the primary key of the lot_number_info table. |
| 2 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | No longer used. |
| 3 | `SERUM_ID` | DOUBLE | NOT NULL | FK→ | Identifies in conjunction with manufacturer the unique serum contained in an HLA Typing tray well. Serum_id and manufacturer_cd are a foreign key reference to the primary key of the hla_tray_well_serum table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `X_POS` | DOUBLE | NOT NULL |  | The horizontal coordinate of a well on the HLA Typing tray being defined. |
| 10 | `Y_POS` | DOUBLE | NOT NULL |  | The vertical coordinate of a well on the HLA Typing tray being defined. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [HLA_TYP_TRAY_MAP](HLA_TYP_TRAY_MAP.md) | `LOT_NUMBER_ID` |
| `SERUM_ID` | [HLA_TRAY_WELL_SERUM](HLA_TRAY_WELL_SERUM.md) | `SERUM_ID` |

