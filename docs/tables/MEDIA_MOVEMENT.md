# MEDIA_MOVEMENT

> Store from and to locations when a media master row is updated with a location change

**Description:** Stores the movement history for media master rows  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | The date and time that the Media Movement row was created |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The personnel id of the user that created the row |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FRAME` | VARCHAR(15) |  |  | Stores an alphanumeric frame number for a microfilm frame. (varchar 15) |
| 10 | `FREETEXT_ROLL_FRAME` | VARCHAR(255) |  |  | For use with microfilm functionality that requires the roll and frame information to be stored in the same field. (varchar 255) |
| 11 | `FROM_LOCATION_CD` | DOUBLE | NOT NULL |  | The location that the media was moved from |
| 12 | `FROM_MEDIA_MASTER_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the media master table. It is an internal system assigned number. It is filled out if the media was moved from another media. |
| 13 | `MEDIA_COMMENT` | VARCHAR(255) |  |  | Comment field for use with microfilm information. (varchar 255) |
| 14 | `MEDIA_MASTER_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the media master table. It is an internal system assigned number |
| 15 | `MEDIA_MOVEMENT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the media movement table. It is an internal system assigned number. |
| 16 | `RECORDING_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that is credited for performing the move. |
| 17 | `ROLL` | VARCHAR(15) |  |  | Stores an alphanumeric roll number for a microfilm roll. (varchar 15) |
| 18 | `SYSTEM_ASSUMED_MOVEMENT` | DOUBLE |  |  | This field indicates whether or not the system assumed the movement based on a predefined trigger |
| 19 | `TO_LOCATION_CD` | DOUBLE | NOT NULL |  | This is the location that the media was moved to. |
| 20 | `TO_MEDIA_MASTER_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the media master table. It is an internal system assigned number. It is filled out if the media was moved to another media. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MEDIA_MASTER_ID` | [MEDIA_MASTER](MEDIA_MASTER.md) | `MEDIA_MASTER_ID` |

