# CCL_FUNCTIONS

> ccl functions

**Description:** ccl functions  
**Table type:** REFERENCE  
**Primary key:** `FUNCTION_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FORMAT_IND` | DOUBLE | NOT NULL |  | Indicates whether the function supports an attached format string |
| 2 | `FUNCTION_DESCRIPTION` | VARCHAR(200) |  |  | Details on the function and its usage |
| 3 | `FUNCTION_ID` | DOUBLE | NOT NULL | PK | Unique function identifier |
| 4 | `FUNCTION_NAME` | VARCHAR(30) | NOT NULL |  | Discern Explorer function name |
| 5 | `FUNCTION_TYPE` | VARCHAR(4) | NOT NULL |  | Used to categorize function types. For example: AGG (Aggregate), BIT (Bitwise logic) MATH (Numeric), MISC, STR (String), DTTM (Date/Time), UAR |
| 6 | `PLANJOIN_IND` | DOUBLE | NOT NULL |  | Indicates whether the function's usage is valid in the qualifications portion of a query |
| 7 | `QUALIFIER_IND` | DOUBLE | NOT NULL |  | Indicates whether a function supports the WHERE clause syntax |
| 8 | `RETURN_TYPE` | VARCHAR(4) | NOT NULL |  | The data type returned when the function is evaluated. Example: NULL, INT, STR, DTTM, etc. |
| 9 | `SELECT_IND` | DOUBLE | NOT NULL |  | select indicator |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CCL_FUNCTION_DET](CCL_FUNCTION_DET.md) | `FUNCTION_ID` |
| [CCL_FUNCTION_PARAMS](CCL_FUNCTION_PARAMS.md) | `FUNCTION_ID` |

