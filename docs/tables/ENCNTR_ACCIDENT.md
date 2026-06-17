# ENCNTR_ACCIDENT

> The encounter accident table contains accident information related to a specific encounter. If necessary, there can be more than one encounter accident row for each encounter.

**Description:** Encounter Accident  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCIDENT_CD` | DOUBLE | NOT NULL |  | Identifies the type of accident (I.e., auto, work related, etc.) |
| 2 | `ACCIDENT_DT_TM` | DATETIME |  |  | The date and time the accident occurred. |
| 3 | `ACCIDENT_LOCTN` | VARCHAR(100) |  |  | The text description of the location where the accident occurred. |
| 4 | `ACCIDENT_TEXT` | VARCHAR(255) |  |  | A text field used to add additional information about the accident or persons involved. |
| 5 | `ACC_COUNTRY_CD` | DOUBLE | NOT NULL |  | The country where the accident occurred. |
| 6 | `ACC_DEATH_CD` | DOUBLE | NOT NULL |  | Defines how death was related to this encounter |
| 7 | `ACC_EMPL_ORG_ID` | DOUBLE |  | FK→ | The organization id of the employer at the time of the accident |
| 8 | `ACC_JOB_RELATED_CD` | DOUBLE | NOT NULL |  | Describes how this accident was job related |
| 9 | `ACC_STATE_CD` | DOUBLE | NOT NULL |  | The country where the accident occurred. |
| 10 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 11 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 12 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 13 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 14 | `AMBULANCE_ARRIVE_CD` | DOUBLE |  |  | Information regarding the arrival of the ambulance |
| 15 | `AMBULANCE_GEO_CD` | DOUBLE |  |  | Describes the geographic region the ambulance was from |
| 16 | `AMBULANCE_SERV_NBR` | CHAR(20) |  |  | The service number related to the ambulance visit |
| 17 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 18 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 19 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 20 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 21 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 22 | `ENCNTR_ACCIDENT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter accident table. It is an internal system assigned number. |
| 23 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 24 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 25 | `PLACE_CD` | DOUBLE | NOT NULL |  | Place of the accident (ex. Client's or Patient's Home, Health Center, Hospice, Group Home¿ etc.) |
| 26 | `POLICE_BADGE_NBR` | CHAR(20) |  |  | Badge Number of the officer involved with this encounter |
| 27 | `POLICE_FORCE_CD` | DOUBLE |  |  | Police force (department) that was involved with this encounter |
| 28 | `POLICE_INVOLVE_CD` | DOUBLE |  |  | Level of involvement the police had with this encounter |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACC_EMPL_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

