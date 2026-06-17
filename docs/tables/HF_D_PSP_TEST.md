# HF_D_PSP_TEST

> This is the HealthFacts dimension table that contains standard values for groups of lab procedures checked for by the PSP rules

**Description:** HF_D_PSP_TEST  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | Indicates if the test is active |
| 2 | `ADE_ID` | DOUBLE | NOT NULL |  | The adverse drug event this test is associated with |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | Defines when HealthFacts first used this test in the PSP rules |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | Defines when HealthFacts will discontinue using this test in the PSP rules |
| 5 | `PSP_RULE_GROUP` | VARCHAR(25) |  |  | The group this test belongs to |
| 6 | `TEST_ID` | DOUBLE | NOT NULL |  | Primary key to the table. Uniquely identifies a test |
| 7 | `TEST_MNEMONIC` | VARCHAR(100) |  |  | A short description of the test |
| 8 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 9 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 10 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

