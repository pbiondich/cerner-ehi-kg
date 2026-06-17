# HLA_TYP_TRAY_MAP

> Further defines an inventory lot as being an HLA typing tray and specifies the dimensions of the tray.

**Description:** HLA Typing Tray Map  
**Table type:** REFERENCE  
**Primary key:** `LOT_NUMBER_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies the inventory lot of the HLA Typing tray for which the mapping is being defined. It is a foreign key reference to the primary key of the lot_number_info table. |
| 2 | `QC_IND` | DOUBLE |  |  | Indicates whether or not quality control procedures have been performed on the typing tray. |
| 3 | `TRAY_ABBREVIATION` | CHAR(20) |  |  | The abbreviation given an HLA Tying tray . This abbreviation will be used to identify the tray when it used in testing. |
| 4 | `TRAY_ORIENTATION_CD` | DOUBLE | NOT NULL |  | Specifies the default direction the tray is rotated when placed on the microscope. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `X_ALPHA_IND` | DOUBLE |  |  | Indicates whether the horizontal coordinates of the HLA Typing tray should be represented as characters. |
| 11 | `X_DIM` | DOUBLE |  |  | Horizontal dimension of the HLA Typing tray. |
| 12 | `Y_ALPHA_IND` | DOUBLE |  |  | Indicates whether the vertical coordinates of the HLA Typing tray should be represented as characters. |
| 13 | `Y_DIM` | DOUBLE |  |  | Vertical dimension of the HLA Typing tray. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HLA_TYP_RES_TRAY](HLA_TYP_RES_TRAY.md) | `LOT_NUMBER_ID` |
| [HLA_TYP_TRAY_WELL](HLA_TYP_TRAY_WELL.md) | `LOT_NUMBER_ID` |

