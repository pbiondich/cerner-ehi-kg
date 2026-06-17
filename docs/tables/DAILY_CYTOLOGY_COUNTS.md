# DAILY_CYTOLOGY_COUNTS

> This activity table contains daily slide count and rescreening information for a specific cytotechnologist. Information such as the # of screening hours, # of slides screened, # of slide rescreened, and # slides selected for rescreening are included.

**Description:** Daily Cytology Counts  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 44

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHR_CASES` | DOUBLE |  |  | This field includes the number of cases that were selected for rescreening due to the clinically high risk indicator, for the cytotechnologist, for a single day. |
| 2 | `CHR_SLIDES` | DOUBLE |  |  | This field includes the number of slides that were evaluated (but possibly not selected) for rescreening due to the clinically high risk indicator, for the cytotechnologist, for a single day. |
| 3 | `CHR_SLIDES_REQUEUED` | DOUBLE |  |  | This field includes the number of slides that were selected for rescreening due to the clinically high risk indicator, for the cytotechnologist, for a single day. |
| 4 | `COMMENTS` | VARCHAR(100) |  |  | This field includes a daily statistics comment entered by the cytotechnologist, if present. |
| 5 | `EXCEEDED_LIMIT_CASES` | DOUBLE |  |  | This field includes the number of cases that were screened or rescreened by the cytotechnologist after the cytotechnologist's daily limit had been exceeded. |
| 6 | `EXCEEDED_LIMIT_SLIDES` | DOUBLE |  |  | This field includes the number of slides that were screened or rescreened by the cytotechnologist after the cytotechnologist's daily limit had been exceeded. |
| 7 | `GYN_CASES_IS` | DOUBLE |  |  | This field includes the total number of gynecologic cytology cases initially screened for a single day. |
| 8 | `GYN_CASES_RS` | DOUBLE |  |  | This field includes the total number of gynecologic cytology cases rescreened for a single day. |
| 9 | `GYN_INSTRUMENT_SCREENING` | DOUBLE |  |  | This field is not used at this time. |
| 10 | `GYN_SLIDES_IS` | DOUBLE |  |  | This field includes the total number of gynecologic cytology slides initially screened for a single day. |
| 11 | `GYN_SLIDES_RS` | DOUBLE |  |  | This field includes the total number of gynecologic cytology slides rescreened for a single day. |
| 12 | `NGYN_CASES_IS` | DOUBLE |  |  | This field includes the total number of non-gynecologic cytology cases initially screened for a single day. |
| 13 | `NGYN_CASES_RS` | DOUBLE |  |  | This field includes the total number of non-gynecologic cytology cases rescreened for a single day. |
| 14 | `NGYN_SLIDES_IS` | DOUBLE |  |  | This field includes the total number of non-gynecologic cytology slides initially screened for a single day. |
| 15 | `NGYN_SLIDES_RS` | DOUBLE |  |  | This field includes the total number of non-gynecologic cytology slides rescreened for a single day. |
| 16 | `NORMAL_CASES` | DOUBLE |  |  | This field includes the number of cases that were selected for rescreening due to the previous normal flag, for the cytotechnologist, for a single day. |
| 17 | `NORMAL_SLIDES` | DOUBLE |  |  | This field includes the number of slides that were evaluated (but possibly not selected) for rescreening due to the previous normal flag, for the cytotechnologist, for a single day. |
| 18 | `NORMAL_SLIDES_REQUEUED` | DOUBLE |  |  | This field includes the number of slides that were selected for rescreening due to the previous normal flag, for the cytotechnologist, for a single day. |
| 19 | `OUTSIDE_GYN_IS` | DOUBLE |  |  | This field includes the total number of gynecologic cytology slides screened at outside institutions. |
| 20 | `OUTSIDE_GYN_RS` | DOUBLE |  |  | This field includes the total number of gynecologic cytology slides rescreened at outside institutions. |
| 21 | `OUTSIDE_HOURS` | DOUBLE |  |  | This field includes the total number of hours spent screening or rescreening slides for outside institutions. |
| 22 | `OUTSIDE_NGYN_IS` | DOUBLE |  |  | This field includes the total number of non-gynecologic cytology slides screened at outside institutions. |
| 23 | `OUTSIDE_NGYN_RS` | DOUBLE |  |  | This field includes the total number of non-gynecologic cytology slides rescreened at outside institutions. |
| 24 | `PREV_ABNORMAL_CASES` | DOUBLE |  |  | This field includes the number of cases that were selected for rescreening due to the previous abnormal flag, for the cytotechnologist, for a single day. |
| 25 | `PREV_ABNORMAL_SLIDES` | DOUBLE |  |  | This field includes the number of slides that were evaluated (but possibly not selected) for rescreening due to the previous abnormal flag, for the cytotechnologist, for a single day. |
| 26 | `PREV_ABN_SLIDES_REQUEUED` | DOUBLE |  |  | This field includes the number of slides that were selected for rescreening due to the previous abnormal flag, for the cytotechnologist, for a single day. |
| 27 | `PREV_ATYPICAL_CASES` | DOUBLE |  |  | This field includes the number of cases that were selected for rescreening due to the previous atypical flag, for the cytotechnologist, for a single day. |
| 28 | `PREV_ATYPICAL_SLIDES` | DOUBLE |  |  | This field includes the number of slides that were evaluated (but possibly not selected) for rescreening due to the previous atypical flag, for the cytotechnologist, for a single day. |
| 29 | `PREV_ATYP_SLIDES_REQUEUED` | DOUBLE |  |  | This field includes the number of slides that were selected for rescreening due to the previous atypical flag, for the cytotechnologist, for a single day. |
| 30 | `PROFICIENCY_SLIDES` | DOUBLE |  |  | This field includes the number of proficiency slides that were screened. |
| 31 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies the cytotechnologist for whom the DAILY_SLIDE_COUNTS record was written. This value could be used to join to other tables, such as the PRSNL, PERSON, and CYTO_SCREENING_LIMITS, for example. |
| 32 | `QA_SLIDES` | DOUBLE |  |  | This field includes the number of quality assurance slides that were screened. |
| 33 | `RECORD_DT_TM` | DATETIME | NOT NULL |  | This field includes the date for which the DAILY_CYTOLOGY_COUNTS record is associated. |
| 34 | `SCREEN_HOURS` | DOUBLE |  |  | This field documents the number of screening hours accepted by the cytotechnologist for the specific date. |
| 35 | `UNSAT_CASES` | DOUBLE |  |  | This field includes the number of cases that were selected for rescreening due to an unsatisfactory result, for the cytotechnologist, for a single day. |
| 36 | `UNSAT_SLIDES` | DOUBLE |  |  | This field includes the number of slides that were evaluated (but possibly not selected) for rescreening due to an unsatisfactory result, for the cytotechnologist, for a single day. |
| 37 | `UNSAT_SLIDES_REQUEUED` | DOUBLE |  |  | This field includes the number of slides that were selected for rescreening due to an unsatisfactory result, for the cytotechnologist, for a single day. |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 43 | `USER_PREFERENCE_CASES` | DOUBLE |  |  | This field includes the number of cases that were manually selected (by the cytotechnologist) for rescreening for the specific date. |
| 44 | `USER_PREFERENCE_SLIDES` | DOUBLE |  |  | This field includes the number of slides that were manually selected (by the cytotechnologist) for rescreening for the specific date. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

