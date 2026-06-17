# HF_F_DIAGNOSIS

> This is the fact table that contain all diagnoses for patients for given encounter (visit)

**Description:** HF_F_DIAGNOSIS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIAGNOSIS_FACT_ID` | DOUBLE |  |  | The unique identifier from the diagnosis table |
| 2 | `DIAGNOSIS_ID` | DOUBLE |  |  | The link to the diagnosis such as ICD-9-CM diagnosis (Unspecified Anemia) |
| 3 | `DIAGNOSIS_PRIORITY` | DOUBLE |  |  | A number identifying the series of a diagnosis within an encounter. The diagnoses are assigned by a medical records coder for billing purposes retrospective to the encounter. The principal diagnosis (sequence =1) is the condition established after study to be chiefly responsible for the admission. The secondary diagnoses (sequences 2-9) are additional conditions that coexist at the time of admission or develop subsequently that have an effect on the treatment received or the the length of stay. |
| 4 | `DIAGNOSIS_TYPE_ID` | DOUBLE |  |  | The type of diagnosis such as admitting diagnosis, final diagnosis etc. |
| 5 | `DISCHARGE_DT_TM` | DATETIME |  |  | The patient discharged date and time |
| 6 | `ENCOUNTER_ID` | DOUBLE |  |  | The visit key for the encounter. This is unique to the patient |
| 7 | `HOSPITAL_ID` | DOUBLE |  |  | The hospital key is a unique identifier for the facility. The key is used to link the hospital dimension table to encounter_facts table." |
| 8 | `PARTITION_DT_TM` | DATETIME |  |  | Indicates which partition of the table this record is in. Matches the partition date/time of the parent encounter |
| 9 | `PRESENT_ON_ADMIT_ID` | DOUBLE |  |  | A number identifying Present on Admission of a diagnosis |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_USER` | VARCHAR(40) |  |  | The user who last modified this record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

