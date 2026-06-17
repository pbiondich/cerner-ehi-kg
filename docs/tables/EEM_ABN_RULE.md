# EEM_ABN_RULE

> ABN Code Pair Table

**Description:** EEM ABN RULE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_RULE_ID` | DOUBLE | NOT NULL |  | The unique primary key of the table. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BEG_SEQ` | DOUBLE | NOT NULL |  | Denotes the first import sequence where the records became active. |
| 8 | `DIAG_BEG_IDENT` | VARCHAR(50) | NOT NULL |  | The ICD9 are stored using ranges SOURCE_IDENTIFIERs. This corresponds to the SOURCE_IDENTIFIER on the NOMENCLATURE table. |
| 9 | `DIAG_END_IDENT` | VARCHAR(50) | NOT NULL |  | The ICD9 are stored using ranges SOURCE_IDENTIFIERs. This corresponds to the SOURCE_IDENTIFIER on the NOMENCLATURE table. |
| 10 | `DIAG_VOCABULARY_CD` | DOUBLE | NOT NULL | FK→ | The external vocabulary or lexicon that contributed the string, e.g. ICD9, SNOMED, etc. |
| 11 | `EEM_FILE_ID` | DOUBLE | NOT NULL | FK→ | ID of the EEM Content File associated to the rule. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `END_SEQ` | DOUBLE | NOT NULL |  | Denotes that last import sequence that contained the record. |
| 14 | `KEY_FIELD` | DOUBLE | NOT NULL |  | Key Field |
| 15 | `PROC_IDENT` | VARCHAR(50) | NOT NULL |  | The CPT4 are stored using SOURCE_IDENTIFIERs. This corresponds to the SOURCE_IDENTIFIER on the NOMENCLATURE table. |
| 16 | `PROC_VOCABULARY_CD` | DOUBLE | NOT NULL | FK→ | The external vocabulary or lexicon that contributed the string, e.g. ICD9, SNOMED, etc. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DIAG_VOCABULARY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `EEM_FILE_ID` | [EEM_FILE](EEM_FILE.md) | `EEM_FILE_ID` |
| `PROC_VOCABULARY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

