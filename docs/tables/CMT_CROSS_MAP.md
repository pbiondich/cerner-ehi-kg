# CMT_CROSS_MAP

> A crossmap links a single SNOMED CT concept to one or more concepts in target terminologies, such as ICD-9-CM, CPT-4 etc.

**Description:** CMT CROSS MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CMT_CROSS_MAP_ID` | DOUBLE | NOT NULL |  | cmt cross map identifierColumn |
| 7 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL | FK→ | Concept CKI is the functional Concept Identifier; it is the codified means within Millennium to identify key medical concepts to support information processing, clinical decision support, executable knowledge and knowledge presentation. Composed of a source and an identifier. For example, if the concept source is "SNOMED" and the concept identifier is "123", then the CKI is "SNOMED!123". |
| 8 | `CROSS_MAP_FLAG` | DOUBLE |  |  | Cross_map_FlagColumn |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `GROUP_SEQUENCE` | DOUBLE |  |  | Group SequenceColumn |
| 11 | `MAP_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The type of cross mapping to indicate whether the SNOMED to ICD-9-cm mapping relationship is one-to-one, or whether the SNOMED concept is more specific or general than the ICD-9-cm code. |
| 12 | `MAP_TYPE_FLAG` | DOUBLE |  |  | map type flagColumn |
| 13 | `SOURCE_IDENTIFIER` | VARCHAR(242) | NOT NULL |  | The code, or key, from source vocabulary that contributed the term to the nomenclature. |
| 14 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL | FK→ | The external vocabulary or lexicon that contributed the code. For example, ICD9, CPT4 etc. |
| 15 | `TARGET_CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Contains the target concept_cki to which the concept_cki is mapped. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONCEPT_CKI` | [CMT_CONCEPT](CMT_CONCEPT.md) | `CONCEPT_CKI` |
| `MAP_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SOURCE_VOCABULARY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

