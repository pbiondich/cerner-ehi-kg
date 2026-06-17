# PFT_SYSTEM_ACTIVITY_LOG

> Stores general logging information for patient accounting processes.

**Description:** Patient Accounting System Activity Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLETION_MSG` | VARCHAR(250) | NOT NULL |  | The message returned from the reply block of the task. |
| 2 | `CURRENT_NODE_NAME` | VARCHAR(100) | NOT NULL |  | The name of the node of the executed task. |
| 3 | `CURRENT_PROCESS_NAME` | VARCHAR(100) | NOT NULL |  | Contains the name of the process which is executing the task. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Encounter record. |
| 5 | `END_DT_TM` | DATETIME |  |  | The end time of the executed task. |
| 6 | `ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the related entity name. |
| 7 | `ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies the related entity. |
| 8 | `EXECUTION_DURATION_SECS` | DOUBLE | NOT NULL |  | The time it took for the script to execute. |
| 9 | `FINAL_STATUS_CD` | DOUBLE | NOT NULL |  | The final status code that is givien back from the reply block of the task. |
| 10 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | Code value of the facility location. |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 12 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related organization. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Person record. |
| 14 | `PFT_EVENT_OCCUR_LOG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related pft_event_occur_log record. |
| 15 | `PFT_SYSTEM_ACTIVITY_LOG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PFT_SYSTEM_ACTIVITY_LOG table. |
| 16 | `SERVER_NAME` | VARCHAR(100) | NOT NULL |  | Name of the server of the executed task. |
| 17 | `START_DT_TM` | DATETIME |  |  | The start time of the executed task. |
| 18 | `TASK_NAME` | VARCHAR(30) | NOT NULL |  | The task that workflow task process performed. |
| 19 | `TIMER_IDENT` | VARCHAR(100) | NOT NULL |  | Used to persist the timer information. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PFT_EVENT_OCCUR_LOG_ID` | [PFT_EVENT_OCCUR_LOG](PFT_EVENT_OCCUR_LOG.md) | `PFT_EVENT_OCCUR_LOG_ID` |

