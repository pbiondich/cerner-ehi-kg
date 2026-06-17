# BR_AUTO_RLI_ALIAS

> This table contains all of the alias value mappings for a reference lab's orderable items. This is an autobuild content table used in the Bedrock reference lab interface table.

**Description:** Bedrock Auto RLI Alias  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Flag value to indicate whether the value is aliased to an existing code_value or a newly created code_value.0 |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ALIAS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the alias. |
| 4 | `ALIAS_NAME` | VARCHAR(100) |  |  | The alias value. |
| 5 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 6 | `CDF_MEANING` | VARCHAR(12) |  |  | If applicable, the CDF_MEANING of the code_value to which the alias is related. |
| 7 | `CODE_SET` | DOUBLE | NOT NULL |  | The code_set number to which the alias is related. |
| 8 | `CODE_VALUE` | DOUBLE | NOT NULL |  | The code_value to which the alias is related. |
| 9 | `DEFINITION` | VARCHAR(100) |  |  | The definition of the code_value to which the alias is related. |
| 10 | `DESCRIPTION` | VARCHAR(60) |  |  | The description of the code_value to which the alias is related. |
| 11 | `DISPLAY` | VARCHAR(40) |  |  | The display of the code_value to which the alias is related. |
| 12 | `SUPPLIER_FLAG` | DOUBLE | NOT NULL |  | Flag value used to identify the reference lab. |
| 13 | `UNIT_MEANING` | VARCHAR(12) |  |  | The meaning for a unit of measure if the alias is related to a value on code set 54. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

