# OEN_PROCINFO

> This table contains the information for the open engine interfaces.

**Description:** open engine interface info  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTROLLABLE` | DOUBLE |  |  | Future |
| 2 | `CURRENT_NODE` | VARCHAR(15) |  |  | Node on which the comserver is currently set to run |
| 3 | `INTERFACEID` | DOUBLE | NOT NULL |  | Unique identifier for interface. Not popped from a sequence. Incrementing number but if there are gaps, those numbers are used. |
| 4 | `PRIMARY_NODE` | VARCHAR(15) |  |  | Node on which the comserver should run under normal conditions. |
| 5 | `PRIMARY_SCP_EID` | DOUBLE |  |  | SCP entry ID of the comserver on the primary node |
| 6 | `PROC_DESC` | VARCHAR(80) |  |  | Description of the interface |
| 7 | `PROC_NAME` | CHAR(32) | NOT NULL |  | Unique interface name |
| 8 | `QUERYABLE` | DOUBLE |  |  | Future: |
| 9 | `SCP_EID` | DOUBLE | NOT NULL |  | Unique scp id for the interface |
| 10 | `SERVICE` | CHAR(10) | NOT NULL |  | Service provided by the interface |
| 11 | `STD_INTERFACEID` | DOUBLE | NOT NULL |  | STD_INTERFACEID |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT` | CHAR(10) |  |  | The date interface was created or updated. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TM` | CHAR(8) |  |  | The time interface was created or updated. |
| 19 | `USER_NAME` | CHAR(15) |  |  | The user who created or last updated the interface. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

