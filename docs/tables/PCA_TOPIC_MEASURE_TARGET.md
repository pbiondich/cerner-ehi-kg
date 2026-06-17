# PCA_TOPIC_MEASURE_TARGET

> Contains the values that will be used to measure adherence to Quality Topics and Quality Measures.

**Description:** PowerChart Analytics Topic Measure Target  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PCA_TOPIC_MEASURE_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The quality topic and quality measure associated with this target. |
| 2 | `PCA_TOPIC_MEASURE_TARGET_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the PCA_TOPIC_MEASURE_TARGET table. |
| 3 | `TARGET_PCT` | DOUBLE | NOT NULL |  | The actual target value, expressed as an integer value. |
| 4 | `TARGET_TYPE_CD` | DOUBLE | NOT NULL |  | The type of target represented by the record. For example, a standard target vs. a client-defined target. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PCA_TOPIC_MEASURE_RELTN_ID` | [PCA_TOPIC_MEASURE_RELTN](PCA_TOPIC_MEASURE_RELTN.md) | `PCA_TOPIC_MEASURE_RELTN_ID` |

