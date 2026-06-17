# SN_TRACK_RULE

> This is the parent table for all client defined rules used in Surginet Case Tracking

**Description:** Surginet Track Rule Table  
**Table type:** REFERENCE  
**Primary key:** `SN_TRACK_RULE_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `RULE_NAME` | VARCHAR(255) |  |  | Client defined name given to the rule. xxx |
| 3 | `RULE_SEQUENCE` | DOUBLE | NOT NULL |  | The order in which the rules are processed |
| 4 | `RULE_TYPE_CD` | DOUBLE | NOT NULL |  | Denotes the template used to create the rule. |
| 5 | `SN_TRACK_RULE_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 6 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL |  | Foreign key to identify the tracking group associates with this rule. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_TRACK_RULE_PROMPT](SN_TRACK_RULE_PROMPT.md) | `SN_TRACK_RULE_ID` |

