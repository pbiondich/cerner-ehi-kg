# NOMENCLATURE_LOAD_NS

> This table is just going to be a temporary table we use to store NON-SNOMED nomenclature data (temporarily) to support the load process.

**Description:** Nomenclature Load NS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Determines action to be taken on row 0 = Need to be processed 1 = Insert Needed 2 = Already Processed |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CMTI` | VARCHAR(250) | NOT NULL |  | the global unique identifier from an outside source |
| 5 | `CONCEPT_CKI` | VARCHAR(255) |  |  | cki from the concept table which is the functional concept. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `CONTRIBUTOR_SYSTEM_MEAN` | VARCHAR(12) |  |  | contributor system identifies the source feed of data from which a row was populated. this is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `DISALLOWED_IND` | DOUBLE |  |  | an indicator of whether the term is allowed for selection. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | Language Code from code set 36 |
| 11 | `LANGUAGE_MEAN` | VARCHAR(12) |  |  | the language that the string is expressed |
| 12 | `MNEMONIC` | VARCHAR(25) |  |  | Mnemonic for Source String |
| 13 | `PRIMARY_CTERM_IND` | DOUBLE |  |  | identifies the source string as the 'official', primary term. |
| 14 | `PRIMARY_VTERM_IND` | DOUBLE |  |  | identifies the source_string as the "official", or primary, term for the source_identifier. |
| 15 | `PRINCIPLE_TYPE_CD` | DOUBLE | NOT NULL |  | Principle Type Code from Code Set 401 |
| 16 | `PRINCIPLE_TYPE_MEAN` | VARCHAR(12) |  |  | a general category used to group strings. |
| 17 | `SHORT_STRING` | VARCHAR(60) |  |  | Short String representation of Source String |
| 18 | `SOURCE_IDENTIFIER` | VARCHAR(50) |  |  | the code, or key, from the source vocabulary that contributed the string to the nomenclature. |
| 19 | `SOURCE_STRING` | VARCHAR(255) |  |  | variable length string that may include alphanumeric characters and punctuation. |
| 20 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | Source Vocabulary Code from code set 400 |
| 21 | `SOURCE_VOCABULARY_MEAN` | VARCHAR(12) |  |  | the external vocabulary or lexicon that contributed the string, e.g. icd9, snomed, etc. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `VOCAB_AXIS_CD` | DOUBLE | NOT NULL |  | Vocabulary Axis Code from code set 15849 |
| 28 | `VOCAB_AXIS_MEAN` | VARCHAR(12) |  |  | vocabulary axis means related to snomed |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

