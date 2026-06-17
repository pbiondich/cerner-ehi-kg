# LH_AMB_FILTER_PARAMS

> This table holds parameters for the LH_AMB_FILTER program.

**Description:** LH_AMB_FILTER_PARAMS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EXTRACT_DT_TM` | DATETIME |  |  | The start of the extract period. |
| 2 | `BIRTHDATE_HIGH_DT_TM` | DATETIME |  |  | The highest value for Patient Birth Date Time. |
| 3 | `BIRTHDATE_LOW_DT_TM` | DATETIME |  |  | The lowest value for Patient Birth Date Time. |
| 4 | `END_EXTRACT_DT_TM` | DATETIME |  |  | The end of the extract period. |
| 5 | `ETHNICITY_CD` | DOUBLE |  |  | CODE_VALUE for Patient Ethnicity Filter. |
| 6 | `FILE_TEXT` | VARCHAR(50) |  |  | The text to associate with records . |
| 7 | `GENDER_ITEM_ID` | DOUBLE | NOT NULL |  | BR_DATAM_VAL_SET_ITEM_ID for Patient Gender Filter. |
| 8 | `INSURANCE_ITEM_ID` | DOUBLE | NOT NULL |  | BR_DATAM_VAL_SET_ITEM_ID for Patient Insurance Filter. |
| 9 | `LH_AMB_FILTER_PARAMS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_AMB_FILTER_PARAMS table. |
| 10 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The id to associate with Parent Entity Name. |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The table to associate with Parent Entity ID. |
| 13 | `PRINT_OPTION` | VARCHAR(10) |  |  | The format in which to print results. |
| 14 | `PROBLEM_VSET_ID` | DOUBLE | NOT NULL |  | BR_DATAM_VAL_SET_ID for Patient Problem Filter. |
| 15 | `RACE_CD` | DOUBLE |  |  | CODE_VALUE for Patient Race Filter. |
| 16 | `REPORT_BY` | VARCHAR(20) |  |  | The Reporting Option. |
| 17 | `REPORT_MODE` | VARCHAR(20) |  |  | The mode for which to run LH_AMB_FILTER. |
| 18 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

