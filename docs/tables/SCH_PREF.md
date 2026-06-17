# SCH_PREF

> Scheduling Preferences

**Description:** Scheduling Preference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `DATA_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the scheduling date type. |
| 8 | `DATA_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling data type. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 11 | `PARENT_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 12 | `PARENT_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT_ID |
| 13 | `PREF_DT_TM` | DATETIME |  |  | A date and time value for the scheduling preference. |
| 14 | `PREF_ID` | DOUBLE | NOT NULL |  | The unique identifier for the scheduling preference. |
| 15 | `PREF_STRING` | VARCHAR(255) |  |  | A string value for a scheduling preference. |
| 16 | `PREF_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling preference type. |
| 17 | `PREF_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling preference type. |
| 18 | `PREF_UNITS` | DOUBLE | NOT NULL |  | Units |
| 19 | `PREF_UNITS_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the preference units of measure. |
| 20 | `PREF_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the preference units of measure. |
| 21 | `PREF_VALUE` | DOUBLE |  |  | A numeric value for a scheduling preference. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DATA_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PREF_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PREF_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

