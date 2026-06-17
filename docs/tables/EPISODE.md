# EPISODE

> The episode table identifies a grouping or collection of information depending on the type of episode. If it is a person episode, then the episode might point to a series of encounters for the person related to a chronic condition or diagnosis.

**Description:** Episode  
**Table type:** ACTIVITY  
**Primary key:** `EPISODE_ID`  
**Columns:** 29  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this episode was created. |
| 8 | `CREATE_PRSNL_ID` | DOUBLE |  |  | The ID of the person who created the episode. |
| 9 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 10 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 11 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 12 | `DISPLAY` | VARCHAR(100) |  |  | Episode name. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `EPISODE_BREACH_DT_TM` | DATETIME |  |  | Contains the breach date and time for the episode. The breach date is the date that the episode is supposed to be completed by. If it continues past the breach_dt_tm then the episode is considered breached. |
| 15 | `EPISODE_CLOSE_REASON_CD` | DOUBLE | NOT NULL |  | The reason for closing an episode. |
| 16 | `EPISODE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the episode table. It is an internal system assigned number. |
| 17 | `EPISODE_PAUSE_DAYS_CNT` | DOUBLE | NOT NULL |  | Count of the number of pause days used to calculate the episode_breach_dt_tm or can be used to determine how many days were not paused between the episode start date time and the episode stop date time. |
| 18 | `EPISODE_START_DT_TM` | DATETIME |  |  | The Start Date and Time of the Episode. |
| 19 | `EPISODE_STATUS_CD` | DOUBLE | NOT NULL |  | The Current Status of the Episode. |
| 20 | `EPISODE_STOP_DT_TM` | DATETIME |  |  | The Stop Date and Time of the Episode. |
| 21 | `EPISODE_TYPE_CD` | DOUBLE | NOT NULL |  | Episode type code identifies the kind of episode (I.e., person, research, epidemic, etc.). |
| 22 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 23 | `REFER_FACILITY_CD` | DOUBLE | NOT NULL |  | The Location of the Referring Facility. |
| 24 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field which identifies the current category of service the patient is receiving for this episode. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [EPISODE_ACTIVITY](EPISODE_ACTIVITY.md) | `EPISODE_ID` |
| [EPISODE_PRSNL_RELTN](EPISODE_PRSNL_RELTN.md) | `EPISODE_ID` |
| [EPISODE_PRSNL_RELTN_HIST](EPISODE_PRSNL_RELTN_HIST.md) | `EPISODE_ID` |
| [MEDIA_MASTER](MEDIA_MASTER.md) | `EPISODE_ID` |
| [PT_PROT_REG](PT_PROT_REG.md) | `EPISODE_ID` |

