# MEDIA_MASTER

> Stores current location, permanent location, media type , etc for each media.

**Description:** Stores Media Master information  
**Table type:** ACTIVITY  
**Primary key:** `MEDIA_MASTER_ID`  
**Columns:** 34  
**Referenced by:** 7 columns

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
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date and time that the media was created |
| 8 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel id of the user that created the row, from the personnel table (prsnl). This is the value of the unique primary identifier of the personnel table. It is an internal system assigned number |
| 9 | `CURRENT_LOC_CD` | DOUBLE | NOT NULL |  | The coded value for the current location of the media |
| 10 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `EPISODE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the episode table. It is an internal system assigned number |
| 13 | `FRAME` | VARCHAR(15) |  |  | Stores an alphanumeric frame number for a microfilm frame. (varchar 15) |
| 14 | `FREETEXT_ROLL_FRAME` | VARCHAR(255) |  |  | For use with microfilm functionality that requires the roll and frame information to be stored in the same field. (varchar 255) |
| 15 | `MEDIA_COMMENT` | VARCHAR(255) |  |  | Comment field for use with microfilm information. (varchar 255) |
| 16 | `MEDIA_MASTER_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the media master table. It is an internal system assigned number |
| 17 | `MEDIA_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies if the media is available, loaned, lost, etc. |
| 18 | `MEDIA_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of media (e.g., unit record, patient chart, microfilm, chart container) |
| 19 | `MOVEMENT_DT_TM` | DATETIME |  |  | The date and time the media's location/parent media was last inserted/updated |
| 20 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 21 | `PARENT_MEDIA_MASTER_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the media master table for the parent of this record. |
| 22 | `PERMANENT_LOC_CD` | DOUBLE | NOT NULL |  | The permanent location where the media is stored. |
| 23 | `PERSON_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Links a row in this table to the person_alias table. |
| 24 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 25 | `PREV_INTERNAL_LOC_CD` | DOUBLE | NOT NULL |  | Previous internal location code is populated when a media is moved to an external location. |
| 26 | `RETURN_LOC_CD` | DOUBLE | NOT NULL |  | Only filled out if the media needs to return to a different location than the permanent_loc_cd. |
| 27 | `ROLL` | VARCHAR(15) |  |  | Stores an alphanumeric roll number for a microfilm roll. (varchar 15) |
| 28 | `STORAGE_CD` | DOUBLE | NOT NULL |  | Identifies the type of location/media that the media is currently stored (e.g., chart container, unit record, perm loc, cur loc). |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 34 | `VOLUME_NBR` | DOUBLE |  |  | Identifies the specific instance of which media this is in a series. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `EPISODE_ID` | [EPISODE](EPISODE.md) | `EPISODE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ALIAS_ID` | [PERSON_ALIAS](PERSON_ALIAS.md) | `PERSON_ALIAS_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [BATCH_LABEL](BATCH_LABEL.md) | `MEDIA_MASTER_ID` |
| [HIM_PV_CHART](HIM_PV_CHART.md) | `MEDIA_MASTER_ID` |
| [HIM_REQUEST_CRITERIA](HIM_REQUEST_CRITERIA.md) | `MEDIA_MASTER_ID` |
| [MEDIA_ENCNTR_RELTN](MEDIA_ENCNTR_RELTN.md) | `MEDIA_MASTER_ID` |
| [MEDIA_MASTER_ALIAS](MEDIA_MASTER_ALIAS.md) | `MEDIA_MASTER_ID` |
| [MEDIA_MASTER_HIST](MEDIA_MASTER_HIST.md) | `MEDIA_MASTER_ID` |
| [MEDIA_MOVEMENT](MEDIA_MOVEMENT.md) | `MEDIA_MASTER_ID` |

