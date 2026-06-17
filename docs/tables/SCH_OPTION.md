# SCH_OPTION

> Scheduling Warning Option

**Description:** Contains the Scheduling Warning Option chosen for a Scheduling Warning Type  
**Table type:** ACTIVITY  
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
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 9 | `PARENT_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 10 | `PARENT_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT_ID |
| 11 | `SCH_OPTION_ID` | DOUBLE | NOT NULL |  | The unique identifier for the warning option chosen for a generated warning. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 18 | `WARN_CLASS_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the scheduling warning class. |
| 19 | `WARN_CLASS_MEANING` | VARCHAR(12) |  |  | A 12-char description of the scheduling warning class. |
| 20 | `WARN_DT_TM` | DATETIME | NOT NULL |  | The date and time was warning was generated. |
| 21 | `WARN_LEVEL_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling warning severity level. |
| 22 | `WARN_LEVEL_MEANING` | VARCHAR(12) |  |  | The 12-character description corresponding to the scheduling warning severity level. |
| 23 | `WARN_OPTION_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the warning option that was chosen by the user. |
| 24 | `WARN_OPTION_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the scheduling warning option chosen. |
| 25 | `WARN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PERSON_ID of the person from the personnel table (PRSNL) that created the warning. |
| 26 | `WARN_REASON_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling warning override reason. |
| 27 | `WARN_REASON_MEANING` | VARCHAR(12) |  |  | The 12-character description corresponing to the scheduling override warning reason. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WARN_CLASS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_LEVEL_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_OPTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `WARN_REASON_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

