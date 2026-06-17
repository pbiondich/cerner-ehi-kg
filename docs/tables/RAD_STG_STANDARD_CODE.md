# RAD_STG_STANDARD_CODE

> Contains codified values from an external source like FHIR and association to the RadNet staged data.

**Description:** RadNet Staging Standard Code  
**Table type:** ACTIVITY  
**Primary key:** `RAD_STG_STANDARD_CODE_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CODE_SYSTEM_TXT` | VARCHAR(100) |  |  | The standard code system that defines the meaning of the symbol in the code. |
| 3 | `CODE_TXT` | VARCHAR(80) |  |  | The standard code value which is a symbol in syntax defined by the system. |
| 4 | `DISPLAY_TXT` | VARCHAR(255) |  |  | The display text of the standard code that represents the meaning of the code. |
| 5 | `RAD_STG_STANDARD_CODE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RAD_STG_STANDARD_CODE table. |
| 6 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `VERSION_TXT` | VARCHAR(10) |  |  | The version of the standard code system. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RAD_STG_DATA](RAD_STG_DATA.md) | `EVENT_CD_STD_CD_ID` |
| [RAD_STG_DATA](RAD_STG_DATA.md) | `REPORT_STATUS_STD_CD_ID` |

