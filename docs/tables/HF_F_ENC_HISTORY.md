# HF_F_ENC_HISTORY

> Contains the history of location, encntr type, med service, and alt level of care changes for a specific encounter.

**Description:** HF_F_ENC_HISTORY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_DT_ID` | DOUBLE |  |  | A date id is a unique identifier used to link the hf_f_enc_history table to the date table. |
| 2 | `BEGIN_DT_TM` | DATETIME |  |  | The beginning date and time when the person was at this location during the encounter. |
| 3 | `CARESETTING_ID` | DOUBLE |  |  | The patient caresetting (location). A unique identifier used to link the caresetting dimension table to the hf_f_enc_history table. |
| 4 | `DISCHARGED_DT_TM` | DATETIME |  |  | Used internally to identify which month/quarter the encounter occurred in. The original discharge date time. However, there is a small chance that the discharged_dt_tm on this fact does not match the discharged_dt_tm on the hf_f_encounter table. |
| 5 | `ENCOUNTER_ID` | DOUBLE |  |  | The visit identifier for the encounter. |
| 6 | `END_DT_ID` | DOUBLE |  |  | A date id is a unique identifier used to link the hf_f_enc_history table to the date table. |
| 7 | `END_DT_TM` | DATETIME |  |  | The end date and time when the person was at this location during the encounter. |
| 8 | `ESTIMATE_IND` | DOUBLE |  |  | Indicates that the times of the history are estimates. |
| 9 | `HOSPITAL_ID` | DOUBLE |  |  | The identifier for the hospital in which the encounter occurred. |
| 10 | `PARTITION_DT_TM` | DATETIME |  |  | A column used to partition the table by. The date is generated based upon when the encounter was discharged. |
| 11 | `PATIENT_TYPE_ID` | DOUBLE |  |  | A unique identifier used to join the patient_type dimension table to the hf_f_encounter table. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `UPDT_USER` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, MANUAL should be entered. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

