# DMS_SERVICE

> Contains a list of the various distribution services in the Digital Media Service sub-system.

**Description:** Digital media services Service table.  
**Table type:** REFERENCE  
**Primary key:** `DMS_SERVICE_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESTINATION_SERVER_NAME` | VARCHAR(32) |  |  | The name of the destination print server for external printing use. |
| 2 | `DMS_SERVICE_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the row. |
| 3 | `HOST_NAME` | VARCHAR(64) | NOT NULL |  | The host name for this distribution service. |
| 4 | `SERVICE_NAME` | VARCHAR(64) | NOT NULL |  | The name of the distribution service that this row refers to. |
| 5 | `SERVICE_TYPE` | VARCHAR(32) | NOT NULL |  | The type of service that this distribution service refers to. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DEVICE](DEVICE.md) | `DMS_SERVICE_ID` |

