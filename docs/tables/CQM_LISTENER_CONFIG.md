# CQM_LISTENER_CONFIG

> The CQM listener configuration table identifies the verifiable alias of listener applications that are permitted to retrieve CQM transaction. Each alias is associated in this table with a CQM application and a trigger table.

**Description:** CQM Listener Configuration  
**Table type:** REFERENCE  
**Primary key:** `LISTENER_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NAME` | VARCHAR(12) | NOT NULL |  | The application name denotes a specific usage of CQM. This string is limited to twelve characters as it concatenated into DB table names to isolate the physical storage space of transaction by applicatio. |
| 2 | `COMM_PARAMS` | VARCHAR(200) |  |  | Identifies communications method and parameters that used by the trigger explosion process to notify the listener presented in this row. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 4 | `CURRENT_NODE` | VARCHAR(100) |  |  | Node on which the comserver is currently set to run |
| 5 | `LISTENER_ALIAS` | VARCHAR(48) | NOT NULL |  | The verifiable alias, by application name, which denotes a listener application that processes trigger exploded transactions. |
| 6 | `LISTENER_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the CQM listener configuration table. It is an internal system assigned number. |
| 7 | `LISTENER_IMAGE_NAME` | VARCHAR(132) |  |  | Future |
| 8 | `LISTENER_IMAGE_OPTIONS` | VARCHAR(132) |  |  | Future |
| 9 | `LISTENER_TRIGGER_TABLE_EXT` | VARCHAR(9) | NOT NULL |  | Denotes the extension string concatenated onto the listener trigger table name that denotes the physical storage space which the listener application identified in this row will receive its trigger events. This string is limited to nine characters. |
| 10 | `PRIMARY_NODE` | VARCHAR(100) |  |  | Node on which the listener should run under normal conditions. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CQM_LISTENER_REGISTRY](CQM_LISTENER_REGISTRY.md) | `LISTENER_ID` |
| [CQM_MDRESULTS_TR_1](CQM_MDRESULTS_TR_1.md) | `LISTENER_ID` |
| [CQM_MICRESULTS_TR_1](CQM_MICRESULTS_TR_1.md) | `LISTENER_ID` |

