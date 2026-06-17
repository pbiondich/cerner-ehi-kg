# BR_NAME_VALUE

> reusable name/value pairs

**Description:** BEDROCK NAME VALUE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** Identifies which bedrock client data belongs to |
| 2 | `BR_NAME` | VARCHAR(50) | NOT NULL |  | the ""name"" portion of the name/value pair |
| 3 | `BR_NAME_VALUE_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table |
| 4 | `BR_NV_KEY1` | VARCHAR(50) | NOT NULL |  | identifies the type of name/value pair on this table |
| 5 | `BR_VALUE` | VARCHAR(100) | NOT NULL |  | the ""value"" portion of the name/value pair |
| 6 | `DEFAULT_SELECTED_IND` | DOUBLE |  |  | Defined as 1 the name value should default in as selected. |
| 7 | `START_VERSION_NBR` | DOUBLE | NOT NULL |  | Identifies which version of start has been loaded |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

