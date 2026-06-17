# VALID_ANSWER_CAT

> This table stores valid answers for categorical questions.

**Description:** VALID ANSWER CAT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANSWER_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a row in the answer format table. The answer format to which this valid answer relates to |
| 2 | `CATEGORY_ITEM_ID` | DOUBLE | NOT NULL | FK→ | This identifies the category Item that is a valid answer |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `VALID_ANSWER_CAT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row in the valid_answer_cat table. It is a system assigned number. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANSWER_FORMAT_ID` | [ANSWER_FORMAT](ANSWER_FORMAT.md) | `ANSWER_FORMAT_ID` |
| `CATEGORY_ITEM_ID` | [CATEGORY_ITEM](CATEGORY_ITEM.md) | `CATEGORY_ITEM_ID` |

