# PERSON_PRSNL_RELTN

> The person-personnel relationship table contains pointers to related personnel in the personnel table. The kind of relationship (i.e., primary care physician, etc.) defines how the person and personnel are related.

**Description:** Person Personnel Relationship  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_PRSNL_RELTN_ID`  
**Columns:** 31  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 8 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 9 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `FREE_TEXT_CD` | DOUBLE | NOT NULL |  | When set to a meaning of 'FTBRIEF', this indicates that the prsnl_person_id is NULL, meaning that there is no reference to the personnel table. This is a 'free text' relationship with the name of this |
| 12 | `FT_PRSNL_NAME` | VARCHAR(100) |  |  | The name of the personnel in the 'free text' relationship indicated by the free_text_ind in the row being set to 'TRUE'. |
| 13 | `INTERNAL_SEQ` | DOUBLE | NOT NULL |  | Internal Person Management sequence |
| 14 | `MANUAL_CREATE_BY_ID` | DOUBLE | NOT NULL |  | Person Id of the person who manually created the relationship |
| 15 | `MANUAL_CREATE_DT_TM` | DATETIME |  |  | Date and Time relationship was manually created. |
| 16 | `MANUAL_CREATE_IND` | DOUBLE | NOT NULL |  | Indicator that this relationship was manually created |
| 17 | `MANUAL_INACT_BY_ID` | DOUBLE | NOT NULL |  | Person Id of the person who manually inactivated the relationship |
| 18 | `MANUAL_INACT_DT_TM` | DATETIME |  |  | Date & time that this relationship was manually inactivated |
| 19 | `MANUAL_INACT_IND` | DOUBLE | NOT NULL |  | Indicator that this relationship was manually inactivated |
| 20 | `NOTIFICATION_CD` | DOUBLE | NOT NULL |  | Personnel preferred method of notification for issues concerning related person. |
| 21 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 22 | `PERSON_PRSNL_RELTN_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the person-personnel relationship table. It is an internally assigned number and generally not revealed to the user. |
| 23 | `PERSON_PRSNL_R_CD` | DOUBLE | NOT NULL |  | Person Prsnl Relationship Id |
| 24 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Identifies a sequencing priority to be used when a duplicate relationship of the same type is created |
| 25 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the personnel table. This is a 'role' name for the reference to person_id in the personnel table and used to differentiate between other references to person_id in this table. |
| 26 | `SOURCE_IDENTIFIER` | VARCHAR(255) |  |  | Identifier assigned from a master system to this row. Added to support he UK's PDS Allocated Object Identifier. Used to help keep the UK master database in sync with Millennium. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_PRSNL_RELTN_HISTORY](PERSON_PRSNL_RELTN_HISTORY.md) | `PERSON_PRSNL_RELTN_ID` |

