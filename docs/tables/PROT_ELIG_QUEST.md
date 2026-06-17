# PROT_ELIG_QUEST

> This table contains the eligibility questions associated with an amendment.

**Description:** PROT ELIG QUEST  
**Table type:** REFERENCE  
**Primary key:** `PROT_ELIG_QUEST_ID`  
**Columns:** 19  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANSWER_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | The primary key of Answer_format table. Identifies the valid answer for this question. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DATE_REQUIRED_FLAG` | DOUBLE | NOT NULL |  | Indicates if a date is required. |
| 4 | `DESIRED_VALUE` | VARCHAR(1) | NOT NULL |  | This field contains the answer to the question that implies eligibility (the desired value). |
| 5 | `ELIG_QUEST_NBR` | DOUBLE | NOT NULL |  | This field contains the number of the eligibility question (1-first, 2-second, 3-third etc.). |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | References the Long Text for the Eligible Question. Foreign Key from the Long Text Reference table. |
| 8 | `PREV_PROT_ELIG_QUEST_ID` | DOUBLE | NOT NULL | FK→ | The key for the original eligibility question of the versioned group. Used to support type-2 versioning. |
| 9 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_amendment table. This field identifies the protocol amendment for which the patient's eligibility is being evaluated. ***OBSOLETE*** |
| 10 | `PROT_ELIG_QUEST_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the prot_elig_quest table. It is an internal system assigned number. |
| 11 | `PROT_QUESTIONNAIRE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a questionnaire in the table |
| 12 | `QUESTION` | VARCHAR(2000) | NOT NULL |  | *OBSOLETE - Patient enrollment Eligibility Question. Replaced by value associate with LONG_TEXT_ID from Long Text Reference |
| 13 | `QUEST_TYPE_IND` | DOUBLE | NOT NULL |  | Indicates whether the question is an eligibility question or an informational question. If set to 1, it indicates that the question is an eligiblity question. If set to 0 it indicates that the question is an informational question. Informational quesitons do not impact eligiblity. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VALUE_REQUIRED_FLAG` | DOUBLE | NOT NULL |  | Indicates whether value is required or not. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANSWER_FORMAT_ID` | [ANSWER_FORMAT](ANSWER_FORMAT.md) | `ANSWER_FORMAT_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `PREV_PROT_ELIG_QUEST_ID` | [PROT_ELIG_QUEST](PROT_ELIG_QUEST.md) | `PROT_ELIG_QUEST_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |
| `PROT_QUESTIONNAIRE_ID` | [PROT_QUESTIONNAIRE](PROT_QUESTIONNAIRE.md) | `PROT_QUESTIONNAIRE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PROT_ELIG_QUEST](PROT_ELIG_QUEST.md) | `PREV_PROT_ELIG_QUEST_ID` |
| [PT_ELIG_RESULT](PT_ELIG_RESULT.md) | `PROT_ELIG_QUEST_ID` |

