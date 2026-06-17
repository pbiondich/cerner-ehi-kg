# HIS_OBS_ACTIVITY_H

> Stores patient's observation activity information history

**Description:** HealtheIntent Solutions Observation Activity History Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `HIS_OBSERVATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the observation information of the patient. |
| 3 | `HIS_OBS_ACTIVITY_H_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the HIS_OBS_ACTIVITY_H table. |
| 4 | `HIS_OBS_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the observation activity information of the patient. |
| 5 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated by the process. |
| 6 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id that caused the last insert or update of the row in the table using the process. |
| 7 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the code that defines the observation status for the row. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HIS_OBSERVATION_ID` | [HIS_OBSERVATION](HIS_OBSERVATION.md) | `HIS_OBSERVATION_ID` |
| `HIS_OBS_ACTIVITY_ID` | [HIS_OBS_ACTIVITY](HIS_OBS_ACTIVITY.md) | `HIS_OBS_ACTIVITY_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

