# CNT_RRF_AR_R

> RRF AR RELTN

**Description:** CNT RRF AR R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALPHA_RESPONSES_CATEGORY_ID` | DOUBLE | NOT NULL |  | foreign key to the category for this alpha_responses row. - ALPHA_RESPONSES_CATEGORY |
| 2 | `AR_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence in which alpha responses are stored and displayed. |
| 3 | `AR_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Alpha Response |
| 4 | `CNT_ALPHA_RESPONSE_KEY_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID (Value: 0.0) |
| 5 | `CNT_RRF_AR_R_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `CNT_RRF_KEY_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID (Value: 0.0) |
| 7 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | Used to indicate which alpha response should be used as the default in result entry applications. |
| 8 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | Used to store the long description of the response. |
| 9 | `MULTI_ALPHA_SORT_ORDER` | DOUBLE | NOT NULL |  | Defines the sort order of alpha responses that are used to result a task or assay with multiple valid alpha results. |
| 10 | `REFERENCE_IND` | DOUBLE | NOT NULL |  | Indicates if the alpha response selected will be printed on hard-copy charts as the typical "reference" value. |
| 11 | `RESULT_PROCESS_CD` | DOUBLE | NOT NULL |  | Used to store processing codes that would flag alpha responses as normal, abnormal, critical, and so on. |
| 12 | `RESULT_PROCESS_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 13 | `RESULT_VALUE` | DOUBLE |  |  | The value associated with the alpha response for a specific assay that would be used for appending additional information to the result. |
| 14 | `RRF_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Reference Range Factor |
| 15 | `TRUTH_STATE_CD` | DOUBLE | NOT NULL |  | this states whether to make the condition true or false based on the nomenclature concept. |
| 16 | `TRUTH_STATE_CDUID` | VARCHAR(100) |  |  | unique identifier fk to cnt_code_value_key |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `USE_UNITS_IND` | DOUBLE | NOT NULL |  | Used to indicate whether or not units of measure will be appended to the alpha response. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_ALPHA_RESPONSE_KEY_ID` | [CNT_ALPHA_RESPONSE_KEY](CNT_ALPHA_RESPONSE_KEY.md) | `CNT_ALPHA_RESPONSE_KEY_ID` |
| `CNT_RRF_KEY_ID` | [CNT_RRF_KEY](CNT_RRF_KEY.md) | `CNT_RRF_KEY_ID` |

