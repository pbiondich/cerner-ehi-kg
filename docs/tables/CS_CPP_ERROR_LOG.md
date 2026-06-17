# CS_CPP_ERROR_LOG

> Contains error records produced from the charge services preprocessor.

**Description:** Charge Services - Charge Preprocessor Error Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CS_CPP_ERROR_LOG_ID` | DOUBLE | NOT NULL |  | Uniquely identifies an error log entry. |
| 6 | `CS_CPP_RULESET_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the ruleset related to this error log entry. |
| 7 | `CS_CPP_RULE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely Identifies the rule related to there is error log entry. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter related to this error log entry. |
| 9 | `ERROR_DT_TM` | DATETIME | NOT NULL |  | The date and time of the error. |
| 10 | `ERROR_TEXT` | VARCHAR(200) | NOT NULL |  | Contains the description of the error that occurred for a particular rule. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person related to this error log entry. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CS_CPP_RULESET_ID` | [CS_CPP_RULESET](CS_CPP_RULESET.md) | `CS_CPP_RULESET_ID` |
| `CS_CPP_RULE_ID` | [CS_CPP_RULE](CS_CPP_RULE.md) | `CS_CPP_RULE_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

