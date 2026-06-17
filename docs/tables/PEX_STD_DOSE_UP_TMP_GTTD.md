# PEX_STD_DOSE_UP_TMP_GTTD

> Used to efficiently transform data from a CSV file (joining with information from the Order_catalog_synonym, standardized_order_dose, and other tables) to facilitate populatin of the standardized_order_dose table.

**Description:** Standardized Dose Upload Temporary Global Temp Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BOTH_UNIT_CD` | DOUBLE |  |  | The unit CD if found or -1 if not found. Used to populate two fields in standardized_order_dose (compare_unit_cd and std_dose_unit_cd) |
| 2 | `BOTH_UNIT_DISP` | VARCHAR(40) |  |  | The CSV value which the script will attempt to match with a unit_cd |
| 3 | `COMPARE_VALUE1` | DOUBLE |  |  | The CSV entry which will go into the corresponding field in standardized_order_dose if the row meets business logic requirements. |
| 4 | `COMPARE_VALUE2` | DOUBLE |  |  | The CSV entry which will go into the corresponding field in standardized_order_dose if the row meets business logic requirements. |
| 5 | `COMPARE_VALUE2_SKIPPED_IND` | DOUBLE |  |  | Indicates that COMPARE_VALUE2 will be ignored because the relational operator was not "BETWEEN". |
| 6 | `CSV_ROW_NBR` | DOUBLE |  |  | Identifies which row of the CSV file the row came from. |
| 7 | `OCS_CKI` | VARCHAR(255) |  |  | The CSV entry which the script will attempt to match with order_catalog_synonym.CKI |
| 8 | `OCS_MNEMONIC` | VARCHAR(100) |  |  | The CSV entry which the script will attempt to match with order_catalog_synonym.mnemonic. |
| 9 | `RANGE_OPERATOR_DISP` | VARCHAR(80) |  |  | Capture what the user actually entered as Range Operator to be able to log wrong values later. |
| 10 | `RELATIONAL_OPERATOR_FLAG` | DOUBLE |  |  | Matches a subset of values in DM_FLAGS or -1 if not found; uses 1,4,6 as hard-coded in the Order Catalog Tool. 1=Less Than, 4=Greater than or equal to, 6=Between |
| 11 | `ROUTE_CD` | DOUBLE |  |  | The route CD if found or -1 if not found |
| 12 | `ROUTE_DISP` | VARCHAR(40) |  |  | The CSV entry which the script will attempt to match with a route_cd. |
| 13 | `STD_DOSE_VALUE` | DOUBLE |  |  | The CSV entry which will go into the corresponding field in standardized_order_dose if the row meets business logic requirements. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

