# DM_XNTR_JOB

> Stores information about what persons are being retrieved

**Description:** Database Architecture Extract and Tranform Retrieve Job  
**Table type:** ACTIVITY  
**Primary key:** `DM_XNTR_JOB_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_SID` | VARCHAR(255) |  |  | Audit SID |
| 2 | `DM_XNTR_JOB_ID` | DOUBLE | NOT NULL | PK | Non-intelligent PK of table |
| 3 | `FILE_NAME` | VARCHAR(30) |  |  | Holds the name of the file containing the list of persons |
| 4 | `JOB_END_DT_TM` | DATETIME |  |  | Holds the time the job was ended |
| 5 | `JOB_START_DT_TM` | DATETIME |  |  | Holds the time the job was started |
| 6 | `LOG_FILE` | VARCHAR(80) |  |  | Log File |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Holds person to retrieve data on |
| 8 | `STATUS` | VARCHAR(20) | NOT NULL |  | Holds status of person being retrieved |
| 9 | `STATUS_MSG` | VARCHAR(250) |  |  | Holds information about status |
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

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_XNTR_EXTRACT](DM_XNTR_EXTRACT.md) | `DM_XNTR_JOB_ID` |

