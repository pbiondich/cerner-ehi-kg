# PCA_ENCNTR_TOPIC_RELTN

> Contains a snapshot which provides information about encounters being tracked as part of a Quality Topic.

**Description:** Power Chart Analytics Encounter Topic Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter being tracked as part of a Quality Topic. |
| 2 | `PCA_ENCNTR_TOPIC_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the PCA_ENCNTR_TOPIC_RELTN table. |
| 3 | `PCA_QUALITY_TOPIC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the Quality Topic associated with the encounter. |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person associated to the encounter being tracked as part of a Quality Topic. |
| 5 | `PUBLISH_IND` | DOUBLE | NOT NULL |  | States whether the item in this record is viewable via "normal" applications (E.g. on-line inquiries, etc.). Audit and/or administrative applications would be able to view non-publishable results. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PCA_QUALITY_TOPIC_ID` | [PCA_QUALITY_TOPIC](PCA_QUALITY_TOPIC.md) | `PCA_QUALITY_TOPIC_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

