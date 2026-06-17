# DM_OVERRIDE_PROPERTIES

> This table contains the property values managed in the client's domain. The values in this table describe properties of the running system, not of the data contained in the database. When refreshing a database these table should be truncated of source rows and repopulated with the destiation rows.

**Description:** Data Management Override Properties  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 2 | `PROPERTY_NAME` | VARCHAR(32) | NOT NULL | FK→ | Name of property in the property set. Dots are not allowed. |
| 3 | `PROPERTY_SET_NAME` | VARCHAR(64) | NOT NULL | FK→ | Dotted notation name used to group like configuration. |
| 4 | `PROPERTY_TXT` | VARCHAR(2048) |  |  | Model value. If Null there is no model default and must be valued in override table. Must be printable. |
| 5 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROPERTY_NAME` | [DM_MODEL_PROPERTIES](DM_MODEL_PROPERTIES.md) | `PROPERTY_NAME` |
| `PROPERTY_SET_NAME` | [DM_MODEL_PROPERTIES](DM_MODEL_PROPERTIES.md) | `PROPERTY_SET_NAME` |

