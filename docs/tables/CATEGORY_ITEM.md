# CATEGORY_ITEM

> This table contains all the categories associated with categorical eligibility questions.

**Description:** This table contains all the categories associated with categorical questions  
**Table type:** REFERENCE  
**Primary key:** `CATEGORY_ITEM_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANSWER_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | Indicates the answer domain to which this category_item belongs |
| 2 | `CATEGORY_ITEM_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the category_item table. It is an internal system assigned number. |
| 3 | `CATEGORY_ITEM_NBR` | DOUBLE | NOT NULL |  | The number of the category For Ex: A category 'Sex' can have three choices 'Male', 'Female' and 'Unknown'. In this case the Category_item_nbr will be 1, 2 and 3 respectively. |
| 4 | `CATEGORY_ITEM_TEXT` | VARCHAR(255) | NOT NULL |  | The textual description of the category item |
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

## Referenced by (1)

| From table | Column |
|------------|--------|
| [VALID_ANSWER_CAT](VALID_ANSWER_CAT.md) | `CATEGORY_ITEM_ID` |

