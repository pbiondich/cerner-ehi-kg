# HF_D_TEST_TYPE

> This is the HealthFacts dimension table that contains standard values for susceptibility test types

**Description:** HF_D_Test_Type  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `TEST_TYPE_DESC` | VARCHAR(40) |  |  | The textual description for the type of susceptibility test (Minimum Inhibitory Concentration, Kirby Bauer, etc.) |
| 2 | `TEST_TYPE_ID` | DOUBLE |  |  | A unique non-intelligent identifier for the table |
| 3 | `TEST_TYPE_MNEMONIC` | VARCHAR(25) |  |  | A standard abbreviation for the type of susceptibility test (MIC, KB, etc.) |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

