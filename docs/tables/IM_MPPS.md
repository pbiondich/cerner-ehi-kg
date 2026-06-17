# IM_MPPS

> IM Modality Perform Procedure Step

**Description:** This table contains the Modality Perform Procedure Step related data.  
**Table type:** ACTIVITY  
**Primary key:** `IM_MPPS_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEVICE_ID` | DOUBLE | NOT NULL |  | Modality Device Id |
| 2 | `DISTANCE_SOURCE_TO_DETECTOR` | DOUBLE | NOT NULL |  | Distance in MM from the source to detector center |
| 3 | `IM_MPPS_ID` | DOUBLE | NOT NULL | PK | This column contains a meaningless number that only serves to uniquely identify a row. |
| 4 | `LOCATION` | VARCHAR(16) |  |  | This column contains the location as it was received from the archive. |
| 5 | `MPPS_END_DT_TM` | DATETIME |  |  | This column contains the date and time that the MPPS transaction ended. |
| 6 | `MPPS_START_DT_TM` | DATETIME |  |  | This column contains the date and time that the MPPS transaction started. |
| 7 | `MPPS_STATUS_CD` | DOUBLE |  |  | This column indicates the status of the MPPS transaction |
| 8 | `MPPS_UID` | VARCHAR(64) |  |  | This column contains the MPPS UID as received from the modality. |
| 9 | `NBR_OF_SERIES` | DOUBLE |  |  | This column indicates the number of series associated with this MPPS. |
| 10 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This column contains the primary key of the parent table. This column along with Parent_entity_name identifies the parent table and row. |
| 11 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | This column contains the name of the parent table. It along with Parent_entity_id identifies the parent table and row. |
| 12 | `SCHEDULED_PROTOCOL_CD` | DOUBLE | NOT NULL |  | The code value that represents the DTA of the step being performed |
| 13 | `SCHEDULED_STEP_ID` | DOUBLE | NOT NULL |  | Unique ID assigned to the scheduled step |
| 14 | `STATION_AE_TITLE` | VARCHAR(16) |  |  | This column indicates the AE Title of the station that the MPPS originated. |
| 15 | `STATION_NAME` | VARCHAR(16) |  |  | This column identifies the station name from which the MPPS originated. |
| 16 | `TOTAL_NUMBER_OF_EXPOSURES` | DOUBLE | NOT NULL |  | Total number of exposures column |
| 17 | `TOTAL_TIME_OF_FLUOROSCOPY` | DOUBLE | NOT NULL |  | Total duration of X-Ray exposure during fluoroscopy in seconds (pedal time) |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [IM_SERIES](IM_SERIES.md) | `IM_MPPS_ID` |

