# CS_CPP_RULESET

> Contains the ruleset information linking the rule to the tier in the new Charge Preprocessor framework. Also stores change history of the table.

**Description:** Charge Services - Charge Preprocessor Ruleset  
**Table type:** REFERENCE  
**Primary key:** `CS_CPP_RULESET_ID`  
**Columns:** 14  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CS_CPP_RULESET_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a Charge Services - Charge preprocessor ruleset. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PREV_CS_CPP_RULESET_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the charge services - charge preprocessor ruleset information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 7 | `PROCESS_IND` | DOUBLE | NOT NULL |  | Indicates whether to process this ruleset or not. 0 - No, 1 - Yes. |
| 8 | `RULESET_NAME` | VARCHAR(100) | NOT NULL |  | Contains the unique name of a ruleset. |
| 9 | `RULESET_NAME_KEY` | VARCHAR(100) | NOT NULL |  | This contains the same value as the ruleset name except it is in all caps and has no spaces or special characters. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_CS_CPP_RULESET_ID` | [CS_CPP_RULESET](CS_CPP_RULESET.md) | `CS_CPP_RULESET_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CS_CPP_ERROR_LOG](CS_CPP_ERROR_LOG.md) | `CS_CPP_RULESET_ID` |
| [CS_CPP_RULE](CS_CPP_RULE.md) | `CS_CPP_RULESET_ID` |
| [CS_CPP_RULESET](CS_CPP_RULESET.md) | `PREV_CS_CPP_RULESET_ID` |

