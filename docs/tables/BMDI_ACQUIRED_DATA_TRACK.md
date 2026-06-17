# BMDI_ACQUIRED_DATA_TRACK

> Association of Device to person/alternate record Identifiers.

**Description:** BMDI Acquired Data Track  
**Table type:** ACTIVITY  
**Primary key:** `ASSOCIATION_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSOCIATION_DT_TM` | DATETIME | NOT NULL |  | This is the date and time the association is created. |
| 3 | `ASSOCIATION_ID` | DOUBLE | NOT NULL | PK | Used as a primary key |
| 4 | `ASSOC_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person_id of associating personnel |
| 5 | `DEVICE_CD` | DOUBLE | NOT NULL | FK→ | Used to identify which physical locations are associated to a service resource |
| 6 | `DISSOC_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person_id of dis-associating personnel |
| 7 | `DIS_ASSOCIATION_DT_TM` | DATETIME |  |  | The date and time the association is broken (dis-associated) |
| 8 | `HINT_ID` | DOUBLE | NOT NULL | FK→ | Primary key in BMDI_ASSOCIATION_HINTS table |
| 9 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Specifies the physical location of this person/alternate_record_id. |
| 10 | `MONITORED_DEVICE_ID` | DOUBLE | NOT NULL | FK→ | Will store the monitore_device_id from the bmdi_monitored_device table. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies which alternate_record_id is associated with a device and location |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Identifies the table which the alternate_record_id is associated with a device and location comes from. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies which person is associated with a device and location. |
| 14 | `RESOURCE_LOC_CD` | DOUBLE | NOT NULL |  | Specifies the physical location of this person/alternate_record_id. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPD_STATUS_CD` | DOUBLE | NOT NULL |  | Valid values include: RETROSPECTIVE, UNVERIFIED, VERIFIED, Default(0) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSOC_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DEVICE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `DISSOC_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `HINT_ID` | [BMDI_ASSOCIATION_HINTS](BMDI_ASSOCIATION_HINTS.md) | `HINT_ID` |
| `MONITORED_DEVICE_ID` | [BMDI_MONITORED_DEVICE](BMDI_MONITORED_DEVICE.md) | `MONITORED_DEVICE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BMDI_ADT_PERSON_R](BMDI_ADT_PERSON_R.md) | `ASSOCIATION_ID` |

