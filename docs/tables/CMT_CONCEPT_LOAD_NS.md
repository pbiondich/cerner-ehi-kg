# CMT_CONCEPT_LOAD_NS

> CMT Concept Load (Non-SNOMED)

**Description:** CMT_CONCEPT_LOAD_NS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | concept cki is the functional concept identifier; it is the codified means within millennium to identify key medical concepts to support information processing, clinical decision support, executable knowledge and knowledge presentation. |
| 4 | `CONCEPT_IDENTIFIER` | VARCHAR(242) |  |  | The unique identifier supplied from other external database (e.g. SNOMED) or Cerner and is persistent once it is assigned to a concept. If the concept is from SNOMED, concept identifier is the unique SNOMED Clinical Term identifier provided by CAP. |
| 5 | `CONCEPT_NAME` | VARCHAR(2000) |  |  | A phrase that describes a concept in a way that it is intended to be unambiguous. It is the same as "Fully Specified Name" in SNOMED CT. It explains the meaning of the concept more fully than preferred term. |
| 6 | `CONCEPT_SOURCE_MEAN` | VARCHAR(12) |  |  | Represents the source that owns the concept identifier. |
| 7 | `DISALLOWED_IND` | DOUBLE |  |  | An indication of whether the term is allowed for selection or not. 0 - allowed 1 - disallowed |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

