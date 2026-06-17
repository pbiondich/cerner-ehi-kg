# ANSWER_FORMAT

> answer_format contains valid answer formats for protocol eligibility questions. One or more answer formats make up an answer domain.

**Description:** answer_format contains valid answer formats for protocol eligibility questions.  
**Table type:** REFERENCE  
**Primary key:** `ANSWER_FORMAT_ID`  
**Columns:** 9  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANSWER_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the answer_domain table. It is an internal system assigned number. |
| 2 | `ANSWER_FORMAT_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the answer_format table. It is an internal system assigned number. |
| 3 | `FORMAT_DESCN` | VARCHAR(255) | NOT NULL |  | A textual description of the format |
| 4 | `FORMAT_LABEL` | VARCHAR(30) | NOT NULL |  | A short display label less than 30 characters in length |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANSWER_DOMAIN_ID` | [ANSWER_DOMAIN](ANSWER_DOMAIN.md) | `ANSWER_DOMAIN_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ELIG_QUEST_LIBRARY](ELIG_QUEST_LIBRARY.md) | `ANSWER_FORMAT_ID` |
| [PROT_ELIG_QUEST](PROT_ELIG_QUEST.md) | `ANSWER_FORMAT_ID` |
| [VALID_ANSWER_CAT](VALID_ANSWER_CAT.md) | `ANSWER_FORMAT_ID` |

