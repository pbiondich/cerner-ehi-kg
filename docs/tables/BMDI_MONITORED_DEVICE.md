# BMDI_MONITORED_DEVICE

> Identifies all BMDI devices, including their locations and aliases.

**Description:** BMDI Monitored Device  
**Table type:** REFERENCE  
**Primary key:** `MONITORED_DEVICE_ID`  
**Columns:** 17  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALTERNATE_DEVICE_CD` | DOUBLE | NOT NULL | FK→ | Identifies alternate data port for the device. For example, used to accept demographic data received by the device in response to an appropriate request while the main device port identified by device_cd is used for clinical data sent out. (FK from SERVICE_RESOURCE) |
| 2 | `ASSOCIATION_LIMIT_CNT` | DOUBLE | NOT NULL |  | Determines maximum number of solution associations with the monitored device at a time - most common value is 1 |
| 3 | `DEVICE_ALIAS` | VARCHAR(40) | NOT NULL |  | An alias sent by the device to identify itself. |
| 4 | `DEVICE_CD` | DOUBLE | NOT NULL | FK→ | Used to identify which physical locations and device aliases are serviced by a service resource |
| 5 | `DEVICE_IND` | DOUBLE | NOT NULL |  | Identify device versus monitor. Device = 1, Monitor = 0. |
| 6 | `DEVICE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of the device |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Specifies the physical location of this bmdi device alias. |
| 8 | `MOBILE_IND` | DOUBLE | NOT NULL |  | Identifies if this device can be mobile. |
| 9 | `MONITORED_DEVICE_ID` | DOUBLE | NOT NULL | PK | the primary key |
| 10 | `RESOURCE_LOC_CD` | DOUBLE | NOT NULL |  | Specifies the physical location of this device alias. |
| 11 | `STRT_MODEL_CHILD_ID` | DOUBLE | NOT NULL | FK→ | Identify child device model. Primary key in STRT_MODEL database table |
| 12 | `STRT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | Identify device to model. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALTERNATE_DEVICE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `DEVICE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `STRT_MODEL_CHILD_ID` | [STRT_MODEL](STRT_MODEL.md) | `STRT_MODEL_ID` |
| `STRT_MODEL_ID` | [STRT_MODEL](STRT_MODEL.md) | `STRT_MODEL_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BMDI_ACQUIRED_DATA_TRACK](BMDI_ACQUIRED_DATA_TRACK.md) | `MONITORED_DEVICE_ID` |
| [BMDI_ACQUIRED_RESULTS](BMDI_ACQUIRED_RESULTS.md) | `MONITORED_DEVICE_ID` |
| [SA_REF_DEVICE](SA_REF_DEVICE.md) | `MONITORED_DEVICE_ID` |

