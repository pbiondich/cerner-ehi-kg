# AP_DC_EVENT

> This activity table includes an entry for every diagnostic correlation event that has been established, regardless of whether or not the evaluation has simply been initiated, is in process, is complete, or is canceled.

**Description:** Diagnostic Correlation Event  
**Table type:** ACTIVITY  
**Primary key:** `EVENT_ID`  
**Columns:** 28  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGN_TO_GROUP_IND` | DOUBLE |  |  | Indicates whether the correlation event is currently assigned to a group. |
| 2 | `CANCEL_DT_TM` | DATETIME |  |  | If the correlation event was cancelled before the evaluation was completed, this field contains the date and time the event was cancelled. |
| 3 | `CANCEL_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | If the correlation event was cancelled before the evaluation was completed, this field contains the internal identification code associated with the user who completed the cancel request. Information about the user can be obtained by joining to the PERSON and/or PRSNL tables. |
| 4 | `CASE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code representing the case to which the diagnostic correlation event is assigned. Information about the case can be obtained by joining to the PATHOLOGY_CASE activity table. |
| 5 | `COMPLETE_DT_TM` | DATETIME |  |  | If the correlation evaluation is complete, this field contains the date and time the event was completed. |
| 6 | `COMPLETE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | If the correlation evaluation is complete, this field contains the internal identification code associated with the user who completed the event. The event is considered "complete" when the final evaluation reason is entered and saved (and the final discrepancy reason, if required). This is the user who was signed on to the system when the interaction occurred. This is not necessarily the user who is actually associated with the evaluation process. |
| 7 | `CORRELATE_CASE_ID` | DOUBLE | NOT NULL | FK→ | If the diagnostic correlation study is specified as an "across case" correlation, this field contains the internal identification code representing the other pathology case to which the initiated case is to be compared. Information about this case can be obtained by joining to the PATHOLOGY_CASE activity table. Information about the study itself can be obtained by viewing or joining to the information stored on the AP_DC_STUDY reference table. |
| 8 | `DISAGREE_REASON_CD` | DOUBLE | NOT NULL |  | If a disagreement reason was entered for the diagnostic correlation study event, this field contains the internal identification code assigned to the disagreement reason. Disagreement reasons are stored on code_set 15429. |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL | PK | This field contains the internal identification code that uniquely identifies this diagnostic correlation study event. This field is referenced on other activity tables, such as the AP_DC_EVENT_PRSNL table. |
| 10 | `FINAL_DISCREP_TERM_ID` | DOUBLE | NOT NULL | FK→ | If a final discrepancy evaluation term was entered for the diagnostic correlation study event, this field contains the internal identification code assigned to the discrepancy evaluation term. Discrepancy evaluation terms are stored on the AP_DC_DISCREPANCY_TERM reference table. |
| 11 | `FINAL_EVAL_TERM_ID` | DOUBLE | NOT NULL | FK→ | If a final evaluation term was entered for the diagnostic correlation study event, this field contains the internal identification code assigned to the evaluation term. Evaluation terms are stored on the AP_DC_EVALUATION_TERM reference table. |
| 12 | `INITIATED_DT_TM` | DATETIME |  |  | This field contains the date and time the diagnostic correlation study event was initiated. |
| 13 | `INITIATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the user who initiated the diagnostic correlation study event. This is the user who was signed on and actually completed the initiation conversation. This may not be the actual user (users or user group) who is associated with the evaluation process. Information about the user can be obtained by joining to the PERSON and/or PRSNL tables. |
| 14 | `INIT_DISCREP_TERM_ID` | DOUBLE | NOT NULL | FK→ | If an initial discrepancy evaluation term was entered for the diagnostic correlation study event, this field contains the internal identification code assigned to the discrepancy evaluation term. Discrepancy evaluation terms are stored on the AP_DC_DISCREPANCY_TERM reference table. |
| 15 | `INIT_EVAL_TERM_ID` | DOUBLE | NOT NULL | FK→ | If an initial evaluation term was entered for the diagnostic correlation study event, this field contains the internal identification code assigned to the evaluation term. Evaluation terms are stored on the AP_DC_EVALUATION_TERM reference table. |
| 16 | `INVESTIGATION_CD` | DOUBLE | NOT NULL |  | If an investigation value was entered for the diagnostic correlation study event, this field contains the internal identification code assigned to the investigation term. Investigation terms are stored on code_set 15449. |
| 17 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | If a free-text comment was entered for the diagnostic correlation study event, this field contains the internal identification code representing the stored location of the comment text. This text is stored on the LONG_TEXT table. |
| 18 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | If the diagnostic correlation event was associated with a "group" rather than an individual (or multiple individuals), this field contains the internal identification code representing the group. Members of the group associated with the specific diagnostic correlation event can be identified by viewing or joining to information stored on the AP_DC_EVENT_PRSNL activity table. |
| 19 | `REPORT_ISSUED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification of the person to which issued the report. This field can be used to join to the PRSNL table. |
| 20 | `RESOLUTION_CD` | DOUBLE | NOT NULL |  | If a resolution value was entered for the diagnostic correlation study event, this field contains the internal identification code assigned to the resolution term. Resolution terms are stored on code_set 15450. |
| 21 | `SLIDE_COUNTS` | DOUBLE | NOT NULL |  | This field contains the number of slides that were reviewed for a correlation event. |
| 22 | `STUDY_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the correlation study to be initiated upon qualification. |
| 23 | `SYS_CORR_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code to the AP_SYS_CORR table. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CANCEL_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `COMPLETE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CORRELATE_CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `FINAL_DISCREP_TERM_ID` | [AP_DC_DISCREPANCY_TERM](AP_DC_DISCREPANCY_TERM.md) | `DISCREPANCY_TERM_ID` |
| `FINAL_EVAL_TERM_ID` | [AP_DC_EVALUATION_TERM](AP_DC_EVALUATION_TERM.md) | `EVALUATION_TERM_ID` |
| `INITIATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `INIT_DISCREP_TERM_ID` | [AP_DC_DISCREPANCY_TERM](AP_DC_DISCREPANCY_TERM.md) | `DISCREPANCY_TERM_ID` |
| `INIT_EVAL_TERM_ID` | [AP_DC_EVALUATION_TERM](AP_DC_EVALUATION_TERM.md) | `EVALUATION_TERM_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `REPORT_ISSUED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `STUDY_ID` | [AP_DC_STUDY](AP_DC_STUDY.md) | `STUDY_ID` |
| `SYS_CORR_ID` | [AP_SYS_CORR](AP_SYS_CORR.md) | `SYS_CORR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AP_DC_EVENT_PRSNL](AP_DC_EVENT_PRSNL.md) | `EVENT_ID` |

