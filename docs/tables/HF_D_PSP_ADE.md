# HF_D_PSP_ADE

> This is the HealthFacts dimension table that contains standard values for adverse drug events checked for by PSP rules

**Description:** HF_D_PSP_ADE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADE_ID` | DOUBLE | NOT NULL |  | Primary key to the table. Uniquely identifies an adverse drug event |
| 2 | `RULE_DESCRIPTION` | VARCHAR(250) |  |  | The description of the purpose of the PSP rule |
| 3 | `RULE_NAME` | VARCHAR(60) |  |  | The name of the PSP rule |
| 4 | `RULE_NBR` | DOUBLE |  |  | The PSP rule associated with this ADE |
| 5 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 6 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 7 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

