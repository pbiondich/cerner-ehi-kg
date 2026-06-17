# FT_TERM_CANDIDATE_LIST

> This activity table contains records of all patients, for whom an active follow-up tracking record is present, who are considered (based on pathology activity) candidates to have their current follow-up tracking activity terminated.

**Description:** Followup Tracking Termination Candidate List  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FOLLOWUP_EVENT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to follow-up tracking information stored on the AP_FT_EVENT activity table. |
| 2 | `REVIEW_CASE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to identify the pathology case which caused the system to flag the follow-up tracking event as a possible termination candidate. This could be used to join to case information stored on PATHOLOGY_CASE. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FOLLOWUP_EVENT_ID` | [AP_FT_EVENT](AP_FT_EVENT.md) | `FOLLOWUP_EVENT_ID` |
| `REVIEW_CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |

