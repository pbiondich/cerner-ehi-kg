# CNT_COND_EXPRESSION_KEY

> Contains details about working view conditional expression, which are used by Bedrock tool. Imported using content manager tool.

**Description:** CNT Conditional Expression  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CNT_COND_EXPRESSION_KEY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `CNT_COND_EXPRESSION_KEY_UID` | VARCHAR(100) |  |  | UID (uique identification) number which is used in versioning of conditional expression in conjunctionwith version_dt_tm column. |
| 4 | `COND_EXPRESSION_ID` | DOUBLE | NOT NULL |  | Value of the expression ID which is used to uniquely identify the conditional expression, |
| 5 | `COND_EXPRESSION_NAME` | VARCHAR(100) |  |  | short description what the expression and conditionality is meant for. |
| 6 | `COND_EXPRESSION_TXT` | VARCHAR(512) |  |  | String representation of the condition |
| 7 | `COND_POSTFIX_TXT` | VARCHAR(512) |  |  | postfix notation of the expression, help us to parse and calculate the logic |
| 8 | `DCP_COND_EXPRESSION_REF_ID` | DOUBLE | NOT NULL | FK→ | refers to original COND_EXPRESSION table which is used by bedrock tool |
| 9 | `MULTIPLE_IND` | DOUBLE | NOT NULL |  | Indicates multiple DTA can trigger the expression |
| 10 | `PREV_COND_EXPRESSION_ID` | DOUBLE | NOT NULL |  | unique identifier for condition expression and will not change between versions |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VERSION_DT_TM` | DATETIME |  |  | Date and time when this record was updated, used in versioning of the conditional expression in conjunction with UID column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_COND_EXPRESSION_REF_ID` | [COND_EXPRESSION](COND_EXPRESSION.md) | `COND_EXPRESSION_ID` |

