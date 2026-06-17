# HIS_OBSERVATION

> Stores Patients observation information

**Description:** HEALTHE INTENT SOLUTONS OBSERVATION LOG  
**Table type:** ACTIVITY  
**Primary key:** `HIS_OBSERVATION_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EVENT_DT_TM` | DATETIME |  |  | The date and time the observation occurred. |
| 3 | `HIS_OBSERVATION_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `OBSERVATION_CREATED_DT_TM` | DATETIME |  |  | The date and time the observation outcome was identified. |
| 5 | `OBSERVATION_DESCRIPTION_CLOB` | LONGTEXT |  |  | The description of the observation. |
| 6 | `OBSERVATION_IDENT` | VARCHAR(100) | NOT NULL |  | The unique identifier of the observation. |
| 7 | `OBSERVATION_NAME` | VARCHAR(255) | NOT NULL |  | The name of the observation. |
| 8 | `OBSERVATION_NAME_KEY` | VARCHAR(255) | NOT NULL |  | The key for the name of the observation. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HIS_OBS_ACTIVITY](HIS_OBS_ACTIVITY.md) | `HIS_OBSERVATION_ID` |
| [HIS_OBS_ACTIVITY_H](HIS_OBS_ACTIVITY_H.md) | `HIS_OBSERVATION_ID` |

