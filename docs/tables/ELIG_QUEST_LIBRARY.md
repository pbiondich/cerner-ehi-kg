# ELIG_QUEST_LIBRARY

> This table contains library questions. These library questions can be imported to create specific amendment level questions.

**Description:** This table stores the library questions that are not related to an amendment.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANSWER_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | The answer format that contains the valid answer for the question |
| 2 | `DATE_REQUIRED_FLAG` | DOUBLE | NOT NULL |  | Indicates if a date is required when answering this question |
| 3 | `ELIG_QUEST_LIBRARY_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the elig_quest_library table. It is an internal system assigned number. |
| 4 | `EQL_CAT_CD` | DOUBLE | NOT NULL |  | Idneitifies which group this library question belongs to |
| 5 | `EQL_LABEL` | VARCHAR(30) | NOT NULL |  | A short display label for the question (< 30 characters) |
| 6 | `EQL_QUESTION` | VARCHAR(2000) | NOT NULL |  | *OBSOLETE - Question Text. Replaced by value associate with LONG_TEXT_ID from Long Text Reference |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | References the Long Text for the eligible question. Foreign Key from Long Text Reference table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `VALUE_REQUIRED_FLAG` | DOUBLE | NOT NULL |  | Indicates if a value is required for the question. 0 indicates not required. 1 indicates required and 2 indicates optional |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANSWER_FORMAT_ID` | [ANSWER_FORMAT](ANSWER_FORMAT.md) | `ANSWER_FORMAT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

