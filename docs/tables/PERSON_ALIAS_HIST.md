# PERSON_ALIAS_HIST

> Used for tracking history of changes to person aliases.

**Description:** Person Alias History Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS` | VARCHAR(200) | NOT NULL |  | The alias is an identifier (I.e., SSN, medical record number, etc.) for a person. The alias may be unique or non-unique depending on the type of alias. |
| 6 | `ALIAS_EXPIRY_DT_TM` | DATETIME |  |  | The date and time for which the alias is expired. |
| 7 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias pool code identifies a unique set or list of person identifiers (i.e., numbers). the alias pool code also determines the accept/display format for the unique set of identifiers. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 12 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 13 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `HEALTH_CARD_EXPIRY_DT_TM` | DATETIME |  |  | The date and time for which this health card becomes ineffective or expired. |
| 16 | `HEALTH_CARD_ISSUE_DT_TM` | DATETIME |  |  | The date and time for which this health card becomes effective or issued. |
| 17 | `HEALTH_CARD_PROVINCE` | VARCHAR(3) |  |  | Province in which the health card was issued with this alias was issued for a person. |
| 18 | `HEALTH_CARD_TYPE` | VARCHAR(32) |  |  | Type of health card which has a certain category or style. |
| 19 | `HEALTH_CARD_VER_CODE` | VARCHAR(3) |  |  | The latest recorded version of the health card with the associated alias value. |
| 20 | `PERSON_ALIAS_HIST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person_alias_hist table. It is an internal system assigned number. |
| 21 | `PERSON_ALIAS_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person alias table. It is an internal system assigned number. |
| 22 | `PERSON_ALIAS_RECORD_STATUS_CD` | DOUBLE | NOT NULL |  | Defines the current state of this person alias record. |
| 23 | `PERSON_ALIAS_STATUS_CD` | DOUBLE | NOT NULL |  | Defines the current verification status of this person alias. |
| 24 | `PERSON_ALIAS_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Person slias sub type code identifies a category within a particular person alias type code. For example, NAME is an alias type and MAIDEN is an alias sub type. |
| 25 | `PERSON_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | person alias type code identifies a kind or type of alias (i.e., ssn, mrn, financial number, community mrn, etc.). they have Cerner pre-defined meanings in the common data foundation table allowing hna applications to look for a specific kind of alias. |
| 26 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 27 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 28 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 29 | `TRANSACTION_DT_TM` | DATETIME |  |  | More aptly named activity_dt_tm; holds the current date and time of the system when the row was inserted. This will match the create_dt_tm from the corresponding pm_hist_tracking row. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

