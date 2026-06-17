# PERSON_INFO_HIST

> Tracks modifications to history elements for a given person_info table.

**Description:** PERSON INFO HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 7 | `CHARTABLE_IND` | DOUBLE | NOT NULL |  | Determines whether this Person Level comment can be charted |
| 8 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `INFO_SUB_TYPE_CD` | DOUBLE |  |  | Information Sub Type Cd |
| 11 | `INFO_TYPE_CD` | DOUBLE | NOT NULL |  | Information Type Code Value |
| 12 | `INTERNAL_SEQ` | DOUBLE |  |  | Internal Person Management sequence |
| 13 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | A foreign key to the long_text table. ties a long_text row (such as a comment) to this table. person_info_hist_id becomes the parent_entity_id on the long_text table, and "person_info_hist" becomes the parent_entity_name. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 15 | `PERSON_INFO_HIST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person_info_hist table. It is an internal system assigned number. |
| 16 | `PERSON_INFO_ID` | DOUBLE | NOT NULL | FK→ | FK from the Person_Info table. |
| 17 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 18 | `PRIORITY_SEQ` | DOUBLE |  |  | Identifies a sequencing priority to be used when a duplicate relationship of the same type are created. |
| 19 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 20 | `TRANSACTION_DT_TM` | DATETIME |  |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `VALUE_CD` | DOUBLE |  |  | Stores historical values of type double from the parent table |
| 27 | `VALUE_DT_TM` | DATETIME |  |  | If the comment is of a date type, it is stored in this attribute |
| 28 | `VALUE_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the long_text table. It is an internal system assigned number. |
| 29 | `VALUE_NUMERIC` | DOUBLE |  |  | If the comment is of a numeric type, it is stored in this attribute. |
| 30 | `VALUE_NUMERIC_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the input from the front end tool for column value_number is 0 or null. |
| 31 | `VALUE_TYPE` | DOUBLE | NOT NULL |  | ** obsolete ** This column is no longer being used. This field holds the indicator as to what type of user defined information is in the row.(1 -text , 2 - coded, 3 - data/time, 4 - indicator, 5 - numeric) ** obsolete ** |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERSON_INFO_ID` | [PERSON_INFO](PERSON_INFO.md) | `PERSON_INFO_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

