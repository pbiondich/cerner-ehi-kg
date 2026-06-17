# HF_F_ENCOUNTER

> The encounter table contains patient information for a specific period of time that a person comes in contact with a healthcare provider (i.e., inpatient hospital stay, outpatient clinic visit, office visit, phone call to the doctor, etc.).

**Description:** HF_F_ENCOUNTER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 44

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMISSION_SOURCE_ID` | DOUBLE |  |  | The admission source id is a unique identifier used to join the admission_source dimension to the hf_f_encounter table. |
| 2 | `ADMISSION_TYPE_ID` | DOUBLE |  |  | The admission type id is a unique identifier used to join the admission_type dimension to the hf_f_encounter table. |
| 3 | `ADMITTED_DT_ID` | DOUBLE |  |  | The admit date id is used to join the hf_f_encounter table to the date dimension table. |
| 4 | `ADMITTED_DT_TM` | DATETIME |  |  | The date/time that the patient was admitted. |
| 5 | `ADMITTED_TM_VALID_IND` | DOUBLE |  |  | Indicates if the admitted date is a valid date. |
| 6 | `ADMITTING_DIAGNOSIS_1_ID` | DOUBLE |  |  | A unique identifier used to link the admitting_diagnosis dimension table to the hf_f_encounter table. Free text field describing the reason the patient was admitted. |
| 7 | `ADMITTING_DIAGNOSIS_2_ID` | DOUBLE |  |  | A unique identifier used to link the admitting_diagnosis dimension table to the hf_f_encounter table. Free text field describing the reason the patient was admitted. |
| 8 | `ADMITTING_DIAGNOSIS_3_ID` | DOUBLE |  |  | A unique identifier used to link the admitting_diagnosis dimension table to the hf_f_encounter table. Free text field describing the reason the patient was admitted. |
| 9 | `ADMITTING_PHYSICIAN_ID` | DOUBLE |  |  | The physician id is a unique identifier used to link the physician dimension table to fact tables. |
| 10 | `AGE_IN_DAYS` | DOUBLE |  |  | The persons age in days if 2 days thru 2 weeks old. Values 2 - 13 days. This value is blank if the age was extracted to only the whole year detail. |
| 11 | `AGE_IN_HOURS` | DOUBLE |  |  | The persons age in hours, if less than 2 days old. Values 0-47 hours. This value is blank if the age was extracted to only the whole year detail. If hours, days, weeks, months, and years are all equal 0, then these persons are less than 1 hour. |
| 12 | `AGE_IN_MONTHS` | DOUBLE |  |  | The persons age in months if 3 months thru 2 years. Values 3-23 months. This value is blank if the age was extracted to only the whole year detail. |
| 13 | `AGE_IN_WEEKS` | DOUBLE |  |  | The persons age in weeks if 2 weeks thru 3 months. Values 2-8 weeks. This value is blank if the age was extracted to only the whole year detail. |
| 14 | `AGE_IN_YEARS` | DOUBLE |  |  | The age of the patient at admission (calculated from admit date-date of birth). If age can be computed to the hours-months level, then age in years will be greater than or equal to 2 years, the other age fields will be 0. Age in years will equal the intege |
| 15 | `ARRIVAL_MODE_CODE` | VARCHAR(10) |  |  | Admit mode code which identifies the method by which the patient arrived. (i.e., helicopter, ambulance, etc.) |
| 16 | `ARRIVAL_MODE_DESC` | VARCHAR(100) |  |  | Admit mode description which identifies the method by which the patient arrived. (i.e., helicopter, ambulance, etc.) |
| 17 | `ATTENDING_PHYSICIAN_ID` | DOUBLE |  |  | The foreign key of the attending physician associated to the encounter. |
| 18 | `BILLING_IND` | DOUBLE |  |  | Yes (1)/No (0) flag indicating whether this encounter received billing information. Prior to 2009, this indicator should correlate to visits that also have diagnoses or procedures. |
| 19 | `DIAGNOSTIC_GROUPING_ID` | DOUBLE |  |  | The diagnostic grouping id is a unique identifier used to link the diagnostic groupings dimension table to the hf_f_encounter table. The diagnostic grouping identifies the MDC and DRG for the encounter if billing data were received. |
| 20 | `DISCHARGED_DT_ID` | DOUBLE |  |  | The foreign key to the date that the patient was discharged. |
| 21 | `DISCHARGED_DT_TM` | DATETIME |  |  | The date/time that the patient was discharged. |
| 22 | `DISCHARGED_TM_VALID_IND` | DOUBLE |  |  | Indicates if the discharged date is a valid date. |
| 23 | `DISCHARGE_CARESETTING_ID` | DOUBLE |  |  | Identifies the last (discharge) patient caresetting for the encounter. A unique identifier used to link the caresetting dimension table to the hf_f_encounter table. |
| 24 | `DISCHARGE_DISPOSITION_ID` | DOUBLE |  |  | The discharge disposition id is a unique identifier used to link the discharge_disposition dimension table to the hf_f_encounter table. If summarizing discharge disposition, use the encounters where discharge disposition not NULL as the population. |
| 25 | `ENCOUNTER_ID` | DOUBLE |  |  | The unique identifier from the source system of the encounter. |
| 26 | `FINANCIAL_NBR` | VARCHAR(40) |  |  | The formatted Financial Number of the encounter. |
| 27 | `FINANCIAL_NBR_RAW` | VARCHAR(40) |  |  | The unformatted Medical Record Number of the encounter. |
| 28 | `FORMATTED_MEDICAL_RECORD_NBR` | VARCHAR(40) |  |  | The formatted Medical Record Number of the encounter. |
| 29 | `HOSPITAL_ID` | DOUBLE |  |  | The hospital id is a unique identifier for the facility. The id is used to link the hospital dimension table to facts table. |
| 30 | `MEDICAID_IND` | DOUBLE |  |  | Indicates if the encounter qualifies for Medicaid. |
| 31 | `MEDICAL_SERVICE_ID` | DOUBLE |  |  | The unique identifier for the type or category of medical service that was received. |
| 32 | `MEDICARE_IND` | DOUBLE |  |  | Indicates if the encounter qualifies for Medicare. |
| 33 | `ORG_ENCOUNTER_NBR` | DOUBLE |  |  | The identifier of the organization that the encounter occurred within. |
| 34 | `PARTITION_DT_TM` | DATETIME |  |  | A column used to partition the table by. The date is generated based upon when the encounter was discharged. |
| 35 | `PATIENT_ID` | DOUBLE |  |  | The id used within the Cerner Health Facts Data Warehouse to join to the patient dim table for additional person information such as gender, race, and marital status. Patient sk on the dim table identifies the unique person. |
| 36 | `PATIENT_TYPE_ID` | DOUBLE |  |  | A unique identifier used to join the patient_type dimension table to the hf_f_encounter table. |
| 37 | `PAYER_ID` | DOUBLE |  |  | A unique identifier used to link the payer dimension table to the hf_f_encounter table. |
| 38 | `RAW_MEDICAL_RECORD_NBR` | VARCHAR(40) |  |  | The unformatted Medical Record Number of the encounter. |
| 39 | `TOTAL_CHARGES` | DOUBLE |  |  | The total charges ($) for the encounter. Total Charges includes both covered and non-covered charges. If summarizing total charges, use the encounters where total charges is not NULL or zero (0) as the population. If NULL that means billing was not received. |
| 40 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 41 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 42 | `UPDT_USER` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, MANUAL should be entered. |
| 43 | `WEIGHT` | DOUBLE |  |  | The weight of the patient. Weight is sparsely populated. Many of the weights extracted are 0 or NULL. Those that are populated should be used with reservation. Also check the clinical event table for addition weights if available. |
| 44 | `WEIGHT_UNIT_ID` | DOUBLE |  |  | A unique identifier used to link the unit dimension table to the encounter fact table. This field defines the unit for the weight entered. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

