# PCA_QUALITY_MEASURE

> Details the procedures that have been determined as measurements of some Topic. This table may serve as a dimension table for certain fact tables containing aggregations related to this Quality Measure.

**Description:** Power Chart Analytics Quality Measure  
**Table type:** REFERENCE  
**Primary key:** `PCA_QUALITY_MEASURE_ID`  
**Columns:** 14  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALC_SCRIPT_NAME` | VARCHAR(40) |  |  | The Discern Explorer program object which does the processing on the data that was qualified for this Quality Measure. |
| 2 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | Comment which provides additional meaning or context to the Quality Measure. |
| 3 | `DISPLAY_TXT` | VARCHAR(60) | NOT NULL |  | The textual displayed description for this Quality Measure. |
| 4 | `MEASURE_CD` | DOUBLE | NOT NULL |  | The CODE VALUE record which identifies the Quality Measure. |
| 5 | `MEASURE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of measure being created. 0 = Person Measure, 1 = Visit measure |
| 6 | `PCA_QUALITY_MEASURE_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the PCA_QUALITY_MEASURE table. |
| 7 | `PCA_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | The source that supplied this Quality Measure. |
| 8 | `PREP_SCRIPT_NAME` | VARCHAR(40) |  |  | The Discern Explorer program which is used to prepare the associated activity tables for data associated with this quality measure. |
| 9 | `QUAL_SCRIPT_NAME` | VARCHAR(40) |  |  | The Discern Explorer program object which is used to determine which data needs to be processed for this quality measure. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PCA_SOURCE_ID` | [PCA_SOURCE](PCA_SOURCE.md) | `PCA_SOURCE_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [BR_ELIG_PROV_MEAS_RELTN](BR_ELIG_PROV_MEAS_RELTN.md) | `PCA_QUALITY_MEASURE_ID` |
| [PCA_ENCNTR_MEASURE_OUTCOME](PCA_ENCNTR_MEASURE_OUTCOME.md) | `PCA_QUALITY_MEASURE_ID` |
| [PCA_MEASURE_OUTCOME_RELTN](PCA_MEASURE_OUTCOME_RELTN.md) | `PCA_QUALITY_MEASURE_ID` |
| [PCA_PERSON_MEASURE_OUTCOME](PCA_PERSON_MEASURE_OUTCOME.md) | `PCA_QUALITY_MEASURE_ID` |
| [PCA_TOPIC_MEASURE_RELTN](PCA_TOPIC_MEASURE_RELTN.md) | `PCA_QUALITY_MEASURE_ID` |

