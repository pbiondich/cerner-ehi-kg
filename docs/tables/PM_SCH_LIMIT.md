# PM_SCH_LIMIT

> Search Limit.

**Description:** Search Limit.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATE_FLAG` | DOUBLE | NOT NULL |  | Flag that determines which date to use in as a limit. |
| 2 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Encounter type class is used to categorize patients into more general groups than encounter type. (i.e., inpatient, outpatient, emergency, recurring outpatient). The values in this codeset all have Cerner defined meanings. |
| 3 | `NUM_DAYS` | DOUBLE | NOT NULL |  | Number of Days. |
| 4 | `SETUP_ID` | DOUBLE | NOT NULL |  | Setup ID. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

