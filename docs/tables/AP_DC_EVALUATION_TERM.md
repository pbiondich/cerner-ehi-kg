# AP_DC_EVALUATION_TERM

> This reference table includes the terminology used to designate agreement or disagreement for a diagnostic correlation event.

**Description:** Diagnostic Correlation Evaluation Terminology  
**Table type:** REFERENCE  
**Primary key:** `EVALUATION_TERM_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AGREEMENT_CD` | DOUBLE | NOT NULL |  | This field includes the internal identification code of the overall classification of the evaluation term. Typically, only two classifications are found - "Agreement" and "Disagreement". These classifications are stored on code_set 15469. |
| 3 | `DESCRIPTION` | VARCHAR(60) |  |  | This field includes the long description, up-to-60 characters, defined for the diagnostic correlation evaluation term. |
| 4 | `DISCREPANCY_REQ_IND` | DOUBLE |  |  | This field includes a value indicating whether or not the user must enter a discrepancy categorization term. If the value is set to "1", the user will be required to enter a discrepancy reason. If the value is set to "0", the user will not be required to enter a discrepancy reason. Discrepancy reasons are stored on reference table AP_DC_DISCREPANCY_TERM. |
| 5 | `DISPLAY` | VARCHAR(15) |  |  | This field includes the short description, up-to-15 characters, defined for the diagnostic correlation evaluation term. |
| 6 | `EVALUATION_TERM_ID` | DOUBLE | NOT NULL | PK | This field includes the internal identification code assigned to the diagnostic correlation evaluation terminology entry. This value would be referenced on other tables, such as the AP_DC_EVENT activity table. |
| 7 | `INVESTIGATION_REQ_IND` | DOUBLE |  |  | This field includes a value indicating whether or not the user must enter an investigation term. If the value is set to "1", the user will be required to enter an investigation term. If the value is set to "0", the user will not be required to enter an investigation term. Investigation terms are stored on code_set 15449. |
| 8 | `REASON_REQ_IND` | DOUBLE |  |  | This field includes a value indicating whether or not the user must enter a discrepancy reason term. If the value is set to "1", the user will be required to enter a discrepancy reason term. If the value is set to "0", the user will not be required to enter a discrepancy reason term. Discrepancy reasons are stored on code_set 15429. |
| 9 | `RESOLUTION_REQ_IND` | DOUBLE |  |  | This field includes a value indicating whether or not the user must enter a discrepancy resolution term. If the value is set to "1", the user will be required to enter a discrepancy resolution term. If the value is set to "0", the user will not be required to enter a discrepancy resolution term. Resolution terms are stored on code_set 15450. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AP_DC_EVENT](AP_DC_EVENT.md) | `FINAL_EVAL_TERM_ID` |
| [AP_DC_EVENT](AP_DC_EVENT.md) | `INIT_EVAL_TERM_ID` |

