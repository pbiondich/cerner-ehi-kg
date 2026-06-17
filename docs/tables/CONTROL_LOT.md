# CONTROL_LOT

> Defines the lot of a control material.

**Description:** Control Material Lot  
**Table type:** REFERENCE  
**Primary key:** `LOT_ID`  
**Columns:** 14  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTROL_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific control material with which the control lot is associated. |
| 2 | `EXPIRATION_DT_TM` | DATETIME |  |  | Defines the date and time the control material lot will expire and be unavailable for resulting. |
| 3 | `LOT_FLAG` | DOUBLE |  |  | Defines the status of the lot added to the control material. |
| 4 | `LOT_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific control lot. |
| 5 | `LOT_NUMBER` | VARCHAR(200) |  |  | Character description of the lot number as defined by the manufacturer of the lot. |
| 6 | `MANUFACTURE_EXP_DT_TM` | DATETIME |  |  | Defines the manufacture expiry date and time of the control material lot. |
| 7 | `PREV_LOT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the lot previous to the current lot in order to see the relationship between lots. |
| 8 | `RECEIVE_DT_TM` | DATETIME |  |  | The date and time the control lot was received and implemented by the system. |
| 9 | `SHORT_DESCRIPTION` | VARCHAR(20) |  |  | Defines a short character description of the lot material. (Currently not implemented) |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTROL_ID` | [CONTROL_MATERIAL](CONTROL_MATERIAL.md) | `CONTROL_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [ASSAY_RESOURCE_LOT](ASSAY_RESOURCE_LOT.md) | `LOT_ID` |
| [HLA_XM_TRAY_WELL](HLA_XM_TRAY_WELL.md) | `LOT_ID` |
| [HLA_XM_TRAY_WELL_SCORE](HLA_XM_TRAY_WELL_SCORE.md) | `LOT_ID` |
| [QC_RESULT](QC_RESULT.md) | `LOT_ID` |
| [QC_STAT_PERIOD](QC_STAT_PERIOD.md) | `LOT_ID` |
| [RESOURCE_LOT_R](RESOURCE_LOT_R.md) | `LOT_ID` |

