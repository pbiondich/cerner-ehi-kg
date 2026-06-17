# PCA_QUALITY_TOPIC

> Contains the high-level topics that require measurements to be taken to indicate performance level. This table may serve as a dimension table for certain fact tables containing aggregations related to this Quality Topic.

**Description:** Power Chart Analytics Quality Topic  
**Table type:** REFERENCE  
**Primary key:** `PCA_QUALITY_TOPIC_ID`  
**Columns:** 16  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALC_SCRIPT_NAME` | VARCHAR(40) |  |  | The Discern Explorer program object which does the processing on the data that was qualified for this Quality Topic. |
| 2 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | Comment which provides additional meaning or context to the Topic. |
| 3 | `DISPLAY_TXT` | VARCHAR(60) | NOT NULL |  | The textual displayed description for this Quality Topic. |
| 4 | `MEASUREMENT_PERIOD_NBR` | DOUBLE | NOT NULL |  | The length of the defined measurement period for this quality topic. Used in conjunction with MEASUREMENT_PERIOD_UNIT_CD. |
| 5 | `MEASUREMENT_PERIOD_UNIT_CD` | DOUBLE | NOT NULL |  | The time period for which this Quality Topic is being measured. E.G. 'day' or 'month'. Used in conjunction with MEASUREMENT_PERIOD_NBR. |
| 6 | `PCA_QUALITY_TOPIC_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the PCA_QUALITY_TOPIC table. |
| 7 | `PCA_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | The source that supplied this Quality Topic. |
| 8 | `PREP_SCRIPT_NAME` | VARCHAR(40) |  |  | The Discern Explorer program which is used to prepare the associated activity tables for data associated with this quality topic. |
| 9 | `QUAL_SCRIPT_NAME` | VARCHAR(40) |  |  | The Discern Explorer program object which is used to determine which data needs to be processed for this quality topic. |
| 10 | `TOPIC_CD` | DOUBLE | NOT NULL |  | The CODE VALUE record which identifies the Quality Topic. Populated on shipped rows only. |
| 11 | `TOPIC_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of topic that is being measured. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PCA_SOURCE_ID` | [PCA_SOURCE](PCA_SOURCE.md) | `PCA_SOURCE_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [PCA_ENCNTR_TOPIC_RELTN](PCA_ENCNTR_TOPIC_RELTN.md) | `PCA_QUALITY_TOPIC_ID` |
| [PCA_PERSON_TOPIC_RELTN](PCA_PERSON_TOPIC_RELTN.md) | `PCA_QUALITY_TOPIC_ID` |
| [PCA_QUALITY_TOPIC_CONTROL](PCA_QUALITY_TOPIC_CONTROL.md) | `PCA_QUALITY_TOPIC_ID` |
| [PCA_TOPIC_MEASURE_RELTN](PCA_TOPIC_MEASURE_RELTN.md) | `PCA_QUALITY_TOPIC_ID` |

