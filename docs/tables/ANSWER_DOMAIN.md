# ANSWER_DOMAIN

> Answer Domains

**Description:** This table contains the answer domains  
**Table type:** REFERENCE  
**Primary key:** `ANSWER_DOMAIN_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANSWER_DOMAIN_DESCN` | VARCHAR(255) | NOT NULL |  | Description of the answer domain |
| 2 | `ANSWER_DOMAIN_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the answer_domain table. It is an internal system assigned number. |
| 3 | `ANSWER_DOMAIN_LABEL` | VARCHAR(30) | NOT NULL |  | A short description of the answer domain less than 30 characters |
| 4 | `ANSWER_DOMAIN_TYPE_CD` | DOUBLE | NOT NULL |  | The type of answer domain. It can be Range, Categorical, Date, Lab or Numerical. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ANSWER_FORMAT](ANSWER_FORMAT.md) | `ANSWER_DOMAIN_ID` |
| [CATEGORY_ITEM](CATEGORY_ITEM.md) | `ANSWER_DOMAIN_ID` |

