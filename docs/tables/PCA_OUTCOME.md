# PCA_OUTCOME

> Defines Outcomes that may be related to Quality Measures. This table may serve as a dimension table for certain fact tables containing aggregations related to an Outcome.

**Description:** Power Chart Analytics Outcome  
**Table type:** REFERENCE  
**Primary key:** `PCA_OUTCOME_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTRAINDICATION_IND` | DOUBLE | NOT NULL |  | Indicates that this outcome represents a contraindication. This may be used in the denominator on performance calculations which allow contra-indicated records to be excluded from the general population. |
| 2 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | Comment which provides additional meaning or context to the Outcome. |
| 3 | `DISPLAY_TXT` | VARCHAR(60) |  |  | The textual displayed description for this Outcome. |
| 4 | `EXPECTATION_MET_IND` | DOUBLE | NOT NULL |  | Indicates that this outcome represents an expectation which has been met. This may be used in the numerator of performance calculations. |
| 5 | `OUTCOME_CD` | DOUBLE | NOT NULL |  | The CODE VALUE record which identifies the Outcome. |
| 6 | `PCA_OUTCOME_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the PCA_OUTCOME table. |
| 7 | `PCA_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | The source that supplied this Outcome. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PCA_SOURCE_ID` | [PCA_SOURCE](PCA_SOURCE.md) | `PCA_SOURCE_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PCA_ENCNTR_MEASURE_OUTCOME](PCA_ENCNTR_MEASURE_OUTCOME.md) | `PCA_OUTCOME_ID` |
| [PCA_MEASURE_OUTCOME_RELTN](PCA_MEASURE_OUTCOME_RELTN.md) | `PCA_OUTCOME_ID` |
| [PCA_PERSON_MEASURE_OUTCOME](PCA_PERSON_MEASURE_OUTCOME.md) | `PCA_OUTCOME_ID` |

