# OEN_SCRIPT_LIST

> script list

**Description:** Holds all Open Engine scripts.  
**Table type:** REFERENCE  
**Primary key:** `SCRIPT_ID`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BUILD_DT_TM` | DATETIME |  |  | Time stamp of script compile/build/include. |
| 3 | `BUILD_VERSION_NBR` | DOUBLE |  |  | Incremented when a build of the script is done.Column |
| 4 | `EXECUTABLE_IND` | DOUBLE | NOT NULL |  | Indicates if script can be compiled/included |
| 5 | `PREV_BUILD_VERSION_NBR` | DOUBLE |  |  | Version number of the previous build on the script.Column |
| 6 | `PRODUCTION_IND` | DOUBLE |  |  | Indicates if script is being used in production |
| 7 | `READ_ONLY_IND` | DOUBLE | NOT NULL |  | Indicator to allow script only as read privileged. |
| 8 | `SCRIPT_DESC` | VARCHAR(80) |  |  | Description of the script. |
| 9 | `SCRIPT_ID` | DOUBLE | NOT NULL | PK | Script ID |
| 10 | `SCRIPT_NAME` | VARCHAR(32) | NOT NULL |  | Name of the Script. |
| 11 | `SCRIPT_TYPE` | DOUBLE | NOT NULL |  | The type of Script: ModOrig-Inbound MaptoLib ModObj-Inbound ModObj-Outbound MapfrLib ModOrig-Outbound Type Ack Route CCLOpen CCLRead CCLSend CCLReset CCLClose AddSeqNbr CustomStartup CheckStartup GenerateStartup MaptoUI MapfrUI MapUItoUI RemoteAck Generic |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VERSION_NBR` | DOUBLE |  |  | Version number of the script. Updated when the script is check into/outof production. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OEN_INTERFACE_SCR_R](OEN_INTERFACE_SCR_R.md) | `SCRIPT_ID` |
| [OEN_SCRIPT_BODY](OEN_SCRIPT_BODY.md) | `SCRIPT_ID` |

