# ALPHA_RESPONSES

> Used to store codified alpha responses for discrete task assays that are result type of alpha.

**Description:** Alpha Responses  
**Table type:** REFERENCE  
**Primary key:** `NOMENCLATURE_ID`, `REFERENCE_RANGE_FACTOR_ID`  
**Columns:** 24  
**Referenced by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALPHA_RESPONSES_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the category for this ALPHA_RESPONSES row. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | The nomenclature concept to which this alpha response is associated. |
| 8 | `DEFAULT_IND` | DOUBLE |  |  | Used to indicate which alpha response should be used as the default in result entry applications. |
| 9 | `DESCRIPTION` | VARCHAR(100) |  |  | Used to store the long description of the response. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `MULTI_ALPHA_SORT_ORDER` | DOUBLE |  |  | Defines the sort order of alpha responses that are used to result a task or assay with multiple valid alpha results. |
| 12 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | PK | Stores the identifier (from the nomenclature table) that stores the text for the alpha response. |
| 13 | `REFERENCE_IND` | DOUBLE |  |  | Indicates if the alpha response selected will be printed on hard-copy charts as the typical "reference" value. |
| 14 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | PK FK→ | Used to store the identifier for the row from the reference range factor table that is associated with the alpha response. |
| 15 | `RESULT_PROCESS_CD` | DOUBLE | NOT NULL |  | Used to store processing codes that would flag alpha responses as normal, abnormal, critical, and so on. |
| 16 | `RESULT_VALUE` | DOUBLE |  |  | The value associated with the alpha response for a specific assay that would be used for appending additional information to the result. |
| 17 | `SEQUENCE` | DOUBLE | NOT NULL |  | The sequence in which alpha responses are stored and displayed. |
| 18 | `TRUTH_STATE_CD` | DOUBLE | NOT NULL |  | This states whether to make the condition true of false based on the nomenclature concept. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 24 | `USE_UNITS_IND` | DOUBLE |  |  | Used to indicate whether or not units of measure will be appended to the alpha response. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALPHA_RESPONSES_CATEGORY_ID` | [ALPHA_RESPONSES_CATEGORY](ALPHA_RESPONSES_CATEGORY.md) | `ALPHA_RESPONSES_CATEGORY_ID` |
| `REFERENCE_RANGE_FACTOR_ID` | [REFERENCE_RANGE_FACTOR](REFERENCE_RANGE_FACTOR.md) | `REFERENCE_RANGE_FACTOR_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [ALPHA_RESPONSE_RULE](ALPHA_RESPONSE_RULE.md) | `NOMENCLATURE_ID` |
| [ALPHA_RESPONSE_RULE](ALPHA_RESPONSE_RULE.md) | `REFERENCE_RANGE_FACTOR_ID` |
| [CYTO_ALPHA_SECURITY](CYTO_ALPHA_SECURITY.md) | `NOMENCLATURE_ID` |
| [CYTO_ALPHA_SECURITY](CYTO_ALPHA_SECURITY.md) | `REFERENCE_RANGE_FACTOR_ID` |
| [CYTO_DIAG_DISCREPANCY](CYTO_DIAG_DISCREPANCY.md) | `NOMENCLATURE_X_ID` |
| [CYTO_DIAG_DISCREPANCY](CYTO_DIAG_DISCREPANCY.md) | `NOMENCLATURE_Y_ID` |
| [CYTO_DIAG_DISCREPANCY](CYTO_DIAG_DISCREPANCY.md) | `REFERENCE_RANGE_FACTOR_ID` |
| [CYTO_SCREENING_EVENT](CYTO_SCREENING_EVENT.md) | `NOMENCLATURE_ID` |
| [CYTO_SCREENING_EVENT](CYTO_SCREENING_EVENT.md) | `REFERENCE_RANGE_FACTOR_ID` |

