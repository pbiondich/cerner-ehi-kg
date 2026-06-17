# UCMR_WS_STMT_VALIDATION

> Stores relationships between whorksheet statements and validation information. Includes numeric range validation.

**Description:** Unified Case Management Reference - Statement Validation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `UCMR_WORKSHEET_STATEMENT_R_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the associated worksheet statement to be validated. |
| 6 | `UCMR_WS_STMT_VALIDATION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a validation entry for a given worksheet statement relationship. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VALIDATION_CD` | DOUBLE | NOT NULL |  | A code value from any code set that is checked at activity time to determine if a valid selection from a code list was made. |
| 13 | `VALIDATION_NBR` | DOUBLE | NOT NULL |  | The number used for comparison with the statement accept value on the activity side to determine if the input is valid. |
| 14 | `VALIDATION_TEXT` | VARCHAR(250) |  |  | Stores textual validation information for a worksheet statement (e.g., ensuring current date entered). |
| 15 | `VALIDATION_TYPE_CD` | DOUBLE | NOT NULL |  | Used to store the internal code for the type of validation (e.g., minimum, maximum, etc.) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_WORKSHEET_STATEMENT_R_ID` | [UCMR_WORKSHEET_STATEMENT_R](UCMR_WORKSHEET_STATEMENT_R.md) | `UCMR_WORKSHEET_STATEMENT_R_ID` |

