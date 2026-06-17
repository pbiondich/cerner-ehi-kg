# AP_PROMPT

> Prompt tests for specimen procedures.

**Description:** AP Prompt  
**Table type:** REFERENCE  
**Primary key:** `AP_PROMPT_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Contains the value used for the prompt procedure action |
| 2 | `AP_PROMPT_ID` | DOUBLE | NOT NULL | PK | Contains the identifier to uniquely identify an AP prompt. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Contains the specimen order catalog item. |
| 4 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Contains the prompt template text. |
| 5 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Contains the code for the specimen prompt procedure. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AP_PROMPT_FIELD](AP_PROMPT_FIELD.md) | `AP_PROMPT_ID` |

