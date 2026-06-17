# CE_STRING_RESULT

> The String Result Table is used to store both text result and interp result (?). In the case of simple text result the Equation_CD column will be empty and will not have Interp_Component.

**Description:** ce string result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALCULATION_EQUATION` | VARCHAR(512) |  |  | This field stores the equation used to calculate the result. Ex. MAP = SAP + (DAP x 2)/3 |
| 2 | `CRITICAL_HIGH` | VARCHAR(20) |  |  | Critical high/low values. |
| 3 | `CRITICAL_LOW` | VARCHAR(20) |  |  | Critical high/low values. |
| 4 | `EQUATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the equation table where the equation for the interp result is stored, if applicable. |
| 5 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the Event Table. |
| 6 | `FEASIBLE_IND` | DOUBLE |  |  | Indicates whether or not the result is within feasible limits. |
| 7 | `INACCURATE_IND` | DOUBLE |  |  | True if the result value is outside of the measuring instruments accurate limits. |
| 8 | `LAST_NORM_DT_TM` | DATETIME |  |  | (For HL7 compatibility) |
| 9 | `MODIFY_FLAG` | DOUBLE |  |  | this field is obsolete |
| 10 | `NORMAL_HIGH` | VARCHAR(20) |  |  | Normal high/low values. |
| 11 | `NORMAL_LOW` | VARCHAR(20) |  |  | Normal high/low values. |
| 12 | `STRING_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Long Text ID from the LONG_TEXT table. ID of the long_text row containing the string result text. |
| 13 | `STRING_RESULT_FORMAT_CD` | DOUBLE | NOT NULL |  | Format of a string result: alpha/date/range/approximation... |
| 14 | `STRING_RESULT_TEXT` | VARCHAR(255) | NOT NULL |  | Text. |
| 15 | `UNIT_OF_MEASURE_CD` | DOUBLE | NOT NULL |  | Unit of measurement for result. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when a row in the table is valid. |
| 22 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. We need to determine what that value is. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EQUATION_ID` | [EQUATION](EQUATION.md) | `EQUATION_ID` |
| `STRING_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

