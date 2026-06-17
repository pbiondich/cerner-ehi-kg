# CONCEPT_PROPERTY

> Concept Property

**Description:** Stores the HNAM properties associated with a concept.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CKI` | VARCHAR(255) | NOT NULL |  | The CKI that the properties belong. |
| 4 | `CONCEPT_PROPERTY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row in the table. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Long blob idColumn |
| 7 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The id of the xml string that contains the concept property data in the long_text_reference table. |
| 8 | `SEMANTIC_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The semanitc type associated with the concept. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `SEMANTIC_TYPE_ID` | [SEMANTIC_TYPE](SEMANTIC_TYPE.md) | `SEMANTIC_TYPE_ID` |

