# HIS_OBS_ACTIVITY

> Stores patient's observation activity information

**Description:** Healthe Intent Solutions Observation Activity Log  
**Table type:** ACTIVITY  
**Primary key:** `HIS_OBS_ACTIVITY_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `HIS_OBSERVATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the observation information of the patient. |
| 3 | `HIS_OBS_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the HIS_OBS_ACTIVITY table. |
| 4 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id that caused the last insert or update of the row in the table. |
| 6 | `STATUS_CD` | DOUBLE | NOT NULL |  | Contains the code that defines the observation status for the row. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HIS_OBSERVATION_ID` | [HIS_OBSERVATION](HIS_OBSERVATION.md) | `HIS_OBSERVATION_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HIS_OBS_ACTIVITY_H](HIS_OBS_ACTIVITY_H.md) | `HIS_OBS_ACTIVITY_ID` |

