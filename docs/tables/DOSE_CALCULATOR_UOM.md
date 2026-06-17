# DOSE_CALCULATOR_UOM

> Contains the units of measure, conversion factors, and numerator/denominator units used by the dose calculator.

**Description:** Dose Calculator Unit of Measure  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `UOM_BASE_NBR` | DOUBLE | NOT NULL |  | Identifier of base unit. |
| 2 | `UOM_BRANCH_NBR` | DOUBLE | NOT NULL |  | Identifier of branch unit. All base units have a branch unit ID equal to one. |
| 3 | `UOM_CD` | DOUBLE | NOT NULL |  | Unit of Measure |
| 4 | `UOM_DENOMINATOR_CD` | DOUBLE | NOT NULL |  | The denominator code value of a previously defined base unit. |
| 5 | `UOM_MULTIPLY_FACTOR` | DOUBLE | NOT NULL |  | Value to multiply measurement by to convert a branch unit of measure to a base unit of measure. Base units of measure have a conversion factor of one. |
| 6 | `UOM_NUMERATOR_CD` | DOUBLE | NOT NULL |  | The numerator code value of a previously defined base unit. |
| 7 | `UOM_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag to indicate type of Unit. Current valid types are Patient Weight and Administered Volume |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

