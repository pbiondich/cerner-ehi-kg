# OMF_INDICATOR

> Contains PowerVision indicators definitions.

**Description:** OMF INDICATOR  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALIGN_FLAG` | DOUBLE |  |  | Indicates view column alignment for PowerVision views. |
| 2 | `COLUMN_STR` | VARCHAR(255) |  |  | Column's name with a table abbreviation attached. Will be used in a CCL select statement. |
| 3 | `DATA_TYPE_FLAG` | DOUBLE |  |  | Indicator"s data type. |
| 4 | `FACT_IND` | DOUBLE |  |  | Is this indicator a fact or not? Can it be Summed, Averaged,etc. |
| 5 | `FILTER_DESCRIPTION` | VARCHAR(100) |  |  | Display value of the indicator in PowerVision if this indicator is filterable and not related to a template item.. |
| 6 | `FILTER_IND` | DOUBLE |  |  | Indicates whether the indicator is filterable in PowerVision. |
| 7 | `FILTER_MEANING` | VARCHAR(50) |  |  | Generic meaning of an indicator if its filterable. E.g. NURSE UNIT, DETAIL PROCEDURE, PHYSICIAN, PATIENT, etc. |
| 8 | `FORMAT` | VARCHAR(50) |  |  | Format to display the indicator in PowerVision. |
| 9 | `GENERIC_OPERAND` | VARCHAR(20) |  |  | Operand (e.g. +, -, *, /) to use for generic indicators such as turnaround time indicators. |
| 10 | `GROUP_BY_IND` | DOUBLE |  |  | Indicates whether this indicator can be group-ed by (e.g. an patient id could but a patient name shouldn't since patients can share names). |
| 11 | `GROUP_BY_STR` | VARCHAR(255) |  |  | Value to use in group by if the column_str is not usable (e.g. if the column_str is a function). |
| 12 | `GROUP_IND` | DOUBLE |  |  | Is this indicator a group of indicators? Not used. |
| 13 | `HELP_DESCRIPTION_STR` | VARCHAR(255) |  |  | Help descriptions for bubble help in PowerVision. |
| 14 | `INDICATOR_CD` | DOUBLE | NOT NULL |  | Indicator's code value. cdf_meaning=INDICATOR, display= . Other codesets can be used besides 14265 depending on the team defining the value. |
| 15 | `INDICATOR_TYPE_CD` | DOUBLE | NOT NULL |  | Tells the type of indicator this is (e.g. RAW, GENERIC, etc.) cdf_meaning = . |
| 16 | `KEY_INDICATOR_CD` | DOUBLE | NOT NULL |  | Indicator code value of the indicator that this column is associated with. Would only be filled out when, e.g., the indicator is the physician name, then this column would be the indicator code value of the physician id. Used for PowerVision. |
| 17 | `SELECT_LIST_NAME` | VARCHAR(12) |  |  | No longer used. Column alias name to use in CCL selects. For example, 'select = from table1' |
| 18 | `SG_TYPE` | VARCHAR(50) |  |  | Study Group type such as PATIENT, PHYSICIAN,etc. Also used to allow drill path connections. |
| 19 | `SORT_FLAG` | DOUBLE |  |  | Sorting method - 0 by description/indicator; 1 = by id/key_indicator |
| 20 | `STR_SEQ` | DOUBLE | NOT NULL |  | Order to put together strings if an indicator's column_str value is greater than 255 characters. |
| 21 | `TOTALS_CD` | DOUBLE | NOT NULL |  | Total method to display in PowerVision (e.g. COUNT, SUM, FORMULA TOT, etc.) |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

