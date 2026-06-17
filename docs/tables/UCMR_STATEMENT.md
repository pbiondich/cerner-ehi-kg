# UCMR_STATEMENT

> This table stores specific information about a protocol statement.

**Description:** Unified Case Management Reference Statement  
**Table type:** REFERENCE  
**Primary key:** `UCMR_STATEMENT_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_TYPE_CD` | DOUBLE | NOT NULL |  | This field indicates the type of data accepted. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ALLOW_MULTIPLE_IND` | DOUBLE | NOT NULL |  | When True, the statement can be added multiple times to Process or Output areas, but cannot be added to Input. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CODE_SET` | DOUBLE | NOT NULL |  | When the accept type is coded list, this number will indicate which code set should appear in list at activity time. |
| 7 | `DEFAULT_LABEL_TEXT` | VARCHAR(250) |  |  | Stores the statement default label text. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `MAX_DIGITS_NBR` | DOUBLE | NOT NULL |  | This field defines the maximum number of digits allowed in the numeric accept. |
| 10 | `MIN_DECIMAL_PLACES_NBR` | DOUBLE | NOT NULL |  | This field defines the minimum number of decimal places required in the numeric accept. |
| 11 | `MIN_DIGITS_NBR` | DOUBLE | NOT NULL |  | This field defines the minimum number of digits required in the numeric accept. |
| 12 | `PREV_UCMR_STATEMENT_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the statement information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 13 | `SCI_NOTATION_IND` | DOUBLE | NOT NULL |  | This field indicates whether the statement allows numeric values in scientific notation. If set, any value that exceeds the maximum digits and decimal places data map settings will be formatted in scientific notation (e.g. MaxDigits = 5, Decimal Places = 2, Value = 1000.00 then the FormattedValue = 1.00e3). Otherwise, the value will be formatted using the data map settings. |
| 14 | `STATEMENT_NAME_CD` | DOUBLE | NOT NULL |  | The code value associated to the statement name. |
| 15 | `UCMR_STATEMENT_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies a row in the UCMR_STATEMENT table. |
| 16 | `UNITS_CD` | DOUBLE | NOT NULL |  | This field contains a unique code value that identifies the unites of measure for interpreting the result value. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `XML_FORMATTING_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains statement formatting information in an xml blob. This information may include whether accept appears before statement text or any other information pertaining the statement within a worksheet. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_UCMR_STATEMENT_ID` | [UCMR_STATEMENT](UCMR_STATEMENT.md) | `UCMR_STATEMENT_ID` |
| `XML_FORMATTING_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [UCMR_STATEMENT](UCMR_STATEMENT.md) | `PREV_UCMR_STATEMENT_ID` |
| [UCMR_STATEMENT_VALIDATION](UCMR_STATEMENT_VALIDATION.md) | `UCMR_STATEMENT_ID` |

