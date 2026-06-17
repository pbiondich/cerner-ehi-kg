# HF_D_PSP_DRUG_CLASS

> This is the HealthFacts dimension table that contains standard values for therapeutic classes used in the PSP Rules

**Description:** HF_D_PSP_DRUG_CLASS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | Indicates if the therapeutic class is active |
| 2 | `ADE_ID` | DOUBLE | NOT NULL |  | A link to the adverse drug event associated with this therapeutic class |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | Defines when HealthFacts first used this therapeutic class in the PSP rules |
| 4 | `DRUG_CLASS_ID` | DOUBLE | NOT NULL |  | Primary key to the table. Uniquely identifies a drug therapeutic class (or a drug therapeutic class name pattern) |
| 5 | `DRUG_CLASS_VALUATION_STRING` | VARCHAR(2000) |  |  | Contains either a therapeutic class name or a pattern describing multiple therapeutic class names |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | Defines when HealthFacts will discontinue using this therapeutic class in the PSP rules |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 8 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 9 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

