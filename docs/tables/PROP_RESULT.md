# PROP_RESULT

> Result information for PROP orders.

**Description:** Contains the result information for PROP orders.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 44

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CRITICAL_CD` | DOUBLE | NOT NULL |  | Defines whether the result is a critical value. |
| 2 | `CRITICAL_HIGH` | DOUBLE |  |  | The defined high value the result is checked against to define when a result critical value is high. The result must be greater than the critical high to be flagged as high. |
| 3 | `CRITICAL_LOW` | DOUBLE |  |  | The defined low value the result is checked against to define when a result value is critical low. The result must be less than the normal low to be flagged as critical low. |
| 4 | `CRITICAL_RANGE_FLAG` | DOUBLE |  |  | Determines if a critical range has been defined. |
| 5 | `DELTA_CD` | DOUBLE | NOT NULL |  | Defines whether the result value has passed or failed a delta check. |
| 6 | `FEASIBLE_CD` | DOUBLE | NOT NULL |  | Describes whether a result has passed or failed feasible result ranges. |
| 7 | `INTERFACE_FLAG` | DOUBLE |  |  | Indicates how the result was entered into the table. |
| 8 | `LESS_GREAT_FLAG` | DOUBLE |  |  | Defines whether the result value should be viewed qualitatively with a < or > sign. |
| 9 | `LINEAR_CD` | DOUBLE | NOT NULL |  | Indicates whether a result has failed linear ranges. |
| 10 | `MAX_DIGITS` | DOUBLE |  |  | Maximum digits for a result. |
| 11 | `MIN_DECIMAL_PLACES` | DOUBLE |  |  | Minimum number of decimal places for a result. |
| 12 | `MIN_DIGITS` | DOUBLE |  |  | Minimum digits for a result. |
| 13 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Defines the nomenclature selected for an alpha response. This is a unique, internal identification for nomenclature. |
| 14 | `NORMAL_ALPHA` | VARCHAR(200) |  |  | Defines the normal alpha response for a procedure with the result type of alpha. |
| 15 | `NORMAL_CD` | DOUBLE | NOT NULL |  | Defines the result to be normal, low, or high based on the result value as compared to the reference ranges. Designates if the ranges have been checked or not. |
| 16 | `NORMAL_HIGH` | DOUBLE |  |  | The defined high value the result is checked against to define when a result value is high. The result must be greater than the normal high to be flagged as high. |
| 17 | `NORMAL_LOW` | DOUBLE |  |  | The defined low value the result is checked against to define when a result value is low. The result must be less than the normal low to be flagged as low. |
| 18 | `NORMAL_RANGE_FLAG` | DOUBLE |  |  | Indicates if a critical range has been defined. |
| 19 | `NOTIFY_CD` | DOUBLE | NOT NULL |  | Indicates the notify flag is applied to this result value. |
| 20 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the order. |
| 21 | `PROMPT_TEST_IND` | DOUBLE |  |  | Indicates that the result is a prompt test. |
| 22 | `QC_OVERRIDE_CD` | DOUBLE |  |  | A code value that identifies if the user has chosen to override the quality control validation when posting this result to the system. |
| 23 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | Used to store the ID value from REFERENCE_RANGE_FACTOR |
| 24 | `RESOURCE_ERROR_CODES` | VARCHAR(255) |  |  | Stores the error codes sent by an automated instrument while processing a result. |
| 25 | `RESULT_ALPHA` | VARCHAR(200) |  |  | Stores the alpha value text of an alpha procedure. |
| 26 | `RESULT_COMMENT_ID` | DOUBLE | NOT NULL |  | A unique internal system assigned number that identifies a result comment text. Creates a relationship with the long text table. |
| 27 | `RESULT_DISPLAY_VALUE` | VARCHAR(255) |  |  | The result display value. |
| 28 | `RESULT_DT_TM` | DATETIME |  |  | The date and time fhe result was performed by the user. This applies to all types of results. |
| 29 | `RESULT_DT_TM_VALUE` | DATETIME |  |  | The date and time the result was performed. This is populated only with the result value of data and time for procedures that are date/time result types. |
| 30 | `RESULT_NOTE_ID` | DOUBLE | NOT NULL |  | A unique internal system assigned number that identifies a result note text. Creates a relationship with the long text table. |
| 31 | `RESULT_PERSONNEL_ID` | DOUBLE | NOT NULL |  | Identifies the person responsible for the result. |
| 32 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the result, such as performed or verified. |
| 33 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of result. |
| 34 | `RESULT_TYPE_FLAG` | DOUBLE |  |  | Indicates the type of result for prompt tests. |
| 35 | `RESULT_VALUE` | DOUBLE | NOT NULL |  | The discrete result value. |
| 36 | `REVIEW_CD` | DOUBLE | NOT NULL |  | Defines whether a result has been flagged for review. Also denotes whether the review ranges have been applied. |
| 37 | `STATUS_FLAG` | DOUBLE |  |  | The status of the result processing. |
| 38 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The task assay code of the detail test. |
| 39 | `UNITS_CD` | DOUBLE | NOT NULL |  | Defines the units of measure for interpreting the result value for the procedure. |
| 40 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 41 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 42 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 43 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 44 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `REFERENCE_RANGE_FACTOR_ID` | [REFERENCE_RANGE_FACTOR](REFERENCE_RANGE_FACTOR.md) | `REFERENCE_RANGE_FACTOR_ID` |

