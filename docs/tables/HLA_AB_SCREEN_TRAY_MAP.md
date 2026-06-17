# HLA_AB_SCREEN_TRAY_MAP

> Further defines an inventory lot as being an HLA antibody screen tray or trays, and specifies the dimensions of the tray(s) and how the tray(s) are mapped.

**Description:** HLA Antibody Screen Tray Map  
**Table type:** REFERENCE  
**Primary key:** `LOT_NUMBER_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILL_METHOD_FLAG` | DOUBLE | NOT NULL |  | Flag to enable batches to be filled by column in HLA Antibody Screen Batch Build. 0 = fill by row; 1 = fill by column |
| 2 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | PK FK→ | Uniquely identifies the record. It is a foreign key reference to the primary key of the lot_number_info table. |
| 3 | `QC_IND` | DOUBLE |  |  | Indicates whether or not quality control procedures have been performed on the antibody screen. |
| 4 | `TRAY_ABBREVIATION` | CHAR(20) |  |  | The abbreviation given an HLA Antibody Screen tray or batch of trays. This abbreviation will be used to identify the Antibody Screen when it used in testing. |
| 5 | `TRAY_COUNT` | DOUBLE |  |  | The number of trays which make up the Antibody Screen. |
| 6 | `TRAY_ORIENTATION_CD` | DOUBLE | NOT NULL |  | Specifies the default direction a tray within the batch is rotated when placed on the microscope. |
| 7 | `TRAY_TYPE_CD` | DOUBLE | NOT NULL |  | The code for the method used in mapping the tray(s) in the Antibody Screen. Antibody Screen trays may be mapped by well, by column, by row, or by tray. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `X_ALPHA_IND` | DOUBLE |  |  | Indicates whether the horizontal coordinates of each tray should be represented as characters. |
| 14 | `X_DIM` | DOUBLE |  |  | Horizontal dimension of each tray included in the Antibody Screen. |
| 15 | `Y_ALPHA_IND` | DOUBLE |  |  | Indicates whether the vertical coordinates of each tray should be represented as characters. |
| 16 | `Y_DIM` | DOUBLE |  |  | Vertical dimension of each tray included in the Antibody Screen. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HLA_AB_SCRN_WELL](HLA_AB_SCRN_WELL.md) | `LOT_NUMBER_ID` |

