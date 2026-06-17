# PM_USER_DEFINED

> PM User Defined

**Description:** This table will hold the information from the user defined prompts  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the user defined row is related (i.e., person_id, encntr_id) |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this User Defined row is related (i.e.,PERSON, ENCOUNTER) |
| 9 | `PM_USER_DEFINED_ID` | DOUBLE | NOT NULL |  | The pm user defined ID is the primary key of the pm_user_defined table. |
| 10 | `UDF_TYPE_CD` | DOUBLE | NOT NULL |  | The user defined type code is the code set value which identifies the user defined information for the pm_user_defined row. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VALUE_CD` | DOUBLE | NOT NULL |  | This field holds Coded value information for user defined prompts This field can hold any Code Set and should be in the group of numbers set aside for User_defined data |
| 17 | `VALUE_DT_TM` | DATETIME |  |  | This field holds Date value information for user defined prompts |
| 18 | `VALUE_IND` | DOUBLE | NOT NULL |  | This field holds Indicator value information for user defined prompts |
| 19 | `VALUE_LONG_TEXT_REF_ID` | DOUBLE | NOT NULL |  | Foreign key from LONG_TEXT table. This field holds the Text value information for user defined prompts. |
| 20 | `VALUE_NBR` | DOUBLE | NOT NULL |  | This field holds Number value information for user defined prompts |
| 21 | `VALUE_TYPE` | DOUBLE | NOT NULL |  | This field holds the indicator as to what type of User Defined Information is in the row. (1 -Text , 2 - coded, 3 - data/time, 4 - Indicator, 5 - numeric) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

