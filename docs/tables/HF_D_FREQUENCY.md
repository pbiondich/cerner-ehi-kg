# HF_D_FREQUENCY

> This is the HealthFacts dimension table that contains standard values for frequency

**Description:** HF_D_FREQUENCY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FREQUENCY_DESC` | VARCHAR(60) |  |  | The description for the frequency |
| 2 | `FREQUENCY_DISP` | VARCHAR(40) |  |  | The display for the frequency |
| 3 | `FREQUENCY_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a frequency |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

