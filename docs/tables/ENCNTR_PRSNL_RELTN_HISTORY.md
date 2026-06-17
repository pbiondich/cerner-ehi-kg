# ENCNTR_PRSNL_RELTN_HISTORY

> Used to store the transactional history for encounter/personnel relationships.

**Description:** Encounter Personnel Relation HIstory  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_DT_TM` | DATETIME |  |  | This column holds the current system date and time that the row was inserted. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 8 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 9 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 10 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 11 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 13 | `ENCNTR_PRSNL_RELTN_HISTORY_ID` | DOUBLE | NOT NULL |  | The primary key of the ENCNTR_PRSNL_RELTN_HISTORY table. |
| 14 | `ENCNTR_PRSNL_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the ENCNTR_PRSNL_RELTN table. |
| 15 | `ENCNTR_PRSNL_R_CD` | DOUBLE | NOT NULL |  | The relationship of the personnel to the encounter. |
| 16 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. Examples may include inpatient, outpatient, etc. |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `EXPIRATION_IND` | DOUBLE |  |  | Indicates whether the relationship between the encounter and the personnel has expired. |
| 19 | `EXPIRE_DT_TM` | DATETIME |  |  | Date/Time that the relationship has been expired from encounter. Primarily used to prevent the relationship from appearing in PowerChart application. |
| 20 | `FREE_TEXT_CD` | DOUBLE | NOT NULL |  | Value that shows the type of free text relationship information that is present between the encounter and personnel. When set to a meaning of 'FTBRIEF', this indicates that the prsnl_person_id is NULL, meaning that there is no reference to the personnel table. |
| 21 | `FT_PRSNL_NAME` | VARCHAR(100) |  |  | The name of the personnel in the 'free text' relationship indicated by the free_text_ind in the row being set to 'TRUE'. |
| 22 | `INTERNAL_SEQ` | DOUBLE |  |  | Used within Cerner applications, if necessary, to order encounter personnel relation rows. |
| 23 | `MANUAL_CREATE_BY_ID` | DOUBLE | NOT NULL |  | Person Id of the person who manually created the relationship. |
| 24 | `MANUAL_CREATE_DT_TM` | DATETIME |  |  | Date and time the encounter personnel relationship was manually created. |
| 25 | `MANUAL_CREATE_IND` | DOUBLE |  |  | Indicates whether the row was manually created. |
| 26 | `MANUAL_INACT_BY_ID` | DOUBLE | NOT NULL |  | The person_id of the person who inactivated the relationship. |
| 27 | `MANUAL_INACT_DT_TM` | DATETIME |  |  | Date and time the row was manually inactivated. |
| 28 | `MANUAL_INACT_IND` | DOUBLE |  |  | Indicates whether the row was manually inactivated. |
| 29 | `NOTIFICATION_CD` | DOUBLE | NOT NULL |  | Personnel preferred method of notification for issues concerning related person. |
| 30 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 31 | `PRIORITY_SEQ` | DOUBLE |  |  | The priority given to the relation type if more than one of the same type exists |
| 32 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the personnel table. This is a 'role' name for the reference to person_id in the personnel table and used to differentiate between other references to person_id in this table. |
| 33 | `TRANSACTION_DT_TM` | DATETIME |  |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_PRSNL_RELTN_ID` | [ENCNTR_PRSNL_RELTN](ENCNTR_PRSNL_RELTN.md) | `ENCNTR_PRSNL_RELTN_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |
| `PRSNL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

