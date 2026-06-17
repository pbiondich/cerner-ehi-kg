# CYTO_SCREENING_LIMITS

> This reference table contains user-specific parameters with regards to slide limits (# of slides per day) associated with the reporting of cytology cases. Once a user's daily limit is reached, no additional cytology reports can be verified by the user.

**Description:** Cytology Screening Limits  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMMENTS` | VARCHAR(200) |  |  | This field contains any comments entered when a cytotechnologist's screening limits were reviewed. |
| 3 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies the cytotechnologist for whom screening limits have been defined or reviewed. This value could be used to join to other tables, such as the PRSNL, PERSON, and CYTO_SCREENING_SECURITY, for example. |
| 4 | `REQUEUE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether requeue will happen when maximum slide count is reached. 0 - User can still verify the report without showing the requeue dialog; 1 - Requeue dialog will be shown when maximum slide limit is reached. User will not able verify the report.0 and 1:1: Requeue dialog will be shown when maximum slide limit is reached. User will not able verify the report.0: User can still verify the report without showing the requeue dialog. |
| 5 | `REVIEWED_DT_TM` | DATETIME |  |  | This field contains the date the time the review event occurred. |
| 6 | `REVIEWER_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code associated with the user who is documented as the reviewer for the cytotechnologist's screening limit parameters. This ID could be used to join to the PRSNL or PERSON tables. |
| 7 | `SCREENING_HOURS` | DOUBLE |  |  | This field contains the standard number of screening hours that have been established for the cytotechnologist. |
| 8 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field documents the record sequence available for the cytotechnologist. The initial limit definition would be represented as the first sequence, the first review would be represented as the second sequence, etc. |
| 9 | `SLIDE_LIMIT` | DOUBLE |  |  | This field contains the maximum number of slides that may be screened or rescreened during a single day for the cytotechologist. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

