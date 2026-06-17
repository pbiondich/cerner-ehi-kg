# PM_USER_DEFINED_HIST

> Tracks modifications to history elements for a given user defined field.

**Description:** PM USER DEFINED HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the user defined row is related (i.e., person_id, encntr_id) |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The upper case name of the table to which this User Defined row is related (i.e.,PERSON, ENCOUNTER) |
| 8 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 9 | `PM_USER_DEFINED_HIST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the pm_user_defined_hist table. It is an internal system assigned number. |
| 10 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 11 | `TRANSACTION_DT_TM` | DATETIME |  |  | Date and time the transaction, which triggered the history row, occurred. This field can be system assigned or manually manipulated by users. |
| 12 | `UDF_TYPE_CD` | DOUBLE | NOT NULL |  | The user defined type code is the code set value which identifies the user defined information for the pm_user_defined row. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VALUE_CD` | DOUBLE | NOT NULL |  | Stores historical values of type double from the parent table |
| 19 | `VALUE_DT_TM` | DATETIME |  |  | This field holds Date value information for user defined prompts |
| 20 | `VALUE_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the long_text table. It is an internal system assigned number. |
| 21 | `VALUE_NBR` | DOUBLE | NOT NULL |  | This field holds Number value information for user defined prompts |
| 22 | `VALUE_NBR_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the input from the front end tool for column VALUE_NBRis 0 or NULL. |
| 23 | `VALUE_TYPE` | DOUBLE | NOT NULL |  | This field holds the indicator as to what type of User Defined Information is in the row. (1 -Text , 2 - coded, 3 - data/time, 4 - Indicator, 5 - numeric) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |
| `VALUE_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

