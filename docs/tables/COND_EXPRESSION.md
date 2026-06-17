# COND_EXPRESSION

> Stores conditional expression that will enable or disable controls

**Description:** Stores conditional expression  
**Table type:** REFERENCE  
**Primary key:** `COND_EXPRESSION_ID`  
**Columns:** 14  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COND_EXPRESSION_ID` | DOUBLE | NOT NULL | PK | Primary way to distinguish |
| 4 | `COND_EXPRESSION_NAME` | VARCHAR(100) | NOT NULL |  | Short description what the expression and conditionality is meant for. |
| 5 | `COND_EXPRESSION_TXT` | VARCHAR(512) | NOT NULL |  | String representation of the condition. |
| 6 | `COND_POSTFIX_TXT` | VARCHAR(512) | NOT NULL |  | Postfix notation of the expression, helps us to parse and calculate the logic |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `MULTIPLE_IND` | DOUBLE | NOT NULL |  | Indicates multiple DTA can trigger the expression. |
| 9 | `PREV_COND_EXPRESSION_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for condition expression and will not change between versions |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_COND_EXPRESSION_ID` | [COND_EXPRESSION](COND_EXPRESSION.md) | `COND_EXPRESSION_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CNT_COND_EXPRESSION_KEY](CNT_COND_EXPRESSION_KEY.md) | `DCP_COND_EXPRESSION_REF_ID` |
| [CONDITIONAL_DTA](CONDITIONAL_DTA.md) | `COND_EXPRESSION_ID` |
| [COND_EXPRESSION](COND_EXPRESSION.md) | `PREV_COND_EXPRESSION_ID` |
| [COND_EXPRESSION_COMP](COND_EXPRESSION_COMP.md) | `COND_EXPRESSION_ID` |

