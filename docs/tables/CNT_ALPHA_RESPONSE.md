# CNT_ALPHA_RESPONSE

> Used to store codified alpha responses for discrete task assays that are result type of alpha.

**Description:** CNT ALPHA RESPONSE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AR_INTERNAL_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for INTERNALAlpha Response |
| 3 | `AR_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Alpha Response |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `CMTI` | VARCHAR(100) | NOT NULL |  | The unique term identifier - from Nomenclature CMTI |
| 6 | `CNT_ALPHA_RESPONSE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `CNT_ALPHA_RESPONSE_KEY_ID` | DOUBLE | NOT NULL | FK→ | FOREIGN KEY FROM CNT_ALPHA_RESPONSE_KEY |
| 8 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | The Concept CKI associated to the term |
| 9 | `CONCEPT_IDENTIFIER` | VARCHAR(242) | NOT NULL |  | a unique identifier supplied from Cerner or other external database and is persistent once it is assigned to a concept. all Cerner assigned concept identifiers are created from the concept_seq. the sequence number is formatted to an 8-byte number padded |
| 10 | `CONCEPT_SOURCE_CD` | DOUBLE | NOT NULL |  | represents the external source that owns the concept_identifier. |
| 11 | `CONCEPT_SOURCE_CDUID` | VARCHAR(100) |  |  | unique identifier fk to cnt_code_value_key |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `CONTRIBUTOR_SYSTEM_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier UID from CNT_CODE_VALUE_KEY |
| 14 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 15 | `DATA_STATUS_CDUID` | VARCHAR(100) |  |  | unique identifier fk to cnt_code_value_key |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | the language that the string is expressed. |
| 18 | `LANGUAGE_CDUID` | VARCHAR(100) |  |  | unique identifier fk to cnt_code_value_key |
| 19 | `MNEMONIC` | VARCHAR(25) |  |  | A terse description of the source string. |
| 20 | `PRIMARY_CTERM_IND` | DOUBLE | NOT NULL |  | This indicator identifies which string is the official client term for a source identifier within a source vocabulary. |
| 21 | `PRIMARY_VTERM_IND` | DOUBLE | NOT NULL |  | This indicator identifies which string is the official term for a source identifier within a source vocabulary. |
| 22 | `SHORT_STRING` | VARCHAR(60) |  |  | Variable length string that may include alphanumeric characters and punctuation. |
| 23 | `STRING_IDENTIFIER` | VARCHAR(18) | NOT NULL |  | a unique identifier supplied from Cerner or other external database and is persistent once it is assigned to a string. |
| 24 | `STRING_SOURCE_CD` | DOUBLE | NOT NULL |  | represents the external source that owns the string_identifier. |
| 25 | `STRING_SOURCE_CDUID` | VARCHAR(100) |  |  | unique identifier fk to cnt_code_value_key |
| 26 | `STRING_STATUS_CD` | DOUBLE | NOT NULL |  | an indication of whether the string is the preferred form of a term or a variant of that form, e.g. by case, plurality, word order. |
| 27 | `STRING_STATUS_CDUID` | VARCHAR(100) |  |  | unique identifier fk to cnt_code_value_key |
| 28 | `TERM_SOURCE_CD` | DOUBLE | NOT NULL |  | represents the external source that owns the term_identifier. |
| 29 | `TERM_SOURCE_CDUID` | VARCHAR(100) |  |  | unique identifier fk to cnt_code_value_key |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 35 | `VOCAB_AXIS_CD` | DOUBLE | NOT NULL |  | The vocabulary axis for the given code - code set 15849 |
| 36 | `VOCAB_AXIS_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_ALPHA_RESPONSE_KEY_ID` | [CNT_ALPHA_RESPONSE_KEY](CNT_ALPHA_RESPONSE_KEY.md) | `CNT_ALPHA_RESPONSE_KEY_ID` |

