# RULE_AUDIT

> This table provides an audit trail of the rules that were run for database cleanups. Tracks changes made by the ExpireEventAction.exe tool (or an Ops job that automatically runs some of the expire rules defined in that tool).

**Description:** This table provides an audit trail of the rules that were run for database clean  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARAMETER_DEFINITION` | VARCHAR(250) | NOT NULL |  | Sentence version of the rule |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key of the Rule_Audit table. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Parent Entity Name is "EXPIRE_RULE" |
| 4 | `ROWS_UPDATED` | DOUBLE | NOT NULL |  | The number of rows that updated as a result of running the rule. |
| 5 | `RULE_AUDIT_ID` | DOUBLE | NOT NULL |  | Unique identifier for the RULE_AUDIT table. |
| 6 | `RUN_DT_TM` | DATETIME | NOT NULL |  | The date and time of the rule execution. |
| 7 | `RUN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the personnel that ran the rule. |
| 8 | `RUN_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates if the rule was run in an AdHoc mode or through Ops Job. Valid values are 0- operations, 1 - AdHoc |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RUN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

