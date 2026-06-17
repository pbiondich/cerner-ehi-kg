# PERSON_PRSNL_RELTN_HISTORY

> Used to store the transactional history for person personnel relationships.

**Description:** Person Personnel Relation History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 9 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 10 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `FREE_TEXT_CD` | DOUBLE | NOT NULL |  | When set to a meaning of 'FTBRIEF', this indicates that the prsnl_person_id is NULL, meaning that there is no reference to the personnel table. This is a 'free text' relationship with the name of this |
| 13 | `FT_PRSNL_NAME` | VARCHAR(100) |  |  | The name of the personnel in the 'free text' relationship indicated by the free_text_ind in the row being set to 'TRUE'. |
| 14 | `INTERNAL_SEQ` | DOUBLE |  |  | Used within Cerner applications, if necessary, to order encounter personnel relation rows. |
| 15 | `MANUAL_CREATE_BY_ID` | DOUBLE | NOT NULL |  | Person Id of the person who manually created the relationship |
| 16 | `MANUAL_CREATE_DT_TM` | DATETIME |  |  | Date and Time relationship was manually created. |
| 17 | `MANUAL_CREATE_IND` | DOUBLE |  |  | Indicator that this relationship was manually created |
| 18 | `MANUAL_INACT_BY_ID` | DOUBLE | NOT NULL |  | Person Id of the person who manually inactivated the relationship |
| 19 | `MANUAL_INACT_DT_TM` | DATETIME |  |  | Date & time that this relationship was manually inactivated |
| 20 | `MANUAL_INACT_IND` | DOUBLE |  |  | Indicator that this relationship was manually inactivated |
| 21 | `NOTIFICATION_CD` | DOUBLE | NOT NULL |  | Personnel preferred method of notification for issues concerning related person. |
| 22 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 23 | `PERSON_PRSNL_RELTN_HISTORY_ID` | DOUBLE | NOT NULL |  | The primary key of the PERSON_PRSNL_RELTN_HISTORY table. |
| 24 | `PERSON_PRSNL_RELTN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person-personnel relationship table. It is an internally assigned number and generally not revealed to the user. |
| 25 | `PERSON_PRSNL_R_CD` | DOUBLE | NOT NULL |  | Person Prsnl Relationship Id |
| 26 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 27 | `PRIORITY_SEQ` | DOUBLE |  |  | Identifies a sequencing priority to be used when a duplicate relationship of the same type is created |
| 28 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the personnel table. This is a 'role' name for the reference to person_id in the personnel table and used to differentiate between other references to person_id in this table. |
| 29 | `SOURCE_IDENTIFIER` | VARCHAR(255) |  |  | Identifier assigned from a master system to this row. Added to support he UK's PDS Allocated Object Identifier. Used to help keep the UK master database in sync with Millennium. |
| 30 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 31 | `TRANSACTION_DT_TM` | DATETIME |  |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_PRSNL_RELTN_ID` | [PERSON_PRSNL_RELTN](PERSON_PRSNL_RELTN.md) | `PERSON_PRSNL_RELTN_ID` |
| `PRSNL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

