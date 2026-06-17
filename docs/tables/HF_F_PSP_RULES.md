# HF_F_PSP_RULES

> This fact table contains information on encounters that triggered any of the PSP rules

**Description:** HF_F_PSP_RULES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADE_ID` | DOUBLE | NOT NULL |  | Links to HF_D_Ade to define the adverse drug event |
| 2 | `DRUG_ID` | DOUBLE | NOT NULL |  | Links to HF_D_Drug to define the drug |
| 3 | `ENCOUNTER_ID` | DOUBLE | NOT NULL |  | Uniquely defines an encounter (without taking HF create encounter logic into account). Links to the encounter_key on WH_CLN_ENCOUNTER |
| 4 | `ENCOUNTER_SK` | VARCHAR(40) |  |  | The unique value assigned to each patient visit. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system, but may be adjusted if there is >1 HF feed from the client. |
| 6 | `HOSPITAL_ID` | DOUBLE | NOT NULL |  | Links to HF_D_Hospital to identify the hospital associated with an encounter |
| 7 | `NBR_LABS_WORSEN_AFTER_1ST_FIRE` | DOUBLE |  |  | Number of lab results that indicate a declining condition after the ADE was triggered |
| 8 | `NBR_OF_DRUG_ORDERS` | DOUBLE |  |  | The number of medication orders that triggered this ADE |
| 9 | `NBR_OF_HOURS_AFTER_1ST_FIRE` | DOUBLE |  |  | Number of hours since the ADE was triggered to the discontinuationof the drug |
| 10 | `NBR_OF_LABS_AFTER_1ST_FIRE` | DOUBLE |  |  | Number of labs found by this ADE after the first lab triggered the ADE |
| 11 | `NBR_OF_TIMES_RULE_FIRED` | DOUBLE |  |  | The number of times this ADE was triggered |
| 12 | `PARTITION_DT_TM` | DATETIME |  |  | Used to break up tables by partition. This is the admit date if available. Otherwise, it is the first process date of the record |
| 13 | `PSP_RULES_KEY` | DOUBLE |  |  | Uniquely identifies a PSP Rules record |
| 14 | `TEST_ID` | DOUBLE | NOT NULL |  | LInks to HF_D_Test to define the lab test |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 16 | `UPDT_TASK` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |
| 17 | `UPDT_USER` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 18 | `VISIT_ID` | DOUBLE | NOT NULL |  | Uniquely defines an encounter (taking HF create encounter logic into account). Links to the visit_key on WH_CLN_ENCOUNTER |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

