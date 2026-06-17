# PERSON_MATCHES

> The person matches table contains proposed or suggested person matches based on search criteria used to help determine if a person has been entered into the system more than once. It is used as a work queue for performing person data reconciliation.

**Description:** Person Matches  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_MATCHES_ID`  
**Columns:** 49  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `A_ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `A_ALIAS` | VARCHAR(200) |  |  | The alias is an identifier (I.e., SSN, medical record number, etc.) for a person. The alias may be unique or non-unique depending on the type of alias. |
| 7 | `A_ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias pool code identifies a unique set or list of person identifiers (I.e., numbers). The alias pool code also determines the accept/display format for the unique set of identifiers. |
| 8 | `A_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Person alias type code identifies a kind or type of alias (i.e., SSN, MRN, Financial Number, Community MRN, etc.). They have Cerner pre-defined meanings in the common data foundation table allowing HNA applications to look for a specific kind of alias. |
| 9 | `A_BIRTH_DT_CD` | DOUBLE | NOT NULL |  | Birth date code indicates the kind of birth date and time value that is contained in the birth_dt_tm field. (i.e., estimated, still born, unknown, etc.) |
| 10 | `A_BIRTH_DT_TM` | DATETIME |  |  | The date and time of birth for the person. |
| 11 | `A_BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 12 | `A_CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | This is the person responsible for creating a row in the person table. |
| 13 | `A_NAME_FIRST_KEY` | VARCHAR(100) |  |  | This is the person's first given name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 14 | `A_NAME_LAST_KEY` | VARCHAR(100) |  |  | This is the person's family name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 15 | `A_NAME_MIDDLE` | VARCHAR(100) |  |  | This is the person's middle or secondary given name or names. |
| 16 | `A_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 17 | `A_PHONETIC` | CHAR(8) |  |  | This is the Soundex coded representation of the person's name. This field is used for indexing and searching for a patient by name when the exact spelling is not known. |
| 18 | `A_SEX_CD` | DOUBLE | NOT NULL |  | The gender of the patient (i.e., male, female, unknown). |
| 19 | `A_SSN_ALIAS` | VARCHAR(200) |  |  | The Social Security Number (SSN) alias for the person. |
| 20 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 21 | `B_ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 22 | `B_ALIAS` | VARCHAR(200) |  |  | The alias is an identifier (I.e., SSN, medical record number, etc.) for a person. The alias may be unique or non-unique depending on the type of alias. |
| 23 | `B_ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias pool code identifies a unique set or list of person identifiers (I.e., numbers). The alias pool code also determines the accept/display format for the unique set of identifiers. |
| 24 | `B_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Person alias type code identifies a kind or type of alias (i.e., SSN, MRN, Financial Number, Community MRN, etc.). They have Cerner pre-defined meanings in the common data foundation table allowing HNA applications to look for a specific kind of alias. |
| 25 | `B_BIRTH_DT_CD` | DOUBLE | NOT NULL |  | Birth date code indicates the kind of birth date and time value that is contained in the birth_dt_tm field. (i.e., estimated, still born, unknow, etc.) |
| 26 | `B_BIRTH_DT_TM` | DATETIME |  |  | The date and time of birth for the person. |
| 27 | `B_BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 28 | `B_CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | This is the person responsible for creating a row in the person table. |
| 29 | `B_NAME_FIRST_KEY` | VARCHAR(100) |  |  | This is the person's first given name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 30 | `B_NAME_LAST_KEY` | VARCHAR(100) |  |  | This is the person's family name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 31 | `B_NAME_MIDDLE` | VARCHAR(100) |  |  | This is the person's middle or secondary given name or names. |
| 32 | `B_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 33 | `B_PHONETIC` | CHAR(8) |  |  | This is the Soundex coded representation of the person's name. This field is used for indexing and searching for a patient by name when the exact spelling is not known. |
| 34 | `B_SEX_CD` | DOUBLE | NOT NULL |  | The gender of the patient (i.e., male, female, unknown). |
| 35 | `B_SSN_ALIAS` | VARCHAR(200) |  |  | The Social Security Number (SSN) alias for the person. |
| 36 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 37 | `EXCEPTION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates type of exception (ex. Block Reconcile, Open Encounter) |
| 38 | `MATCH_DT_TM` | DATETIME |  |  | The date and time when the potential or proposed person match was identified. |
| 39 | `MATCH_SOURCE_CD` | DOUBLE | NOT NULL |  | Identifies the general method used to identify the proposed person match. |
| 40 | `MATCH_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the proposed person match (I.e., proposed, review, match, no match, etc.). |
| 41 | `MATCH_STATUS_CHG_DT_TM` | DATETIME |  |  | The date/time when a person match row became pending person match row. |
| 42 | `MATCH_STATUS_DT_TM` | DATETIME |  |  | The date and time a pending match is to be updated. |
| 43 | `MATCH_WEIGHT` | DOUBLE |  |  | A value between 0 and 100 representing the confidence level of the match based on match parameters. |
| 44 | `PERSON_MATCHES_ID` | DOUBLE | NOT NULL | PK | This is the person responsible for creating a row in the person matches table. |
| 45 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 46 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 47 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 48 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 49 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `A_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `B_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_COMBINE_BATCH](PERSON_COMBINE_BATCH.md) | `PERSON_MATCHES_ID` |

