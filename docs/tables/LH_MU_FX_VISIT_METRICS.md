# LH_MU_FX_VISIT_METRICS

> Fact table for Meaningful Use Functional Reporting

**Description:** LH_MU_FX_VISIT_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 43

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | Identifies whether the encounter record is active. |
| 2 | `ALLERGY_DOC_IND` | DOUBLE |  |  | Indicates that a least one entry or an indication of no allergies are known for the patient, recorded as structured data.This is the Numerator for the Allergy Report. |
| 3 | `CLIN_SUMMARY_IND` | DOUBLE |  |  | Indicates a Clinical Summary was given within 3 business days or was held for reason |
| 4 | `CPOE_DENOM_IND` | DOUBLE |  |  | Indicates that the patient qualifies for the CPOE denominator. |
| 5 | `CPOE_NUM_IND` | DOUBLE |  |  | Indicates that the patient qualifies for the CPOE numerator. |
| 6 | `DEMOGRAPHICS_DOC_IND` | DOUBLE |  |  | Indicates that the patient has a sex and DOB documented.This is used for the Numerator for the Demographics Report. |
| 7 | `DEMOG_ETHN_DOC_IND` | DOUBLE |  |  | Indicates that the patient has an ethnicity documented.This is used for the Numerator for the Demographics Report. |
| 8 | `DEMOG_LANG_DOC_IND` | DOUBLE |  |  | Indicates that the patient has a language documented.This is used for the Numerator for the Demographics Report. |
| 9 | `DEMOG_RACE_DOC_IND` | DOUBLE |  |  | Indicates that the patient has a race documented.This is used for the Numerator for the Demographics Report. |
| 10 | `DIAG_DOC_IND` | DOUBLE |  |  | Indicates that a least one entry or an indication of no problems are known for the patient, recorded as structured data in their diagnosis list.(from the Diagnosis table)This is used for the Numerator for the Problem Report. |
| 11 | `D_PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON table. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 13 | `ERX_ONLY_IND` | DOUBLE |  |  | Indicates that a visit qualifies for only the eRx measure |
| 14 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 15 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the record was inserted into the table. |
| 16 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 17 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 18 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The last date/time that the record was updated on the table. |
| 19 | `LH_MU_FX_VISIT_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_FX_VISIT_METRICS table. |
| 20 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the logical domain. This identifier allows the data to be grouped by logical domain. |
| 21 | `MEDICATION_DOC_IND` | DOUBLE |  |  | Indicates that a least one entry or an indication that the patient is not currently prescribed medication, recorded as structured data .This is the Numerator for the Medication List Report. |
| 22 | `MEDS_RECON_DENOM_IND` | DOUBLE |  |  | Indicates that medication reconciliation needed to be done.This is the Denominator for the Medication Reconciliation Report |
| 23 | `MEDS_RECON_IND` | DOUBLE |  |  | Indicates that medication reconciliation was done.This is the Numerator for the Medication Reconciliation Report |
| 24 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The unique ID of the table that the row on this table is a child of |
| 25 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The name of the table that the row on this table is a child of |
| 26 | `PAT_ED_DENOM_IND` | DOUBLE |  |  | This is the Denominator for the Patient Education Report |
| 27 | `PAT_ED_IND` | DOUBLE |  |  | Indicates that the patient received proper education upon discharge.This is the Numerator for the Patient Education Report |
| 28 | `PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 29 | `PROBLEM_DOC_IND` | DOUBLE |  |  | Indicates that a least one entry or an indication of no problems are known for the patient, recorded as structured data in their problem list.(from the Problem table)This is used for the Numerator for the Problem Report. |
| 30 | `SMOKING_STATUS_IND` | DOUBLE |  |  | Indicates that smoking status was documented. |
| 31 | `SUMMARY_TRAN_DENOM_IND` | DOUBLE |  |  | Indicates a Transfer order was created and a Summary of Care needed to be done.This is the Denominator for the Summary of Care at Transition Report. |
| 32 | `SUMMARY_TRAN_IND` | DOUBLE |  |  | Indicates a Summary of Care happened at transfer.This is the Numerator for the Summary of Care at Transition Report. |
| 33 | `TIMELY_ACCESS_IND` | DOUBLE |  |  | Indicates Timely Access (within 4 days) of clinical data was provided.This will be the Numerator for the Timely Access Report |
| 34 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. |
| 35 | `UPDT_DT_TM` | DATETIME |  |  | The date/time the row was last inserted or updated. |
| 36 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 37 | `UPDT_TASK` | VARCHAR(50) |  |  | The application responsible for updating the record. |
| 38 | `VISIT_DT_TM` | DATETIME |  |  | The date and time of the patient's visit. |
| 39 | `VISIT_UTC_DT_TM` | DATETIME |  |  | The date and time of the patient's visit converted to UTC. |
| 40 | `VITALS_DIASTOLIC_IND` | DOUBLE |  |  | Indicates that diastolic was documented. |
| 41 | `VITALS_HEIGHT_IND` | DOUBLE |  |  | Indicates that height was documented. |
| 42 | `VITALS_SYSTOLIC_IND` | DOUBLE |  |  | Indicates that systolic was documented. |
| 43 | `VITALS_WEIGHT_IND` | DOUBLE |  |  | Indicates that weight was documented. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

