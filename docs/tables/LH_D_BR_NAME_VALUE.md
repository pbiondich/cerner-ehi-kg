# LH_D_BR_NAME_VALUE

> This table contains the information about br_eligible_provider

**Description:** LH_D_BR_NAME_VALUE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BNV_UPDT_DT_TM` | DATETIME |  |  | Date and time coming from br_name_value |
| 2 | `BNV_UPDT_ID` | DOUBLE |  |  | updt_id coming from br_name_value table |
| 3 | `BNV_UPDT_PRSNL_NAME` | VARCHAR(200) |  |  | Name coming from prsnl table |
| 4 | `BR_CLIENT_ID` | DOUBLE |  |  | Identifies which bedrock client data belongs to |
| 5 | `BR_NAME` | VARCHAR(50) |  |  | Name value coming br_name_value table |
| 6 | `BR_NAME_VALUE_ID` | DOUBLE |  |  | Date and time when the load was run and the row qualified |
| 7 | `BR_NV_KEY` | VARCHAR(50) |  |  | Key value coming br_name_value table |
| 8 | `BR_VALUE` | DOUBLE |  |  | Code Value coming from br_name_value table |
| 9 | `BR_VALUE_TEXT` | VARCHAR(50) |  |  | Display of the br_value field |
| 10 | `DEFAULT_SELECTED_IND` | DOUBLE |  |  | Defined as 1 the name value should default in as selected. |
| 11 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and time when the load was run |
| 12 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data |
| 13 | `LH_D_BR_NAME_VALUE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 14 | `PROCESS_DT_TM` | DATETIME |  |  | Process date and time |
| 15 | `START_VERSION_NBR` | DOUBLE |  |  | Identifies which version of start has been loaded |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_SOURCE` | VARCHAR(100) |  |  | Source through which the row was updated |
| 19 | `UPDT_TASK` | VARCHAR(100) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

