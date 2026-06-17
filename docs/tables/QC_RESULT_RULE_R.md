# QC_RESULT_RULE_R

> Maintains a relationship for the rules applied with those that failed or were not checked.

**Description:** Quality Control Result Rule Resolution  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `QC_RESULT_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific quality control result associated with a rule that failed or was checked. Creates a relationship to the quality control result table. |
| 2 | `RULE_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the rule that was applied to the quality control result. Creates a relationship to the quality control rule type table. |
| 3 | `SEQUENCE` | DOUBLE | NOT NULL | FK→ | Stores the sequence number from the QC rule table. |
| 4 | `STATUS_FLAG` | DOUBLE |  |  | Defines the status of the rule that was checked for the QC result. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QC_RESULT_ID` | [QC_RESULT](QC_RESULT.md) | `QC_RESULT_ID` |
| `RULE_ID` | [QC_RULE](QC_RULE.md) | `RULE_ID` |
| `SEQUENCE` | [QC_RULE](QC_RULE.md) | `SEQUENCE` |

