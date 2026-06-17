# SI_OEN_CONTEXT

> Defines the comservers that exist in the domain

**Description:** Open Engine Context  
**Table type:** REFERENCE  
**Primary key:** `SI_OEN_CONTEXT_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_PARAMS` | VARCHAR(255) |  |  | CONTEXT ADDITIONAL PARAMS |
| 2 | `CONTEXT_NAME` | VARCHAR(100) | NOT NULL |  | Unique Name of the comserver |
| 3 | `CURRENT_NODE` | VARCHAR(100) |  |  | The name of the node that the comserver is currently being run on. |
| 4 | `DESCRIPTION` | VARCHAR(255) |  |  | Description of the comserver |
| 5 | `FAILOVER_LAUNCH_ENTRY` | VARCHAR(100) |  |  | IDENTIFIER FOR THE FAIL OVER LAUNCH ENTRY |
| 6 | `LAUNCH_ENTRY` | VARCHAR(100) |  |  | The identifier for the entry that the comserver will be launched by. For example an scp id |
| 7 | `LAUNCH_ENTRY_TYPE` | VARCHAR(31) |  |  | The type of entry used to launch the comserver |
| 8 | `RESOURCE_GROUP` | VARCHAR(100) |  |  | The resource group that the comserver runs in. This is usually equal to the node that it should run on. |
| 9 | `SERVICE_URL` | VARCHAR(255) | NOT NULL |  | The RMI url for connecting to the comserver |
| 10 | `SI_OEN_CONTEXT_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SI_OEN_COMCHANNEL](SI_OEN_COMCHANNEL.md) | `SI_OEN_CONTEXT_ID` |
| [SI_OEN_ENDPOINT](SI_OEN_ENDPOINT.md) | `SI_OEN_CONTEXT_ID` |
| [SI_OEN_WORK_POOL](SI_OEN_WORK_POOL.md) | `SI_OEN_CONTEXT_ID` |

