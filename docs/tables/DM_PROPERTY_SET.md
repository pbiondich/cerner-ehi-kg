# DM_PROPERTY_SET

> Used to describe and scope a list of like properties used to configure the system. This table is populated with model data only. A prefix using dotted notation should be used to group like property sets. For example WebServices.Configuration. prefix would group all like webservice configuration.

**Description:** Data Management Property Set  
**Table type:** REFERENCE  
**Primary key:** `PROPERTY_SET_NAME`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PROPERTY_SET_DESC` | VARCHAR(256) | NOT NULL |  | Describes the collection of properties. |
| 2 | `PROPERTY_SET_NAME` | VARCHAR(64) | NOT NULL | PK | Dotted notation name used to group like configuration. |
| 3 | `TTL_SECS` | DOUBLE | NOT NULL |  | In seconds, how often this property set should be checked for change. -1 means never check, 0 means not to cache the properties associated with the set, minimum value greater than 0 is 60 seconds. |
| 4 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_MODEL_PROPERTIES](DM_MODEL_PROPERTIES.md) | `PROPERTY_SET_NAME` |

