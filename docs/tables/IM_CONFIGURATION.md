# IM_CONFIGURATION

> This table contains configuration settings specific to image management.

**Description:** IM Configuration  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONFIGURATION_COMMENT` | VARCHAR(60) |  |  | This column contains a comment that could be viewed by the user that further explains the purpose of the configuration. |
| 2 | `IM_CONFIGURATION_ID` | DOUBLE | NOT NULL |  | This column contains a unique meaningless number that only serves as a unique identifier for a row. |
| 3 | `PARAMETER_NAME` | VARCHAR(40) | NOT NULL |  | This column contains the name of the configuration parameter. |
| 4 | `RESTRICTED_IND` | DOUBLE |  |  | This column indicates if the configuration setting is to be seen by the user in the database tool. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VALUE_CHAR` | VARCHAR(512) |  |  | This column contains the character value of the configuration setting if the setting is of type character. |
| 11 | `VALUE_DATE` | DATETIME |  |  | This column contains the date value for the configuration setting if the setting is of type date. |
| 12 | `VALUE_DESCRIPTION` | VARCHAR(60) |  |  | This column contains the description of the configuration setting. |
| 13 | `VALUE_NUMBER` | DOUBLE |  |  | This column contains the number value if the configuration is of type number. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

