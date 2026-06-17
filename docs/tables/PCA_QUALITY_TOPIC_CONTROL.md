# PCA_QUALITY_TOPIC_CONTROL

> Contains data that controls the data population of Quality Topics.

**Description:** PowerChart Analytics Quality Topic Control  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXECUTION_CNT` | DOUBLE | NOT NULL |  | The number of times that the Quality Topic has been executed. |
| 2 | `HISTORICAL_ACTIVE_IND` | DOUBLE | NOT NULL |  | Indicates that historical extractions will be performed for this Quality Topic. |
| 3 | `HISTORICAL_QUAL_FROM_DT_TM` | DATETIME |  |  | The date/time which will be used as the lower limit during the qualification phase of a historical extraction. |
| 4 | `HISTORICAL_QUAL_TO_DT_TM` | DATETIME |  |  | The date/time which will be used as the upper limit during the qualification phase of a historical extraction. |
| 5 | `INCREMENTAL_ACTIVE_IND` | DOUBLE | NOT NULL |  | Indicates that incremental extractions will be performed for this Quality Topic. |
| 6 | `INCREMENTAL_QUAL_FROM_DT_TM` | DATETIME |  |  | The date/time which will be used as the lower limit during the qualification phase of the next incremental extraction. This is also the upper limit of the previous incremental extraction. |
| 7 | `PCA_QUALITY_TOPIC_CONTROL_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the PCA_QUALITY_TOPIC_CONTROL table. |
| 8 | `PCA_QUALITY_TOPIC_ID` | DOUBLE | NOT NULL | FK→ | The Quality Topic that is associated with this record. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PCA_QUALITY_TOPIC_ID` | [PCA_QUALITY_TOPIC](PCA_QUALITY_TOPIC.md) | `PCA_QUALITY_TOPIC_ID` |

