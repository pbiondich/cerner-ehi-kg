# CV_CASE

> CVNet Omf summary table

**Description:** CVNet Omf Summary table. Stores non clinical events that are related to case  
**Table type:** ACTIVITY  
**Primary key:** `CV_CASE_ID`  
**Columns:** 47  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMT_DT_NBR` | DOUBLE |  |  | Admission Date NumberColumn |
| 6 | `AGE` | DOUBLE |  |  | Age of Patient in yearsColumn |
| 7 | `AGE_GROUP_CD` | DOUBLE | NOT NULL |  | Patients age,grouped into different ranges for easy reporting |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CASE_DT_TM` | DATETIME |  |  | The primary date associated with this case (e.g., SURGDT for STS, PROCDT for ACC LabVisit, ADMITDT for ACC Admission). |
| 10 | `CHART_DT_TM` | DATETIME |  |  | Charted Date and TimeColumn |
| 11 | `CV_CASE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the cv_case table. It is an internal system assigned number |
| 12 | `CV_CASE_NBR` | DOUBLE |  |  | ** OBSOLETE ** Formatted Case Number for this case. This column has been replaced by column CASE_NUMBER |
| 13 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 14 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 15 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 16 | `DEATH_IND` | DOUBLE |  |  | Death indicator-This flag is set on when a patient dies in the hospital. It is used in CVNet Management reporting |
| 17 | `DISCH_DT_NBR` | DOUBLE |  |  | Discharge Date NumberColumn |
| 18 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 19 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 20 | `FORM_EVENT_ID` | DOUBLE | NOT NULL |  | This is the event_id from CLINICAL_EVENT. For imported data (for which there actually is no HNAM form/event) it?s a negative number corresponding to an external index system. |
| 21 | `FORM_ID` | DOUBLE | NOT NULL | FK→ | The Form Id for this Case if it is documented in PowerFormsColumn |
| 22 | `FORM_TYPE_CD` | DOUBLE | NOT NULL |  | Type of form(Admit, LabVisit). Unified form has form_type_cd=0 |
| 23 | `HOSPITAL_CD` | DOUBLE | NOT NULL |  | This is the location facility code. This field is the current patient location with a location type of facility. |
| 24 | `LOS_ADM_DISCH` | DOUBLE |  |  | Length of stay in days This is calculated as the difference between the date a patient is admitted and discharge |
| 25 | `LOS_ADM_PROC` | DOUBLE |  |  | Length of ADM - ProcedureColumn |
| 26 | `LOS_PROC_DISCH` | DOUBLE |  |  | Length of Discharge - ProcedureColumn |
| 27 | `NUM_HISTORY` | DOUBLE |  |  | Number of historyColumn |
| 28 | `NUM_OOLAB_COMPL` | DOUBLE |  |  | Number of out of lab complicationsColumn |
| 29 | `NUM_PRESENTN` | DOUBLE |  |  | Number of presentationColumn |
| 30 | `NUM_PROC` | DOUBLE |  |  | Number of Procedures.Column |
| 31 | `NUM_RFACTOR` | DOUBLE |  |  | Number of risk factors.Column |
| 32 | `PATIENT_TYPE_CD` | DOUBLE | NOT NULL |  | Patient type code is equivalent to encounter type class code in encounter table . It is used to categorize patients into more general groups than encounter type. (i.e., inpatient, outpatient, emergency, recurring outpatient) |
| 33 | `PAT_ADM_DT_TM` | DATETIME |  |  | This is the time the patient is registered. It is equivalent to register date and time in the encounter table |
| 34 | `PAT_ADM_IND` | DOUBLE |  |  | This indicator is set if a patient is admitted. This allows us to compute the number of patient admitted for a given period. |
| 35 | `PAT_DISCH_DT_TM` | DATETIME |  |  | The actual date/time that the patient was discharged from the facility. For most outpatients, this field may be null unless the user process requires capturing this data for example, day surgery. |
| 36 | `PAT_DISCH_IND` | DOUBLE |  |  | This is the indicator that reflects the statue of a patient. A discharged patient will have this flag set to 1 |
| 37 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 38 | `PROC_DT_NBR` | DOUBLE |  |  | Procedure Date NumberColumn |
| 39 | `SEX_CD` | DOUBLE | NOT NULL |  | The gender of the patient (i.e., male, female, unknown).Column |
| 40 | `SOURCE_CD` | DOUBLE | NOT NULL |  | The organization that have this dataset for example Apache |
| 41 | `UPDT_APP` | DOUBLE |  |  | The registered application number of the client applicaton that does the update. |
| 42 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 43 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 44 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 45 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 46 | `UPDT_REQ` | DOUBLE |  |  | The request Number of the application that performs the update |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FORM_ID` | [DCP_FORMS_ACTIVITY](DCP_FORMS_ACTIVITY.md) | `DCP_FORMS_ACTIVITY_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CV_CASE_ABSTR_DATA](CV_CASE_ABSTR_DATA.md) | `CV_CASE_ID` |
| [CV_CASE_DATASET_R](CV_CASE_DATASET_R.md) | `CV_CASE_ID` |
| [CV_DEVICE](CV_DEVICE.md) | `CV_CASE_ID` |
| [CV_PROCEDURE](CV_PROCEDURE.md) | `CV_CASE_ID` |

