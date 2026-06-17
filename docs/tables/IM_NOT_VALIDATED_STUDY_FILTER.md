# IM_NOT_VALIDATED_STUDY_FILTER

> This table contains a list of filters. Currently it contains institution names, station names, and modality types. Users will be able to select zero or more of these filters to save as preferences. The user's preferences will be used to build the not-validated studies list displayed in the Radiology Desktop worklist.

**Description:** Image Not-Validated Study Filter  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IM_FILTER_DATA` | VARCHAR(64) | NOT NULL |  | This column contains the station name, modality, or institution as it was received from the archive. |
| 2 | `IM_FILTER_ID` | DOUBLE | NOT NULL |  | This column contains a unique meaningless number that only serves the purpose of uniquely identifying a row. |
| 3 | `IM_FILTER_TYPE_CD` | DOUBLE | NOT NULL |  | This column contains the code value to indicate if the row contains a station name, modality, or institution. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

