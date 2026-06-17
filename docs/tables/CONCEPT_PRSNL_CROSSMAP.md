# CONCEPT_PRSNL_CROSSMAP

> Table used to store concept mappings established by end users.

**Description:** Concept personnel crossmap  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONCEPT_PRSNL_CROSSMAP_ID` | DOUBLE | NOT NULL |  | Unique identifier for table row. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `MAP_SCOPE_MEAN` | VARCHAR(12) |  |  | Map scope identifier used to determine the scope of the mapping's applicability (all patients, this patient, etc.) |
| 6 | `MAP_TYPE_MEAN` | VARCHAR(12) |  |  | Map type identifier used to distinguish between specific entities that were crossmapped (problem to diagnosis, diagnosis to problem, etc.) |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person Patient ID |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the user who established the concept mapping. |
| 9 | `SOURCE_CONCEPT_CKI` | VARCHAR(255) |  |  | Concept identifier for the source concept. |
| 10 | `SOURCE_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature identifier for the source nomenclature. |
| 11 | `SOURCE_VOCAB_CD` | DOUBLE | NOT NULL |  | Vocabulary code identifier for the source concept |
| 12 | `TARGET_CONCEPT_CKI` | VARCHAR(255) |  |  | Concept identifier for the target concept. |
| 13 | `TARGET_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature identifier for the target nomenclature. |
| 14 | `TARGET_VOCAB_CD` | DOUBLE | NOT NULL |  | Vocabulary code identifier for the target concept |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SOURCE_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `TARGET_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

