# CAC_RULE_RELTN

> Stores the relationship of computer assisted coding rule sets to rules.

**Description:** Computer Assisted Coding Rule Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CAC_RULE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of ht unique primary identifier of the CAC_RULE table. This is the rule that the rule set is related to. |
| 2 | `CAC_RULE_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CAC_RULE_RELTN table. |
| 3 | `CAC_RULE_SET_ID` | DOUBLE | NOT NULL | FK→ | This is the value of ht unique primary identifier of the CAC_RULE_SET table. This is the rule set that the rule is related to. |
| 4 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | A number that represents the order the CAC Rule will be run within the CAC Rule Set. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CAC_RULE_ID` | [CAC_RULE](CAC_RULE.md) | `CAC_RULE_ID` |
| `CAC_RULE_SET_ID` | [CAC_RULE_SET](CAC_RULE_SET.md) | `CAC_RULE_SET_ID` |

