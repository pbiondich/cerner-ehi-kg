# PM_PREF

> PM_PREF

**Description:** Enterprise Registration Preferences table.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 7 | `DATA_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the data_status_cd was set. |
| 8 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 9 | `DETAILS_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Long text string representing additional details about a preference. Mainly used to store XML strings. |
| 10 | `DISPLAY_FLAG` | DOUBLE | NOT NULL |  | Flags used to represent display infomation about a preference. Values are Application/Task specific. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `ICON_LONG_BLOB_ID` | DOUBLE | NOT NULL |  | Used to store a Icon to the data base on the long_blob_reference table. |
| 13 | `LABEL` | VARCHAR(100) |  |  | Preference Label. |
| 14 | `OPTIONS` | VARCHAR(200) |  |  | Additional Preference Options encoded into a string. |
| 15 | `OPTIONS_NBR` | DOUBLE | NOT NULL |  | Additional preference options encoded into a number. Usually used as a bitmap. |
| 16 | `PM_PREF_ID` | DOUBLE | NOT NULL |  | Primary key for the PM Preferences table. |
| 17 | `PM_PREF_SETUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to pm_pref_setup table. |
| 18 | `PREF_TYPE_FLAG` | DOUBLE | NOT NULL |  | Preference Type Flag, used to determine type of preference for a given application/task. |
| 19 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Sequence that determines the order of the preference types for a given application/task. |
| 20 | `PUBLISH_PREF_ID` | DOUBLE | NOT NULL |  | Original preference id from the pm_pref table. The original preference_id may be deleted from this table but it is still used here to group preferences. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PM_PREF_SETUP_ID` | [PM_PREF_SETUP](PM_PREF_SETUP.md) | `PM_PREF_SETUP_ID` |

