# PM_TRANSACTION2

> Extension table to the pm_transaction table

**Description:** Person Management Transaction 2  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABS_N_BIRTH_DT_TM` | DATETIME |  |  | Absolute date stored for birth date that is always saved using GMT instead of the system time zone or the _tz column. |
| 2 | `ABS_O_BIRTH_DT_TM` | DATETIME |  |  | Absolute date stored for birth date that is always saved using GMT instead of the system time zone or the _tz column. |
| 3 | `N_BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `N_SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | New service category code was captured in. |
| 5 | `N_SPECIALTY_UNIT_CD` | DOUBLE | NOT NULL |  | Represents the current specialty unit associated with the program service of the patient |
| 6 | `O_BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 7 | `O_SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Old service category code was captured in. |
| 8 | `O_SPECIALTY_UNIT_CD` | DOUBLE | NOT NULL |  | Represents the old specialty unit associated with the program service of the patient registration |
| 9 | `TRANSACTION_DT_TM` | DATETIME |  |  | The date and time of the transaction. |
| 10 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Unique identifier for the transaction |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

