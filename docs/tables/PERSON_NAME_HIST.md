# PERSON_NAME_HIST

> Used for tracking history of changes to person names.

**Description:** PERSON NAME HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 43

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 9 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 10 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `NAME_DEGREE` | VARCHAR(100) |  |  | This is the person's abbreviation that represents a degree or certification. |
| 13 | `NAME_FIRST` | VARCHAR(100) |  |  | This is the person's first given name. |
| 14 | `NAME_FIRST_KEY` | VARCHAR(100) |  |  | This is the person's first given name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 15 | `NAME_FIRST_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_FIRST_KEY_A_NLS column |
| 16 | `NAME_FIRST_KEY_NLS` | VARCHAR(202) |  |  | First Name Key field converted to NLS format for internationalization requirements |
| 17 | `NAME_FULL` | VARCHAR(100) |  |  | This is the complete person name including punctuation, formatting, prefix, and suffix. |
| 18 | `NAME_INITIALS` | VARCHAR(100) |  |  | The three character initial abbreviation of the person's name. |
| 19 | `NAME_LAST` | VARCHAR(100) |  |  | This is the person's family name. |
| 20 | `NAME_LAST_KEY` | VARCHAR(100) |  |  | This is the person's family name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 21 | `NAME_LAST_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_LAST_KEY_A_NLS column |
| 22 | `NAME_LAST_KEY_NLS` | VARCHAR(202) |  |  | Last Name Key field converted to NLS format for internationalization requirements |
| 23 | `NAME_MIDDLE` | VARCHAR(100) |  |  | This is the person's middle or secondary given name or names. |
| 24 | `NAME_MIDDLE_KEY` | VARCHAR(100) |  |  | This is the person's middle name with all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 25 | `NAME_MIDDLE_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_MIDDLE_KEY_A_NLS column |
| 26 | `NAME_MIDDLE_KEY_NLS` | VARCHAR(202) |  |  | Last Name Key field converted to NLS format for internationalization requirements |
| 27 | `NAME_PREFIX` | VARCHAR(100) |  |  | Name prefix includes any titles that will precede the regular person name. |
| 28 | `NAME_SUFFIX` | VARCHAR(100) |  |  | Name suffix includes any titles that will follow the regular person name. |
| 29 | `NAME_TITLE` | VARCHAR(100) |  |  | This is the person's abbreviation that represents formal method of addressing, such as Mr. or Mrs. |
| 30 | `NAME_TYPE_CD` | DOUBLE | NOT NULL |  | This code identifies the type of name for the person name row (i.e., current, previous, maiden, other). |
| 31 | `NAME_TYPE_SEQ` | DOUBLE | NOT NULL |  | This is the numeric sequence that determines the priority or precedence that one name row has over another when both rows contain the same person_id and name_type_cd. |
| 32 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 33 | `PERSON_NAME_HIST_ID` | DOUBLE | NOT NULL |  | Unique identifier for the Person_name_hist table. |
| 34 | `PERSON_NAME_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person name table. It is an internal system assigned number. |
| 35 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 36 | `SOURCE_IDENTIFIER` | VARCHAR(255) |  |  | Identifier assigned from a master system to this row. Added to support the uk's pds allocated object identifier. Used to help keep the uk master database in sync with millennium. |
| 37 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 38 | `TRANSACTION_DT_TM` | DATETIME |  |  | More aptly named activity_dt_tm; holds the current date and time of the system when the row was inserted. This will match the create_dt_tm from the corresponding pm_hist_tracking row. |
| 39 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERSON_NAME_ID` | [PERSON_NAME](PERSON_NAME.md) | `PERSON_NAME_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

