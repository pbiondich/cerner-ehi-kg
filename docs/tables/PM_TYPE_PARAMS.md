# PM_TYPE_PARAMS

> Stores information for properties of different types of parameters and flags. Only one active, "unended" row should ever exists for a given combination of type_flag, organization_id, type_cd and param_name.

**Description:** PM Type Params  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 7 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 8 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 11 | `PARAM_NAME` | VARCHAR(40) | NOT NULL |  | String value used to determine parameter for each type flag, type code and organization id. |
| 12 | `PARENT_ROW_NBR` | DOUBLE | NOT NULL |  | The value of the primary identifier for the parent row on this table to which the row is related. |
| 13 | `PM_TYPE_PARAMS_SEQ` | DOUBLE | NOT NULL |  | PM Type Params Sequence |
| 14 | `TYPE_CD` | DOUBLE | NOT NULL |  | Represents the property name from codeset 28240 or 356 or 17649. This value can be a table column header, a user defined property or a location attribute property. In the future, might contain code values from additional codesets as new parameters are defined for different functional areas. |
| 15 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | An indicator which determines the type of transaction that occurred for each row. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VALUE_CD` | DOUBLE | NOT NULL |  | Represents the codified value for a parameter. Value could be from multiple codesets based on the type flag and parameter. |
| 22 | `VALUE_DT_TM` | DATETIME |  |  | Represents the date and time for a parameter. |
| 23 | `VALUE_NBR` | DOUBLE |  |  | Represents the constant which is the cdf meaning of the type_cd if the parameter is for secondary alerts. May also represent the number value for the parameter of a different type. |
| 24 | `VALUE_STRING` | VARCHAR(100) |  |  | Represents the type extension on the type_cd code value if the parameter is for a secondary alert. May also contain a string value for a parameter of a different type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

