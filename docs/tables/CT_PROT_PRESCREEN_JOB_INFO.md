# CT_PROT_PRESCREEN_JOB_INFO

> Stores the prescreening job results for each protocol in the job.

**Description:** PowerTrials Screening Job Data for Protocols  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHUNK_INDEX_NBR` | DOUBLE | NOT NULL |  | Stores the index value of chunk which is being run for pre-screening |
| 2 | `CHUNK_NBR` | DOUBLE | NOT NULL |  | Stores the number of chunks in which the patient data will be divided in and used for pre-screening |
| 3 | `COMPLETED_FLAG` | DOUBLE | NOT NULL |  | This field contains the current status for the prescreening job. 0=Incomplete 1=Completed Successfully 2=Forced Completion |
| 4 | `CT_PRESCREEN_JOB_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a job in ct_prescreen_job table. |
| 5 | `CT_PROT_PRESCREEN_JOB_INFO_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 6 | `CURR_EVAL_PAT_CNT` | DOUBLE | NOT NULL |  | The number of patients that have been evalauted by the HE server |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | this field uniquely identifies a row in the person table for which the prescreening was done |
| 8 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_master table. |
| 9 | `PT_QUALIFIED_NBR` | DOUBLE | NOT NULL |  | This field contains the number of patient qualified for this protocol for the specific job. |
| 10 | `TOTAL_EVAL_PAT_CNT` | DOUBLE | NOT NULL |  | The total number of patients that are to be evaluated for quick prescreening |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CT_PRESCREEN_JOB_ID` | [CT_PRESCREEN_JOB](CT_PRESCREEN_JOB.md) | `CT_PRESCREEN_JOB_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |

