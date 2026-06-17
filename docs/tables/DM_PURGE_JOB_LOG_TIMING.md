# DM_PURGE_JOB_LOG_TIMING

> A table to store the timings of individual runs of purge templates

**Description:** DM_PURGE_JOB_LOG_TIMINGS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `JOB_LOG_TIMING_ID` | DOUBLE | NOT NULL |  | A non-intelligent key for each row; populated from DM_CLINICAL_SEQ sequence |
| 2 | `LOG_ID` | DOUBLE | NOT NULL | FK→ | Foreign key referencing DM_PURGE_JOB_LOG |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `VALUE_KEY` | VARCHAR(40) | NOT NULL |  | The text key which, in conjunction with the LOG_ID, can be used to determine a value stored for a particular purge template run |
| 9 | `VALUE_NBR` | DOUBLE | NOT NULL |  | A value corresponding to the value key. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOG_ID` | [DM_PURGE_JOB_LOG](DM_PURGE_JOB_LOG.md) | `LOG_ID` |

