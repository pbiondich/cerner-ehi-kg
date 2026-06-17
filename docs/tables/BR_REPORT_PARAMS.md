# BR_REPORT_PARAMS

> Stores the type of parameter to be used in the bedrock reports

**Description:** Bedrock Report Parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `BR_REPORT_ID` | DOUBLE | NOT NULL |  | Unique id from br_report |
| 3 | `CAPTION` | VARCHAR(100) |  |  | The string that will be displayed to the end user when prompting for data like 'Facility' or 'Organization'. |
| 4 | `CODE_SET` | DOUBLE | NOT NULL |  | Code set number for a CODESET Parameter |
| 5 | `MULTIPLE_VALUE_IND` | DOUBLE |  |  | 1 if more than one value is valid |
| 6 | `PARAM_TYPE_MEAN` | VARCHAR(20) | NOT NULL |  | Type of parameter (CODESET,FACILITY,DATE, etc..) |
| 7 | `REQUIRED_IND` | DOUBLE |  |  | 1 if at least one value is required |
| 8 | `SEQUENCE` | DOUBLE |  |  | Orders the parameters |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

