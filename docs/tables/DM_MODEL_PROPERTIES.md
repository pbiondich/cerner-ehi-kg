# DM_MODEL_PROPERTIES

> This table contains a list of model properties group by property set. This table is populate by a readme file and cannot be modified on a client domain.

**Description:** Data Management Model Properties  
**Table type:** REFERENCE  
**Primary key:** `PROPERTY_NAME`, `PROPERTY_SET_NAME`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPENDER_NAME` | VARCHAR(32) |  |  | If valued, this appender will be called to lookup the value. This will only be used if property is not defined in the override table. |
| 2 | `APPENDER_PARAM` | VARCHAR(2048) |  |  | If an appender is defined, this column is used as an argument to the appender which is most likely the reference to the property value. |
| 3 | `PROPERTY_NAME` | VARCHAR(32) | NOT NULL | PK | Name of property in the property set. Dots are not allowed. |
| 4 | `PROPERTY_SET_NAME` | VARCHAR(64) | NOT NULL | PK FK→ | Dotted notation name used to group like configuration. |
| 5 | `PROPERTY_TXT` | VARCHAR(2048) |  |  | Model value. If Null, there is no model default and must be valued in override table. Must be printable characters. |
| 6 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROPERTY_SET_NAME` | [DM_PROPERTY_SET](DM_PROPERTY_SET.md) | `PROPERTY_SET_NAME` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DM_OVERRIDE_PROPERTIES](DM_OVERRIDE_PROPERTIES.md) | `PROPERTY_NAME` |
| [DM_OVERRIDE_PROPERTIES](DM_OVERRIDE_PROPERTIES.md) | `PROPERTY_SET_NAME` |

