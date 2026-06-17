# CYTO_ALPHA_SECURITY

> This reference table contains the verification limits, general classifications, and required rescreening requirements for every diagnosis alpha response code associated with a cytology report.

**Description:** Cytology Alpha Security  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFINITION_IND` | DOUBLE | NOT NULL |  | Indicates whether this row has been defined for:0 = both cyto alpha security and follwo-up tracking parameters.1 = cyto alpha security parameters only2 = follow-up tracking parameters only |
| 2 | `DEGREES_FROM_NORMAL` | DOUBLE |  |  | This field contains a numeric value documenting the relative comparison of the designated alpha response (nomenclature) value to the normal diagnosis response. The greater the number, the more abnormal the response. |
| 3 | `DIAGNOSTIC_CATEGORY_CD` | DOUBLE | NOT NULL |  | This field value contains the internal identification code of the diagnostic category associated with the alpha response (nomenclature) code. Diagnostic categories are defined on codeset 1314. |
| 4 | `FOLLOWUP_FINAL_INTERVAL` | DOUBLE |  |  | This field value contains the number of days post report verification that should elapse before a report having the associated alpha response (nomenclature) value for the diagnosis is due for printing on the final overdue follow-up tracking report. |
| 5 | `FOLLOWUP_FIRST_INTERVAL` | DOUBLE |  |  | This field value contains the number of days post report verification that should elapse before a report having the associated alpha response (nomenclature) value for the diagnosis is due for printing on the initial overdue follow-up tracking report. |
| 6 | `FOLLOWUP_INITIAL_INTERVAL` | DOUBLE |  |  | This field value contains the number of days post report verification that should elapse before a report having the associated alpha response (nomenclature) value for the diagnosis is due for printing on the initial notification follow-up tracking report. |
| 7 | `FOLLOWUP_TERMINATION_INTERVAL` | DOUBLE |  |  | This field value contains the number of days post report verification that should elapse before a report having the associated alpha response (nomenclature) value for the diagnosis is due for being removed from the AP_FT_EVENT activity table. |
| 8 | `FOLLOWUP_TRACKING_TYPE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the follow-up tracking type to which the alpha response (nomenclature) value is assigned. Follow-up tracking types are stored on codeset 1317. |
| 9 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the nomenclature response documenting the diagnosis (the alpha response value for which this table entry is associated). This value could be used to join to the NOMENCLATURE table. |
| 10 | `QA_FLAG_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains a flag value documenting the generic categorization that is associated with cases having the associated alpha response entered as the diagnosis. Categorizations include normal, atypical, abnormal, and unsatisfactory, for example. |
| 11 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the table storing the reference range (alpha response values, in this example) information for the diagnosis alpha response report component. |
| 12 | `REQUEUE_FLAG` | DOUBLE |  |  | This field contains a flag value documenting how (and if) requeueing occurs when a user selects the associated alpha response (nomenclature) value as the diagnosis but where the user has insufficient security to verify (also based on the alpha response). |
| 13 | `REQUEUE_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | If a requeue to service resource value is defined for the alpha response (nomenclature) code, this field contains the internal identification code associated with the response. This value could be used to join to the location tables and codesets. |
| 14 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The routing location for which these cytology alpha security settings are defined. A value of 0.0 in this field signifies these are default cytology alpha security settings. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `VERIFY_LEVEL_IS` | DOUBLE |  |  | This field contains the numeric verification security level that a user must meet or exceed in order to be able to verify, at the time of initial screening, a case having the associated alpha response (nomenclature) code designated as the diagnosis. |
| 21 | `VERIFY_LEVEL_RS` | DOUBLE |  |  | This field contains the numeric verification security level that a user must meet or exceed in order to be able to verify, at the time of rescreening, a case having the associated alpha response (nomenclature) code designated as the diagnosis. |
| 22 | `WORKLOAD_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FOLLOWUP_TRACKING_TYPE_CD` | [AP_FT_TYPE](AP_FT_TYPE.md) | `FOLLOWUP_TRACKING_TYPE_CD` |
| `NOMENCLATURE_ID` | [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `NOMENCLATURE_ID` |
| `REFERENCE_RANGE_FACTOR_ID` | [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `REFERENCE_RANGE_FACTOR_ID` |
| `REQUEUE_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

