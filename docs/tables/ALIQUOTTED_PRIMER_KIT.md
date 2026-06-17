# ALIQUOTTED_PRIMER_KIT

> Further defines an inventory lot as being an HLA molecular testing primer kit that has been aliquotted.

**Description:** Aliquotted Primer Kit  
**Table type:** REFERENCE  
**Primary key:** `LOT_NUMBER_ID`  
**Columns:** 13  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GEL_X_DIM` | DOUBLE |  |  | Default number of columns for a Gel this aliquotted primer kit placed on. |
| 2 | `GEL_Y_DIM` | DOUBLE |  |  | Default number of rows for a Gel this aliquotted primer kit placed on. |
| 3 | `KIT_ABBREVIATION` | CHAR(20) |  |  | The abbreviation given an HLA molecular primer kit. This abbreviation will be used to identify the aliquotted kit's primer tubes when they are placed in racks or on gels. |
| 4 | `LOCI_CD` | DOUBLE | NOT NULL |  | The code for a specific HLA Loci that the aliquotted primer kit tests for. |
| 5 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | PK FK→ | Uniquely identifies the record. It is a foreign key reference to the primary key of the lot_number_info table. |
| 6 | `QC_IND` | DOUBLE |  |  | Indicates whether or not quality control procedures have been performed on the aliquotted primer kit. |
| 7 | `TUBE_COUNT` | DOUBLE |  |  | The number of tubes contained in the aliquotted primer kit. |
| 8 | `TUBE_START` | DOUBLE |  |  | The starting position of the first tube in the aliquotted primer kit. Primer kits may be broken into separate aliquotted kits. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [GEL_LOADING_POSN](GEL_LOADING_POSN.md) | `LOT_NUMBER_ID` |
| [PRIMER_KIT_SPECIFICITY](PRIMER_KIT_SPECIFICITY.md) | `LOT_NUMBER_ID` |
| [THERMO_RACK_PLACEMENT](THERMO_RACK_PLACEMENT.md) | `LOT_NUMBER_ID` |
| [TUBE_INFORMATION](TUBE_INFORMATION.md) | `LOT_NUMBER_ID` |

