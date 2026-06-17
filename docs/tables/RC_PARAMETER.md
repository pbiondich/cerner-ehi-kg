# RC_PARAMETER

> The RC_PARAMETER table stores information about parameters.

**Description:** Revenue Cycle Parameter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Contains the date and time the row was created. |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Contains the id of the person who created the row |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `PARM_NAME` | VARCHAR(100) | NOT NULL |  | Contains the name of the parameter. |
| 10 | `PARM_NAME_CD` | DOUBLE | NOT NULL |  | Codified Parameter Name |
| 11 | `PARM_VALUE` | DOUBLE |  |  | The Real number value of the parameter. |
| 12 | `PARM_VALUE_DT_TM` | DATETIME |  |  | The date and time value of the parameter. |
| 13 | `PARM_VALUE_NBR` | DOUBLE |  |  | The Integer value of the parameter. |
| 14 | `PARM_VALUE_TXT` | VARCHAR(255) |  |  | The text value of the parameter. |
| 15 | `PARM_VALUE_TYPE_FLAG` | DOUBLE | NOT NULL |  | This column is a flag column to indicate the data type of the parameter value - PARM_VALUE_TYPE_FLAG. This will allow us to easily identify which value column to use, especially when values of 0 are used. |
| 16 | `RC_PARAMETER_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_PARAMETER table. |
| 17 | `RC_PARAMETER_SET_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the RC_PARAMETER_SET table. It is an internal system assigned number. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_PARAMETER_SET_ID` | [RC_PARAMETER_SET](RC_PARAMETER_SET.md) | `RC_PARAMETER_SET_ID` |

