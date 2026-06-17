# TRANSFER_LIST_AUTO_BUILD

> Contains the parameters for auto-building transfer lists from robotics messages.

**Description:** Transfer List Auto Build  
**Table type:** REFERENCE  
**Primary key:** `TRANSFER_LIST_AUTO_BUILD_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FROM_LOCATION_CD` | DOUBLE | NOT NULL |  | Indicates the starting location to be used for the transfer lists. |
| 5 | `MAX_CONTAINER_NBR` | DOUBLE | NOT NULL |  | The maximum number of containers that an auto-built transfer list based off of this configuration will accept. |
| 6 | `ROUTE_CODE_TXT` | VARCHAR(40) | NOT NULL |  | The route code text for which the parameters apply. |
| 7 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The unique identifier for the service resource for which the parameters apply. |
| 8 | `TO_LOCATION_CD` | DOUBLE | NOT NULL |  | Indicates the location the containers will be sent to. |
| 9 | `TRANSFER_LIST_AUTO_BUILD_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies parameters for auto-building transfer lists from robotics messages. |
| 10 | `TRANSFER_TEMP_CD` | DOUBLE | NOT NULL |  | Indicates the transfer temperature the transfer list will use. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [COLLECTION_LIST](COLLECTION_LIST.md) | `TRANSFER_LIST_AUTO_BUILD_ID` |

