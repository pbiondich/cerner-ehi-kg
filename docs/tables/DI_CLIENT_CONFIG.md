# DI_CLIENT_CONFIG

> Configuration information mapping Enterprise Device Connectivity devices to Millenium Service Requests

**Description:** Device Integration Client Configuration  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DEVICE_NAME` | VARCHAR(256) | NOT NULL |  | EDC Device Name |
| 3 | `DI_CLIENT_CONFIG_ID` | DOUBLE | NOT NULL |  | Unique Device Integration Client Configuration ID. Primary key for this table. |
| 4 | `EDC_ENVIRONMENT` | VARCHAR(255) |  |  | EDC ENVIRONMENT NAME |
| 5 | `EDC_SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | EDC Service Type code from codeset 4002001 |
| 6 | `SAMPLE_PERIOD` | DOUBLE | NOT NULL |  | Minimum time since last sample was posted in seconds. |
| 7 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Service Resource Code from SERVICE_RESOURCE table |
| 8 | `SUBSCRIPTION_NAME` | VARCHAR(256) | NOT NULL |  | EDC Subscription Name |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

