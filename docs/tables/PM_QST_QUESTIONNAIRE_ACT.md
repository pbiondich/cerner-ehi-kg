# PM_QST_QUESTIONNAIRE_ACT

> Person Mgmt: Stores data related to activity occurring to a questionnaire

**Description:** Person Management Questionnaire Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMPLETED_DT_TM` | DATETIME |  |  | The date and time the questionnaire was completed. |
| 6 | `COMPLETED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the person who completed the questionnaire. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the questionnaire activity is related (i.e., person_id, encounter_id, etc.) |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this questionnaire activity row is related (i.e. PERSON, ENCOUNTER, etc.) |
| 9 | `PM_QST_QUESTIONNAIRE_ACT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies activity occurring to a questionnaire. |
| 10 | `QUESTIONNAIRE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a related questionnaire. |
| 11 | `REVIEWED_DT_TM` | DATETIME |  |  | The date and time at which an already completed questionnaire was reviewed.. |
| 12 | `REVIEWED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the person who reviewed the completed questionnaire. |
| 13 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the questionnaire. Examples are In Progress, Completed, etc. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMPLETED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `QUESTIONNAIRE_ID` | [PM_QST_QUESTIONNAIRE](PM_QST_QUESTIONNAIRE.md) | `QUESTIONNAIRE_ID` |
| `REVIEWED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

