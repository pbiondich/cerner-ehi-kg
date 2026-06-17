# EPISODE_PRSNL_RELTN_HIST

> Used to store the transactional history for episode/personnel relationships.

**Description:** Episode Personnel Relationship History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `EPISODE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the episode table. it is an internal system assigned number. This represents the value stored on the corresponding episode_prsnl_reltn_id at the time this history row was created. |
| 5 | `EPISODE_PRSNL_RELTN_HIST_ID` | DOUBLE | NOT NULL |  | The primary key of the episode_prsnl_reltn_history table. It is an internally generated number. |
| 6 | `EPISODE_PRSNL_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the episode_prsnl_reltn table. Identifies the row in the Episode_Prsnl_Reltn table that the history row is related to. |
| 7 | `EPISODE_PRSNL_R_CD` | DOUBLE | NOT NULL |  | Relationship of the prsnl to the episode. This represents the value stored on the corresponding episode_prsnl_reltn_id at the time this history row was createdCode Set: 333 |
| 8 | `PRSNL_PERSON_ID` | DOUBLE | NOT NULL | FK→ | this is the value of the unique primary identifier of the personnel table. this is a 'role' name for the reference to person_id in the personnel table and used to differentiate between other references to person_id in this table. This represents the value stored on the corresponding episode_prsnl_reltn_id at the time this history row was created |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | `EPISODE_ID` |
| `EPISODE_PRSNL_RELTN_ID` | [EPISODE_PRSNL_RELTN](EPISODE_PRSNL_RELTN.md) | `EPISODE_PRSNL_RELTN_ID` |
| `PRSNL_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

