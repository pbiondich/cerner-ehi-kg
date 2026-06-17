# QC_RULE

> Stores the definitions for quality control rules that are used by the system

**Description:** Quality Control Rule  
**Table type:** REFERENCE  
**Primary key:** `RULE_ID`, `SEQUENCE`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACROSS_CONTROL_IND` | DOUBLE |  |  | Indicates whether the quality control rule is defined for across control checking. A value of 0 indicates the rule is defined for within control checking. A value of 1 indicates the rule is defined for across control checking. |
| 2 | `ACROSS_RUN_IND` | DOUBLE |  |  | Indicates whether the quality control rule is defined to check across runs. A value of 0 indicates the rule is defined to check within runs. A value of 1 indicates the rule is defined to check across runs. |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `ERROR_FLAG` | DOUBLE |  |  | Defines the type of error encountered if a rule has failed. |
| 10 | `MAX_REQ_RESULTS` | DOUBLE |  |  | Defines the maximum number of results required to perform rule evaluation. Used internally. |
| 11 | `REQ_COMMENT_IND` | DOUBLE | NOT NULL |  | Indicator to require comment entered if this rule fails. |
| 12 | `REQ_TROUBLE_STEP_IND` | DOUBLE | NOT NULL |  | Indicator to require trouble shooting step selected if this rule fails. |
| 13 | `RULE_DEFINITION` | VARCHAR(60) |  |  | Character description of the rule being defined. |
| 14 | `RULE_FORM_FLAG` | DOUBLE |  |  | Defines the type of rule that is being defined, such as a-bs. |
| 15 | `RULE_ID` | DOUBLE | NOT NULL | PK FK→ | A unique, internal, system-assigned number that identifies a specific quality control rule. Creates a relationship to the quality control rule type table. |
| 16 | `SEQUENCE` | DOUBLE | NOT NULL | PK | Defines the display sequence of the quality control rules. |
| 17 | `TRIG_IND` | DOUBLE |  |  | Indicates whether the quality control rule is a trigger rule. A value of 0 indicates this is not a trigger rule. A value of 1 indicates that this is a trigger rule - meaning if this rule fails, continue checking the rest of the rules defined. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RULE_ID` | [QC_RULE_TYPE](QC_RULE_TYPE.md) | `RULE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [QC_RESULT_RULE_R](QC_RESULT_RULE_R.md) | `RULE_ID` |
| [QC_RESULT_RULE_R](QC_RESULT_RULE_R.md) | `SEQUENCE` |

