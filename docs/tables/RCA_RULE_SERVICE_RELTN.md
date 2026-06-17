# RCA_RULE_SERVICE_RELTN

> This table defines a relationship between a rule and a rule service.

**Description:** Revenue Cycle Ambulatory Rule Service Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RCA_RULE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the rule in this relationship. |
| 2 | `RCA_RULE_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related RCA_RULE_SERVICE. |
| 3 | `RCA_RULE_SERVICE_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between an RCA_RULE and an RCA_RULE_SERVICE. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCA_RULE_ID` | [RCA_RULE](RCA_RULE.md) | `RCA_RULE_ID` |
| `RCA_RULE_SERVICE_ID` | [RCA_RULE_SERVICE](RCA_RULE_SERVICE.md) | `RCA_RULE_SERVICE_ID` |

