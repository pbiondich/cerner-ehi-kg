# PCA_TOPIC_MEASURE_RELTN

> Defines the measures that pertain to a given topic.

**Description:** Power Chart Analytics Topic Measure Relation  
**Table type:** REFERENCE  
**Primary key:** `PCA_TOPIC_MEASURE_RELTN_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `PCA_QUALITY_MEASURE_ID` | DOUBLE | NOT NULL | FK→ | The measurement that pertains to this topic. |
| 3 | `PCA_QUALITY_TOPIC_ID` | DOUBLE | NOT NULL | FK→ | The Quality Topic that this Measure pertains to. |
| 4 | `PCA_TOPIC_MEASURE_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the PCA_TOPIC_MEASURE_RELTN table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PCA_QUALITY_MEASURE_ID` | [PCA_QUALITY_MEASURE](PCA_QUALITY_MEASURE.md) | `PCA_QUALITY_MEASURE_ID` |
| `PCA_QUALITY_TOPIC_ID` | [PCA_QUALITY_TOPIC](PCA_QUALITY_TOPIC.md) | `PCA_QUALITY_TOPIC_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PCA_TOPIC_MEASURE_TARGET](PCA_TOPIC_MEASURE_TARGET.md) | `PCA_TOPIC_MEASURE_RELTN_ID` |

