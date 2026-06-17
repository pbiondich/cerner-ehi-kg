# COND_EXPRESSION_COMP

> The tables stores the Trigger DTA and conditions to evaluate the condition for them.

**Description:** COND_EXPRESSION_COMP  
**Table type:** REFERENCE  
**Primary key:** `COND_EXPRESSION_COMP_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COND_COMP_NAME` | VARCHAR(30) | NOT NULL |  | Unique description for the component for the expression |
| 4 | `COND_EXPRESSION_COMP_ID` | DOUBLE | NOT NULL | PK | Primary identifier for the table |
| 5 | `COND_EXPRESSION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from the cond_expression table |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `OPERATOR_CD` | DOUBLE | NOT NULL |  | Stores comparison operator between the triggerDTA and logical operator. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key to a table identified by PARENT_ENTITY_NAME |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(60) | NOT NULL |  | Parent table of nomenclature and codeset. |
| 10 | `PREV_COND_EXPRESSION_COMP_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the original version. |
| 11 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Required Ind for the conditionality |
| 12 | `RESULT_VALUE` | DOUBLE | NOT NULL |  | Result value that evaluates the component |
| 13 | `TRIGGER_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | The dta which enable or disable other dta's. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COND_EXPRESSION_ID` | [COND_EXPRESSION](COND_EXPRESSION.md) | `COND_EXPRESSION_ID` |
| `PREV_COND_EXPRESSION_COMP_ID` | [COND_EXPRESSION_COMP](COND_EXPRESSION_COMP.md) | `COND_EXPRESSION_COMP_ID` |
| `TRIGGER_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CNT_COND_EXPRSN_COMP_KEY](CNT_COND_EXPRSN_COMP_KEY.md) | `DCP_COND_EXP_COMP_ID_REF_ID` |
| [COND_EXPRESSION_COMP](COND_EXPRESSION_COMP.md) | `PREV_COND_EXPRESSION_COMP_ID` |

