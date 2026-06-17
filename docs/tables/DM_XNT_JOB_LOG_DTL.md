# DM_XNT_JOB_LOG_DTL

> Logging table for the Extract and Transform process, 1 row should exist in this table for each JOB_ID,DM_XNT_JOB_LOG_ID, PERSON_ID, EXTRACT_DATE_START

**Description:** Data Management Extract and Transform Job Log  
**Table type:** ACTIVITY  
**Primary key:** `DM_XNT_JOB_LOG_DTL_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_SID` | VARCHAR(255) |  |  | Auditing Session Id |
| 2 | `DM_XNT_JOB_LOG_DTL_ID` | DOUBLE | NOT NULL | PK | Primary key for the logging table |
| 3 | `DM_XNT_JOB_LOG_ID` | DOUBLE | NOT NULL | FK→ | Primary key from DM_XNT_JOB_LOG table. |
| 4 | `END_UPDT_DT_TM` | DATETIME |  |  | Used to store the maximum UPDT_DT_TM value for the rows affected by this extract |
| 5 | `ERROR_MSG` | VARCHAR(1000) |  |  | Contains error message info if errors are reported, otherwise NULL |
| 6 | `EXTRACT_END_DT_TM` | DATETIME |  |  | Used to store the date/time that the extract was started for this JOB_ID and PERSON_ID |
| 7 | `EXTRACT_START_DT_TM` | DATETIME | NOT NULL |  | Used to store the date/time that the extract was started for this JOB_ID and PERSON_ID |
| 8 | `EXTRACT_STATUS` | VARCHAR(30) | NOT NULL |  | Indicates the current status of this extract process |
| 9 | `FILE_LABEL` | VARCHAR(100) |  |  | Stores the label assigned to this extract |
| 10 | `FILE_UUID` | VARCHAR(200) |  |  | UUID returned from MMF when extract is saved |
| 11 | `JOB_ID` | DOUBLE | NOT NULL | FK→ | Primary key from DM_PURGE_JOB table used to describe the template and parameters used for this extract |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | PERSON_ID for the transform being processed |
| 13 | `START_UPDT_DT_TM` | DATETIME |  |  | Used to store the minimum UPDT_DT_TM value for the rows affected by this extract |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_XNT_JOB_LOG_ID` | [DM_XNT_JOB_LOG](DM_XNT_JOB_LOG.md) | `DM_XNT_JOB_LOG_ID` |
| `JOB_ID` | [DM_PURGE_JOB](DM_PURGE_JOB.md) | `JOB_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_XNT_JOB_LOG_CNT](DM_XNT_JOB_LOG_CNT.md) | `DM_XNT_JOB_LOG_DTL_ID` |

