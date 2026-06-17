# CS_CPP_RULE

> Contains the rule information for the new Charge Preprocessor framework.

**Description:** Charge Services - Charge Preprocessor Rule  
**Table type:** REFERENCE  
**Primary key:** `CS_CPP_RULE_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `CHARGE_STATUS_IND` | DOUBLE | NOT NULL |  | Indicates the rule will ignore the charge status of other charges on each encounter or not. 0 -No, 1-Yes. |
| 4 | `CS_CPP_RULESET_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the ruleset related to this rule. |
| 5 | `CS_CPP_RULE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies rule information for the Charge Preprocessor framework. |
| 6 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies text related to this rule. |
| 7 | `PRIORITY_NBR` | DOUBLE | NOT NULL |  | The execution priority of a rule inside its associated ruleset. |
| 8 | `PROCESS_IND` | DOUBLE | NOT NULL |  | Indicates whether to process this rule or not. 0 - No, 1 - Yes |
| 9 | `RULE_BEG_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `RULE_END_DT_TM` | DATETIME | NOT NULL |  | The date and time after which the row is no longer valid as active current data. This may be valued with the date and time the row became inactive. |
| 11 | `RULE_NAME` | VARCHAR(100) | NOT NULL |  | The name of the rule. This is unique per ruleset. |
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
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CS_CPP_ERROR_LOG](CS_CPP_ERROR_LOG.md) | `CS_CPP_RULE_ID` |

