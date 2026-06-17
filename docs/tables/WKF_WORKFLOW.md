# WKF_WORKFLOW

> Workflow Session contains details surrounding a user's session working through a particular workflow

**Description:** Workflow Session  
**Table type:** ACTIVITY  
**Primary key:** `WKF_WORKFLOW_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the Encntr table identifying the encounter this work flow session is being executed for. |
| 2 | `END_DT_TM` | DATETIME |  |  | The Date and time the workflow session was closed |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the Person Table identifying the Person this work flow session is being executed for. |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the Perersonnel that owns the work flow session |
| 5 | `SERVICE_DT_TM` | DATETIME |  |  | Date and time that the person was seen by the personnel |
| 6 | `SERVICE_TZ` | DOUBLE |  |  | Time Zone display associated with the Service Date and Time. |
| 7 | `START_DT_TM` | DATETIME |  |  | The Date and time the workflow session was started |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `WKF_WORKFLOW_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the WKF_WORKFLOW table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [WKF_COMPONENT](WKF_COMPONENT.md) | `WKF_WORKFLOW_ID` |
| [WKF_OUTPUT](WKF_OUTPUT.md) | `WKF_WORKFLOW_ID` |

