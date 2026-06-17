# RCA_RULE_RULE_RELTN

> The relationship between two RCA Rules

**Description:** Revenue Cycle Access Rule to Rule Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_RCA_RULE_ID` | DOUBLE |  | FK→ | The identifier of the rule rule in the relationship. |
| 2 | `PARENT_RCA_RULE_ID` | DOUBLE |  | FK→ | The identifier of the parent rule in the relationship. |
| 3 | `RCA_RULE_RULE_RELTN_ID` | DOUBLE | NOT NULL |  | A system generated identifier to uniquely identify a row on the RCA_RULE_RULE_RELTN table. |
| 4 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_RCA_RULE_ID` | [RCA_RULE](RCA_RULE.md) | `RCA_RULE_ID` |
| `PARENT_RCA_RULE_ID` | [RCA_RULE](RCA_RULE.md) | `RCA_RULE_ID` |

