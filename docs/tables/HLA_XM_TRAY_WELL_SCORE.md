# HLA_XM_TRAY_WELL_SCORE

> Records the individual well scores as part of the raw result data specific to HLA crossmatch for an order.

**Description:** HLA Crossmatch Tray Well Score  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DILUTION_CD` | DOUBLE | NOT NULL |  | The code for the dilution that used for the order at this batch placement. |
| 2 | `HLA_AB_SCREEN_ID` | DOUBLE | NOT NULL | FK→ | The ID of the Antibody Screen that is placed in a Crossmatch Inventory item at a specific tray position. It is only used for Antibody Screens that are manually entered or uploaded from a contributor system and not for those associated with an order. It is a foreign key reference to the primary key of the Person HLA Ab Screen table. |
| 3 | `HLA_XM_RES_TRAY_ID` | DOUBLE | NOT NULL | FK→ | Relates the HLA Crossmatch tray well to the inventory lot and related map. It is a foreign key reference to the primary key of the hla_xm_res_tray table. |
| 4 | `LOT_ID` | DOUBLE | NOT NULL | FK→ | Contains a reference to the CONTROL_LOT table. |
| 5 | `METHODOLOGY_CD` | DOUBLE | NOT NULL |  | The code for the methodology that used for the order at this batch placement. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the Order that is placed in a Crossmatch batch at a specific tray position. It is a foreign key reference to the primary key of the orders table. |
| 7 | `QC_ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | The ID of the QC Accession related to a QC Control that is placed in a Crossmatch batch at a specific tray position. It is a foreign key reference to the primary key of the Accession table. |
| 8 | `TRAY_NUMBER` | DOUBLE | NOT NULL |  | The tray of a well on the HLA Crossmatch tray being defined. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `WELL_SCORE_CD` | DOUBLE | NOT NULL |  | The code for the well score given to this HLA crossmatch tray well. |
| 15 | `X_POS` | DOUBLE | NOT NULL |  | Horizontal coordinate of the well being scored. |
| 16 | `Y_POS` | DOUBLE | NOT NULL |  | Vertical coordinate of the well being scored. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HLA_AB_SCREEN_ID` | [PERSON_HLA_AB_SCREEN](PERSON_HLA_AB_SCREEN.md) | `HLA_AB_SCREEN_ID` |
| `HLA_XM_RES_TRAY_ID` | [HLA_XM_RES_TRAY](HLA_XM_RES_TRAY.md) | `HLA_XM_RES_TRAY_ID` |
| `LOT_ID` | [CONTROL_LOT](CONTROL_LOT.md) | `LOT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `QC_ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |

