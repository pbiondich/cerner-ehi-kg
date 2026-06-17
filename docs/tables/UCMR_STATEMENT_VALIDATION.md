# UCMR_STATEMENT_VALIDATION

> This table stores relationships between worksheets statements and validation information. Includes numeric range validation and whether the statement is enabled for a specific sample.

**Description:** Unified Case Management Reference - Statement Validation  
**Table type:** REFERENCE  
**Primary key:** `UCMR_STATEMENT_VALIDATION_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PREV_UCMR_STMT_VALIDATION_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the statement validation information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 6 | `UCMR_STATEMENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the statement. |
| 7 | `UCMR_STATEMENT_VALIDATION_ID` | DOUBLE | NOT NULL | PK | This field contains the key that uniquely identifies a row on the UCMR_STATEMENT_VALIDATION table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALIDATION_CD` | DOUBLE | NOT NULL |  | A code value from any code set that is checked at activity time to determine if a valid selection from a code list was made. |
| 14 | `VALIDATION_NBR` | DOUBLE | NOT NULL |  | The number used for comparison with the statement accept value on the activity side to determine if the input is valid. |
| 15 | `VALIDATION_TEXT` | VARCHAR(250) |  |  | This field is used to store textual validation information for a worksheet statement (e.g. ensuring current date entered.) |
| 16 | `VALIDATION_TYPE_CD` | DOUBLE | NOT NULL |  | This field is used to store the internal code for the type of validation (e.g., minimum, maximum, etc.) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_UCMR_STMT_VALIDATION_ID` | [UCMR_STATEMENT_VALIDATION](UCMR_STATEMENT_VALIDATION.md) | `UCMR_STATEMENT_VALIDATION_ID` |
| `UCMR_STATEMENT_ID` | [UCMR_STATEMENT](UCMR_STATEMENT.md) | `UCMR_STATEMENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UCMR_STATEMENT_VALIDATION](UCMR_STATEMENT_VALIDATION.md) | `PREV_UCMR_STMT_VALIDATION_ID` |

