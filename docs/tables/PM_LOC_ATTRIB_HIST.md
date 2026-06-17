# PM_LOC_ATTRIB_HIST

> Person Mgmt: History of attributes related to locations

**Description:** PM LOC ATTRIB HIST  
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
| 5 | `ATTRIB_TYPE_CD` | DOUBLE | NOT NULL |  | Type of attribute that is related to a location (e.g. Motor Vehicle, Fire/Explosion) |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `DESCRIPTION` | VARCHAR(40) |  |  | Free-text description of the attribute |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `HIST_ACTION` | VARCHAR(3) | NOT NULL |  | Indicates what type of action occurred (add, update, delete, etc.) |
| 10 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Code value describing the location related to the attribute |
| 11 | `LOC_TEMPLATE_STRING` | VARCHAR(20) |  |  | Column is not used |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | When a location is closed, this column gets stamped with the location_cd of the parent location that was closed. (e.g. if a Room gets closed, the bed locations belonging in that room will have a parent_entity_id equal to the location_cd for the Room) |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(60) |  |  | CDF meaning from code set 17649 describing the type of attribute |
| 14 | `PM_LOC_ATTRIB_HIST_ID` | DOUBLE | NOT NULL |  | Primary key |
| 15 | `PM_LOC_ATTRIB_ID` | DOUBLE | NOT NULL |  | Foreign key attribute associating the history row with a certain row on the pm_loc_attrib table |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VALUE_CD` | DOUBLE | NOT NULL |  | Value used for tying code values to attributes |
| 22 | `VALUE_DT_TM` | DATETIME |  |  | Value used for tying date/time to attributes |
| 23 | `VALUE_ID` | DOUBLE | NOT NULL |  | Value used for tying id's to attributes |
| 24 | `VALUE_NUM` | DOUBLE |  |  | Value used for tying integers to attributes |
| 25 | `VALUE_STRING` | VARCHAR(40) |  |  | Value used for tying strings to attributes |
| 26 | `VALUE_TIME_NUM` | DOUBLE |  |  | Value used for tying times to attributes |
| 27 | `VALUE_TYPE` | VARCHAR(1) |  |  | Indicates which value type is filled out (date, string, etc.) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

