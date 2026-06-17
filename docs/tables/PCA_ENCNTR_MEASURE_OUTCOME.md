# PCA_ENCNTR_MEASURE_OUTCOME

> Contains a snapshot which provides information about encounters being tracked as part of a Quality Topic, specifically the outcomes for various measures associated with the topic.

**Description:** Power Chart Analytics Encounter Measure Outcome  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter being tracked as part of a Quality Topic. |
| 2 | `MEASURE_PROCESS_FLAG` | DOUBLE | NOT NULL |  | Indicates that this record needs some type of processing to fill it's PCA_OUTCOME_ID field.0 |
| 3 | `PCA_ENCNTR_MEASURE_OUTCOME_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the PCA_ENCNTR_MEASURE_OUTCOME table. |
| 4 | `PCA_OUTCOME_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the Quality Measure's Outcome. |
| 5 | `PCA_QUALITY_MEASURE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the Quality Measure being tracked as part of the Quality Topic. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the encounter that is being tracked as part of a Quality Topic. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PCA_OUTCOME_ID` | [PCA_OUTCOME](PCA_OUTCOME.md) | `PCA_OUTCOME_ID` |
| `PCA_QUALITY_MEASURE_ID` | [PCA_QUALITY_MEASURE](PCA_QUALITY_MEASURE.md) | `PCA_QUALITY_MEASURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

