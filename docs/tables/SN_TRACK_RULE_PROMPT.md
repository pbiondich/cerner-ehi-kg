# SN_TRACK_RULE_PROMPT

> This table holds the prompts for all client defined rules used in Surginet Case Tracking.

**Description:** Surginet Track Rule Prompt  
**Table type:** REFERENCE  
**Primary key:** `SN_TRACK_RULE_PROMPT_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `PROMPT_SEQUENCE` | DOUBLE | NOT NULL |  | Defines order of the prompts that allows us to determine what the prompt is based on the rule_type_flag of the parent sn_track_rule record. |
| 3 | `SN_TRACK_RULE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to sn_track_rule table |
| 4 | `SN_TRACK_RULE_PROMPT_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SN_TRACK_RULE_ID` | [SN_TRACK_RULE](SN_TRACK_RULE.md) | `SN_TRACK_RULE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_TRACK_RULE_RESPONSE](SN_TRACK_RULE_RESPONSE.md) | `SN_TRACK_RULE_PROMPT_ID` |

