# QMD_ABS_SUBMISSION_RPT

> This table stores the submission level report data for clinically abstracted data.

**Description:** QMD_ABS_SUBMISSION_RPT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time that the admission process is performed. |
| 2 | `BIRTH_DT_TM` | DATETIME |  |  | The birth date time of the patient |
| 3 | `CCN_NAME` | VARCHAR(150) |  |  | Stores the name associated to the CCN. |
| 4 | `CCN_NBR_TXT` | VARCHAR(150) |  |  | The CMS Certification Number (CCN) used to uniquely identify a Facility. |
| 5 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | The patients community medical record number. |
| 6 | `DISCHARGE_DT_TM` | DATETIME |  |  | The actual date/time that the patient was discharged from the facility. |
| 7 | `ENCNTR_ID` | DOUBLE |  |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 8 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 9 | `NAME_FULL` | VARCHAR(100) |  |  | The full name of the patient. |
| 10 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 11 | `TABLE_NAME` | VARCHAR(25) |  |  | The name of the table that the record points to. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that the patient record was added |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

