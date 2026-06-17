# CE_CALCULATION_RESULT

> This table will store a new type of result for calculation equations.

**Description:** The Calculation equation Table to store calculated results.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALCULATION_RESULT` | VARCHAR(255) | NOT NULL |  | Calculation result of evaluation of the equation. |
| 2 | `CALCULATION_RESULT_FRMT_CD` | DOUBLE | NOT NULL |  | Code Set 14113Format of the calculation result : alpha/date/range/etc. |
| 3 | `EQUATION` | VARCHAR(2000) | NOT NULL |  | This field stores the equation used to calculate the result. Ex. MAP = SAP + (DAP x 2)/3 |
| 4 | `EVENT_ID` | DOUBLE | NOT NULL |  | Identifier to a logical event row in clinical_event table. This is NOT the CE ID |
| 5 | `LAST_NORM_DT_TM` | DATETIME |  |  | For HL7 compatibility |
| 6 | `UNIT_OF_MEASURE_CD` | DOUBLE | NOT NULL |  | CODE SET:54 Unit of measurement for result. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Creation date for row. Contains the "Beginning Point" of when a row in the table is valid. |
| 13 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. This indicates when |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

