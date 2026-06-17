# EXT_DATA_CODING

> Contains codified values from an external source (e.g. FHIR) and associates the value to a piece of externally staged data.

**Description:** External Data Coding  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CODE_TEXT` | VARCHAR(40) | NOT NULL |  | The codified value. |
| 3 | `CODING_SYSTEM_URI` | VARCHAR(255) | NOT NULL |  | The URI of the coding system. |
| 4 | `EXT_DATA_CODING_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the EXT_DATA_CODING table |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary key of the external data associated with this codified value. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the table associated with this codified value. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `VERSION_TEXT` | VARCHAR(10) | NOT NULL |  | The version of the coding system. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

