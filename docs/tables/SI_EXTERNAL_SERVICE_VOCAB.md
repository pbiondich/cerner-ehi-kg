# SI_EXTERNAL_SERVICE_VOCAB

> Contains the vocabularies supported by an external service, grouped by a content category (clinical concept).

**Description:** SI External Service Vocabulary  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTENT_CATEGORY_CD` | DOUBLE | NOT NULL |  | The content category (clinical concept) that the associated vocabulary should be used for |
| 2 | `SI_EXTERNAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Number that uniquely identifies a single row on the SI_EXTERNAL_SERVICE table. |
| 3 | `SI_EXTERNAL_SERVICE_VOCAB_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row in the table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VOCABULARY_CD` | DOUBLE | NOT NULL |  | One of the vocabularies that the service understands for the associated content category (clinical concept). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_EXTERNAL_SERVICE_ID` | [SI_EXTERNAL_SERVICE](SI_EXTERNAL_SERVICE.md) | `SI_EXTERNAL_SERVICE_ID` |

