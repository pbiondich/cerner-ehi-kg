# PEX_STD_DOSE_UP_MATCH_GTTD

> Used to efficiently transform data from a CSV file (joining with information from the Order_catalog_synonym, standardized_order_dose, and other tables) to facilitate populatin of the standardized_order_dose table; stores information on matches which may not be one-to-one with the STD_DOSE_UPLOAD_TMP table

**Description:** Standardized Dose Upload Matches Global Temporary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CSV_ROW_NBR` | DOUBLE |  |  | Identifies which row of the CSV file the row came from. |
| 2 | `MATCH_FLAG` | DOUBLE |  |  | Captures whether the match was found via CKI or mnemonic. 0 = CKI, 1 = Mnemonic |
| 3 | `SKIP_FLAG` | DOUBLE |  |  | Indicates whether business logic requires the data to NOT be populated into the standardized_order_table and the reason. 0 indicates that the row should not be skipped as long as all other columns are valid. Value 0: Row should not be skipped, 1=Combination of synonym_id and route_cd already exists in the synonym_order_dose table. 2=Duplication in the CSV file itself that would violate the unique constraint in synonym_order_dose. |
| 4 | `SYNONYM_ID` | DOUBLE |  |  | Defines what type of domain setting a configuration is (view,detail, viewcomp, message center etc.) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

