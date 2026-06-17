# HF_D_PSP_DRUG

> This is the HealthFacts dimension table that contains standard values for medications used in the PSP Rules

**Description:** HF_D_PSP_DRUG  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | Indicates if the drug is active |
| 2 | `ADE_ID` | DOUBLE | NOT NULL |  | A link to the adverse drug event associated with this drug |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | Defines when HealthFacts first used this drug in the PSP rules |
| 4 | `DRUG_ID` | DOUBLE | NOT NULL |  | Primary key to the table. Uniquely identifies a drug name (or a drug name pattern) |
| 5 | `DRUG_VALUATION_STRING` | VARCHAR(2000) |  |  | Contains either a drug name or a pattern describing a series of drug names |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | Defines when HealthFacts will discontinue using this drug in the PSP rules |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 8 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 9 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

