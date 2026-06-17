# HF_F_PSP_ENCOUNTER

> This is an encounter level fact table for the PSP rules

**Description:** HF_F_PSP_ENCOUNTER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIT_DATE_ID` | DOUBLE | NOT NULL |  | Links to HF_D_Date to define the admit date |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The admit date of the encounter (included for troubleshooting and easy querying purposes) |
| 3 | `ADMIT_TM_VALID_FLG` | DOUBLE |  |  | Indicates if the admit date has a valid timestamp |
| 4 | `AGE_IN_YEARS` | DOUBLE |  |  | Defines the age of a person at admission in years |
| 5 | `BILLING_JOIN_NBR` | VARCHAR(40) |  |  | The number used to join billing and clinical date together |
| 6 | `DISCHARGE_DATE_ID` | DOUBLE | NOT NULL |  | Links to HF_D_Date to define a discharge date |
| 7 | `DISCHARGE_DT_TM` | DATETIME |  |  | The discharge date of the encounter (included for troubleshooting and easy querying purposes) |
| 8 | `DISCHARGE_TM_VALID_FLG` | DOUBLE |  |  | Indicates if the discharge date has a valid timestamp |
| 9 | `DISCHG_DISP_ID` | DOUBLE | NOT NULL |  | Links to HF_D_Disch_Disp to define the discharge disposition |
| 10 | `DRG_ID` | DOUBLE | NOT NULL |  | Links to HF_D_Drg to define the DRG |
| 11 | `ENCOUNTER_ID` | DOUBLE | NOT NULL |  | Uniquely defines an encounter (without taking HF create encounter logic into account). Links to the encounter_key on WH_CLN_ENCOUNTER |
| 12 | `ENCOUNTER_SK` | VARCHAR(40) |  |  | The unique value assigned to each patient visit. |
| 13 | `FORMATTED_MEDICAL_RECORD_NBR` | VARCHAR(40) |  |  | The formatted patient medical record number |
| 14 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system, but may be adjusted if there is >1 HF feed from the client. |
| 15 | `HOSPITAL_ID` | DOUBLE | NOT NULL |  | Links to HF_D_Hospital to identify the hospital associated with an encounter |
| 16 | `MDC_ID` | DOUBLE | NOT NULL |  | Links to HF_D_Mdc to define the MDC |
| 17 | `MORTALITY_IND` | DOUBLE |  |  | Indicates if the for this encounter has died or not (calculated based on Dischg_Disp_ID) |
| 18 | `PARTITION_DT_TM` | DATETIME |  |  | Used to break up tables by partition. This is the admit date if available. Otherwise, it is the first process date of the record |
| 19 | `PSP_ENCOUNTER_KEY` | DOUBLE |  |  | Uniquely identifies a PSP Encounter record |
| 20 | `RULE_FIRED_IND` | DOUBLE |  |  | Indicates if this encounter had any ADE rules fired |
| 21 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `UPDT_USER` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 24 | `VISIT_ID` | DOUBLE | NOT NULL |  | Uniquely defines an encounter (taking HF create encounter logic into account). Links to the visit_key on WH_CLN_ENCOUNTER |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

