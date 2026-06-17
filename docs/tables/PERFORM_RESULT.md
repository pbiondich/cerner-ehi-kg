# PERFORM_RESULT

> Stores result values and corresponding information relating to the result. If a result is performed multiple times a new entry into the table is added.

**Description:** Perform Result  
**Table type:** ACTIVITY  
**Primary key:** `PERFORM_RESULT_ID`  
**Columns:** 56  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE |  |  | Defines the sequence to use when selecting a row from the result comment table. (Currently not implemented) |
| 2 | `ADVANCED_DELTA_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific advanced delta check reference rule that was used to evaluate a result that failed delta checking. Creates a relationship to the advanced delta table. |
| 3 | `APP_MODE_IND` | DOUBLE |  |  | This indicator is used to show what application/application mode this result came from. The possible values are: 1 = AccessionResultEntry Accession Mode 2 = AccessionResultEntry Worklist Mode 3 = AccessionResultEntry Instrument Queue Mode 4 = AccessionResultEntry Correction Mode 5 = AccessionResultEntry Differential Mode 6 = BatchResultEntry Mode 7 = Multiple Accession Result Verification Mode If the value is + 100, it means that synchronous posting to clinical events was used. |
| 4 | `ASCII_TEXT` | VARCHAR(60) |  |  | If the procedure is defined as free-text, the result value is stored. If the procedure is defined as text or interpretation, the first 60 characters of the text without RTF attributes is stored. |
| 5 | `AV_ERROR_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific autoverification error code if the autoverification server is not able to autoverify a result. |
| 6 | `CONTAINER_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific container holding the specimen on which the procedure was performed to produce the result. Creates a relationship to the container table. |
| 7 | `CRITICAL_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies whether a result has passed or failed critical result reference range. |
| 8 | `DELTA_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies whether the result value has passed or failed a delta check. |
| 9 | `DELTA_PERF_RESULT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific perform result ID of the previous result used in delta checking. |
| 10 | `DILUTION_FACTOR` | DOUBLE |  |  | Defines the dilution factor to be considered when reviewing a result when the specimen has been diluted for testing. |
| 11 | `EQUATION_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific equation used to create the result value. This field is valid for discrete task assays that are defined as the calculation result type. Creates a relationship to the equation table. |
| 12 | `FEASIBLE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies whether a result has passed or failed feasible result reference range. |
| 13 | `IDENTIFIER` | VARCHAR(20) |  |  | If the result was posted using an identifier from a worklist, the identifier used will be recorded here. (Currently not implemented) |
| 14 | `INTERFACE_FLAG` | DOUBLE |  |  | Defines how the result was entered into the table. |
| 15 | `INTERFACE_STATUS_FLAG` | DOUBLE | NOT NULL |  | Will Indicate the result status coming from an instrument.0 - Default, No messages from interface.1 - Modified on Instrument by Operator2 - In result group with an assay that was modified on an instrument |
| 16 | `INTERP_DATA_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies when specific interpretive data is associated with the discrete task assay. Creates a relationship to the interpretive data table. |
| 17 | `INTERP_OVERRIDE_IND` | DOUBLE |  |  | Indicates whether an interpretation has been overridden and an alpha response entered. A value of 1 indicates when an interpretation has been overridden. A value of 0 indicates when the interpretation has not been overridden. |
| 18 | `LESS_GREAT_FLAG` | DOUBLE |  |  | Defines whether or not the result value should be viewed qualitatively with a < or > sign. |
| 19 | `LINEAR_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies whether a result has passed or failed a linear result reference range. |
| 20 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the specific text associated with a textual or interpretation result. Creates a relationship to the long text table. |
| 21 | `MULTIPLEX_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific multiplexor that the instrument was running when the interface sent the result across. |
| 22 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific nomenclature selection for an alpha response. Creates a relationship to the nomenclature table. |
| 23 | `NORMAL_ALPHA` | VARCHAR(2000) |  |  | Defines the normal alpha response for a procedure with the result type of alpha. |
| 24 | `NORMAL_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the normal reference range associated with the result value, such as normal, low, or high. |
| 25 | `NORMAL_HIGH` | DOUBLE |  |  | Defines the normal high reference range value associated with a result. The result must be greater than the normal high to be flagged as high. |
| 26 | `NORMAL_LOW` | DOUBLE |  |  | Defines the normal low reference range value associated with a result. The result must be less than the normal low to be flagged as low. |
| 27 | `NOTIFY_CD` | DOUBLE | NOT NULL |  | Indicates the notify flag is applied to this result value. |
| 28 | `NUMERIC_RAW_VALUE` | DOUBLE |  |  | Stores the numeric result value as transmitted from the instrument or entered by the result entry application before any rounding has been appiled. |
| 29 | `PARENT_PERFORM_RESULT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the previous performed result value when a discrete task assay result is changed. Creates a relationship to an associated row on the perform result table. |
| 30 | `PERFORM_DT_TM` | DATETIME |  |  | Defines the date and time the result was performed. |
| 31 | `PERFORM_PERSONNEL_ID` | DOUBLE | NOT NULL |  | Defines the person who performed the result for a procedure. |
| 32 | `PERFORM_RESULT_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific perform result value. |
| 33 | `PERFORM_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 34 | `POST_ALPHA_IND` | DOUBLE |  |  | Indicates whether a result was posted as an alpha from an instrument, but changed to the numeric linear value. A value of 1 indicates the result was posted as an alpha from an instrument. A value of 0 indicates the result was posted as received from the instrument. (Currently not implemented) |
| 35 | `QC_OVERRIDE_CD` | DOUBLE |  |  | A code value that identifies if the user has chosen to override the quality control validation when posting this result to the system. |
| 36 | `RAW_RESULT_STR` | VARCHAR(255) |  |  | Contains the result exactly as it was sent from the instrument. For alphas, it is what was used to match the mnemonic on nomenclature. For numerics, it is what was posted as the numeric value. For free textit is what was sent and could not be matched to an alpha response. |
| 37 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific reference range applied to the result. Creates a relationship to the reference range factor table. |
| 38 | `REPEAT_NBR` | DOUBLE | NOT NULL |  | Defines the sequence number of a repeated result value. A value of zero represents the original performed result, one is the first repeat, etc. |
| 39 | `RESOURCE_ERROR_CODES` | VARCHAR(255) |  |  | Stores the error codes that have been sent by an automated instrument while processing a result. |
| 40 | `RESULT_CODE_SET_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific code value result type for a discrete task assay that is to be resulted as a code value. The code set can be any code set and is not tied specifically to one code set. |
| 41 | `RESULT_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific discrete task assay result. Creates a relationship to the result table. |
| 42 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific status of the result, such as performed, verified, corrected, and so on. |
| 43 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the result type of the result value. |
| 44 | `RESULT_VALUE_ALPHA` | VARCHAR(200) |  |  | Stores the alpha response text of an alpha procedure. |
| 45 | `RESULT_VALUE_DT_TM` | DATETIME |  |  | Stores the date and time for a procedure defined as date. |
| 46 | `RESULT_VALUE_NUMERIC` | DOUBLE |  |  | Stores the numeric result value as rounded for formatting and display. |
| 47 | `REVIEW_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies whether or not a result has passed or failed the review result reference range. Denotes that a result has been flagged for review. |
| 48 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific service resource (such as instrument, bench, or sub section) where the procedure was performed. |
| 49 | `UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the units of measure for interpreting the result value. |
| 50 | `UNPERF_FLAG` | DOUBLE |  |  | Defines how the result is unperformed. (Currently not implemented) |
| 51 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 55 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 56 | `WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | Identifies the automatic worklist associated with the result. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADVANCED_DELTA_ID` | [ADVANCED_DELTA](ADVANCED_DELTA.md) | `ADVANCED_DELTA_ID` |
| `EQUATION_ID` | [EQUATION](EQUATION.md) | `EQUATION_ID` |
| `INTERP_DATA_ID` | [INTERP_DATA](INTERP_DATA.md) | `INTERP_DATA_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `REFERENCE_RANGE_FACTOR_ID` | [REFERENCE_RANGE_FACTOR](REFERENCE_RANGE_FACTOR.md) | `REFERENCE_RANGE_FACTOR_ID` |
| `RESULT_ID` | [RESULT](RESULT.md) | `RESULT_ID` |
| `WORKLIST_ID` | [WORKLIST](WORKLIST.md) | `WORKLIST_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_EXCEPTION](BB_EXCEPTION.md) | `PERFORM_RESULT_ID` |

