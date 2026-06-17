# PCA_PERSON_TOPIC_RELTN

> Contains a snapshot which provides information about persons being tracked as part of a quality Topic.

**Description:** PowerChart Analytics Person Topic Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `PCA_PERSON_TOPIC_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the PCA_PERSON_TOPIC_RELTN table. |
| 6 | `PCA_QUALITY_TOPIC_ID` | DOUBLE | NOT NULL | FK→ | The Quality Topic that is associated with this person. |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the person being tracked as part of this Quality Topic. |
| 8 | `PUBLISH_IND` | DOUBLE | NOT NULL |  | States whether the item in this record is viewable via "normal" applications. (e.g. on-line inquiries, etc.) Audit and/or administrative applications would be able to view non-publishable results. 1 means that all data has been processed and is available for viewing. |
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
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

