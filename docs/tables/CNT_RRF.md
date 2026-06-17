# CNT_RRF

> RRF

**Description:** CNT RRF  
**Table type:** REFERENCE  
**Primary key:** `CNT_RRF_ID`  
**Columns:** 43  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CNT_RRF_ID` | DOUBLE | NOT NULL | PK | Sequence generated ID |
| 3 | `CNT_RRF_KEY_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID (Value: 0.0) |
| 4 | `CODE_SET` | DOUBLE | NOT NULL |  | defines the code set used to validate reference ranges for assays with the result type of "online code set". |
| 5 | `CRITICAL_HIGH` | DOUBLE |  |  | Defines the critical high reference range. |
| 6 | `CRITICAL_IND` | DOUBLE | NOT NULL |  | indicates whether critical result reference ranges are defined. |
| 7 | `CRITICAL_LOW` | DOUBLE |  |  | Defines the critical low reference range. |
| 8 | `DEFAULT_RESULT` | DOUBLE |  |  | defines the default result value associated with specified reference range. |
| 9 | `DEF_RESULT_IND` | DOUBLE | NOT NULL |  | indicates whether the default result value has been defined for the reference range. |
| 10 | `DELTA_CHECK_TYPE_CD` | DOUBLE | NOT NULL |  | Code Set: 236 |
| 11 | `DELTA_CHECK_TYPE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 12 | `DELTA_CHK_FLAG` | DOUBLE | NOT NULL |  | 0.00 No delta checking 1.00 Perform standard delta checking 2.00 Perform advanced delta checking |
| 13 | `DELTA_MINUTES` | DOUBLE |  |  | defines the specific number of minutes used to calculate the delta checking algorithm. |
| 14 | `DELTA_VALUE` | DOUBLE |  |  | defines the value used to perform delta checking. |
| 15 | `DILUTE_IND` | DOUBLE | NOT NULL |  | indicates whether a dilution will be required for results that exceed the limits of the linear high range column. |
| 16 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value display that identifies the encounter type |
| 17 | `ENCNTR_TYPE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 18 | `FEASIBLE_HIGH` | DOUBLE |  |  | Defines the feasible high value for the defined reference range. Typically, this is the limit above which no result is possible. |
| 19 | `FEASIBLE_IND` | DOUBLE | NOT NULL |  | indicates whether feasible limits exist for the reference range |
| 20 | `FEASIBLE_LOW` | DOUBLE |  |  | Defines the feasible low value for the reference range. Typically, this is the limit below which no result is possible. |
| 21 | `GESTATIONAL_IND` | DOUBLE | NOT NULL |  | Indicates whether the reference range defined is for the gestational age. |
| 22 | `LINEAR_HIGH` | DOUBLE |  |  | Defines the linear high limit for the reference range. Result values above this limit are considered out of the linear high limits of the service resource specified. |
| 23 | `LINEAR_IND` | DOUBLE | NOT NULL |  | indicates whether linear limits exist for the reference range. |
| 24 | `LINEAR_LOW` | DOUBLE |  |  | Defines the linear low limit for the reference range. Result values below this limit are considered out of the linear low limits of the service resource specified. |
| 25 | `MINS_BACK` | DOUBLE |  |  | Used to calculate the minutes back from the previous result to default the value for the current result for CareNet applications. |
| 26 | `NORMAL_HIGH` | DOUBLE |  |  | Defines the normal high reference range value for a specific discrete task assay. |
| 27 | `NORMAL_IND` | DOUBLE | NOT NULL |  | indicates whether normal ranges are built for the reference range specified. |
| 28 | `NORMAL_LOW` | DOUBLE |  |  | Defines the normal low reference range value for a specific discrete task assay. |
| 29 | `REVIEW_HIGH` | DOUBLE |  |  | defines the review high reference range limit for a discrete task assay. |
| 30 | `REVIEW_IND` | DOUBLE | NOT NULL |  | indicates whether review range values are defined for the reference range. |
| 31 | `REVIEW_LOW` | DOUBLE |  |  | defines the value for the review low reference range. |
| 32 | `RRF_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Reference Range Factor. |
| 33 | `SENSITIVE_HIGH` | DOUBLE |  |  | Defines the value for the sensitive high reference range. |
| 34 | `SENSITIVE_IND` | DOUBLE | NOT NULL |  | indicates whether sensitive range values are defined for the reference range. |
| 35 | `SENSITIVE_LOW` | DOUBLE |  |  | Defines the sensitive low value for the reference range. |
| 36 | `UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value display that identifies the specific units of measure to be appended to results for the defined reference range |
| 37 | `UNITS_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 38 | `UNITS_CKI` | VARCHAR(50) | NOT NULL |  | UNITS CKI |
| 39 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 40 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 41 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 42 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 43 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_RRF_KEY_ID` | [CNT_RRF_KEY](CNT_RRF_KEY.md) | `CNT_RRF_KEY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CNT_DTA_RRF_R](CNT_DTA_RRF_R.md) | `CNT_RRF_ID` |

