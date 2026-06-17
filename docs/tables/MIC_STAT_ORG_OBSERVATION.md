# MIC_STAT_ORG_OBSERVATION

> This summary table is comprised of records extracted from the MIC_ORGANISM_OBSERVATION table. This information is utilized by the Microbiology Statistical Reporting package.

**Description:** Microbiology Statistical Organism Observation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MEDIA_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the specific type of media identified for this procedure. |
| 2 | `OBSERVATION` | VARCHAR(100) |  |  | This field identifies the morphological description of the organism for each piece of media. |
| 3 | `QUANTITATION_CD` | DOUBLE | NOT NULL |  | This field identifies the internal identification code of the quantity associated with the media and organism. |
| 4 | `REPORT_IND` | DOUBLE | NOT NULL |  | This field idocuments whether or not the quantity for the associated organism should be linked to the report. Only one quantity may be linked per organism. |
| 5 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field contains a unique value that uniquely identifies more than occurrence of the same media code for a given organism. |
| 6 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code assigned to the organism task from the MIC_STAT_TASK table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_LOG_ID` | [MIC_STAT_TASK](MIC_STAT_TASK.md) | `TASK_LOG_ID` |

