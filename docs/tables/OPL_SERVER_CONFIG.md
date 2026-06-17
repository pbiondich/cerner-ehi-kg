# OPL_SERVER_CONFIG

> This table will store server configuration of openlink Engine (aka Designs) data for clients.

**Description:** OPENlink Server Configuration  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_PORT_NBR` | DOUBLE | NOT NULL |  | The design Server Alert port number, where OPENLink core engine can be requested design alerts. |
| 2 | `MACHINE_NAME` | VARCHAR(255) | NOT NULL |  | Host name of the OPENLink Engine |
| 3 | `OPL_SERVER_CONFIG_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the OPL_SERVER_CONFIG table. |
| 4 | `SERVER_DISPLAY_NAME` | VARCHAR(256) | NOT NULL |  | Display name of the OPENLink Engine server |
| 5 | `SERVER_NBR` | DOUBLE | NOT NULL |  | The design Server number managed by core OPENLink Engine |
| 6 | `SERVER_PORT_NBR` | DOUBLE | NOT NULL |  | The design Server port number, where the OPENLink core engine can be requested for all design status and operations. |
| 7 | `SERVER_SUB_TYPE_TXT` | VARCHAR(256) |  |  | Sub-Type of server design Example: ENTERPRISE, MILLENNIUM, MILLENNIUM_LEGACY, CLOUD |
| 8 | `SERVER_TYPE_TXT` | VARCHAR(256) | NOT NULL |  | Type of design Example: ENGINE, ADAPTER & PROXY |
| 9 | `TENANT_IDENT` | VARCHAR(128) | NOT NULL |  | Tenant indicator, identifies the tenant |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

