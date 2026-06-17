# OMF_RULE_DTL

> Stores the clinical event level information pertaining to a turnaround time rule - turnaround time method and definition.

**Description:** Stores the clinical event level information pertaining to a turnaround time rule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_NUM` | DOUBLE | NOT NULL |  | The ending clinical event in the event range defining the turnaround time interval. |
| 2 | `EXPECTED_TAT` | DOUBLE |  |  | The expected turnaround time for an event range using the elapsed method. |
| 3 | `INBY_TIME` | VARCHAR(8) |  |  | The in by qualifying time for an event range using the in by/out by method. |
| 4 | `IN_OUT_ADD_DAYS` | DOUBLE |  |  | The number of additional days defined for an event range using the in by/out by method. |
| 5 | `OUTBY_TIME` | VARCHAR(8) |  |  | The out by qualifying time for an event range using the in by/out by method. |
| 6 | `RULE_ID` | DOUBLE | NOT NULL |  | The unique identification number for a turnaround time rule. |
| 7 | `TAT_FLAG` | DOUBLE |  |  | The method used for defining the turnaround times. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

