# OMF_PVB_COL_INFO

> Column information about scheduled results sets from PowerVision.

**Description:** OMF PVB COL INFO  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIGN_FLAG` | DOUBLE |  |  | Not currently used. |
| 2 | `BATCH_ID` | DOUBLE | NOT NULL |  | ID of the result set this column info comes from. |
| 3 | `CI_SEQ` | DOUBLE | NOT NULL |  | Sequence used to provide uniqueness. |
| 4 | `DATA_COL` | DOUBLE |  |  | Position in list of visible facts and dimensions for this result_set. |
| 5 | `DATA_TYPE_FLAG` | DOUBLE |  |  | Data type of this column. |
| 6 | `DISPLAY_IND` | DOUBLE |  |  | Indicates whether this column is visible. |
| 7 | `FACT_IND` | DOUBLE |  |  | Indicates whether this is a fact or dimension. |
| 8 | `FORMAT` | VARCHAR(255) |  |  | Formatting to apply to this column. |
| 9 | `FORM_MAP_NAME` | VARCHAR(255) |  |  | String to refer to in formulas. |
| 10 | `HELP_DESC_STR` | VARCHAR(255) |  |  | Help description for this column. |
| 11 | `NAME` | VARCHAR(255) |  |  | Name of column. |
| 12 | `PVFORMULA1` | VARCHAR(255) |  |  | Formula string. |
| 13 | `PVFORMULA2` | VARCHAR(255) |  |  | Formula string2. |
| 14 | `PVFORMULA3` | VARCHAR(255) |  |  | Formula string3. |
| 15 | `PVFORMULA4` | VARCHAR(255) |  |  | Formula string4. |
| 16 | `TOTALS_STR` | VARCHAR(40) |  |  | Not currently used. |
| 17 | `VO_GROUP_ID` | DOUBLE | NOT NULL |  | Template folder which holds this column. |
| 18 | `VO_ID` | DOUBLE | NOT NULL |  | Indicator_cd for the column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

