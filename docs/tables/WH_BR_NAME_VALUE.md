# WH_BR_NAME_VALUE

> This table stores reusable name/value pairs

**Description:** WH_BR_NAME_VALUE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `BR_NAME` | VARCHAR(50) |  |  | the NAME portion of the name/value pair |
| 3 | `BR_NAME_VALUE_ID` | DOUBLE | NOT NULL |  | Unique identifer for the table |
| 4 | `BR_NV_KEY1` | VARCHAR(50) |  |  | identifies the type of name/value pair on this table |
| 5 | `BR_VALUE` | VARCHAR(100) |  |  | the VALUE portion of the name/value pair |
| 6 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which extracts were run. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 8 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The unique identifier that identifies a client health system id |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The unique identifier that identifies a client health system source id |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 11 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_USER` | VARCHAR(40) |  |  | The user that performs the insert or update to the record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

