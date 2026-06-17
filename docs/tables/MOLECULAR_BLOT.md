# MOLECULAR_BLOT

> Further defines an inventory lot as being an HLA molecular testing blot.

**Description:** Molecular Blot  
**Table type:** REFERENCE  
**Primary key:** `LOT_NUMBER_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOT_ABBREVIATION` | CHAR(20) |  |  | The abbreviation given an HLA molecular blot. This abbreviation will be used to identify the blot when it is used in testing. |
| 2 | `FILL_COLUMN_IND` | DOUBLE | NOT NULL |  | Indicator to enable batches to be filled by column in Blot Batch Build0 = fill by row1 = fill by column |
| 3 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | PK FK→ | Uniquely identifies the record. It is a foreign key reference to the primary key of the lot_number_info table. |
| 4 | `NORMAL_BLOT_IND` | DOUBLE |  |  | Indicates whether the Molecular Blot is a Normal Dot Blot or Reverse Dot Blot. 0 = Reverse, 1 = Normal. |
| 5 | `PROBE_COUNT` | DOUBLE |  |  | The number of probes contained in the blot. |
| 6 | `QC_IND` | DOUBLE |  |  | Indicates whether or not quality control procedures have been performed on the molecular blot. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `X_ALPHA_IND` | DOUBLE |  |  | Indicates whether the horizontal coordinates of the Molecular Blot should be represented as characters. |
| 13 | `X_DIM` | DOUBLE |  |  | Horizontal dimension of the Molecular Blot |
| 14 | `Y_ALPHA_IND` | DOUBLE |  |  | Indicates whether the vertical coordinates of the Molecular Blot should be represented as characters. |
| 15 | `Y_DIM` | DOUBLE |  |  | Vertical dimension of the Molecular Blot. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BLOT_SPECIFICITY](BLOT_SPECIFICITY.md) | `LOT_NUMBER_ID` |
| [BLOT_STRIP](BLOT_STRIP.md) | `LOT_NUMBER_ID` |
| [PROBE_INFORMATION](PROBE_INFORMATION.md) | `LOT_NUMBER_ID` |

