# RCA_NOTIFICATION

> Represents notification actions for the Revenue Cycle solution.

**Description:** Revenue Cycle Ambulatory - Notification  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related logical domain. |
| 2 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The sequence index for the RCA_RULE_ID for a given LOGICAL_DOMAIN and TYPE_MEANING. |
| 3 | `RCA_NOTIFICATION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a notification action for the Revenue Cycle solution. |
| 4 | `RCA_RULE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a related Revenue Cycle Ambulatory Rule. |
| 5 | `TYPE_MEANING_TXT` | VARCHAR(100) |  |  | The meaning of the type of notification for the given Logical_Domain_ID. Valid values are "PATIENT" |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `RCA_RULE_ID` | [RCA_RULE](RCA_RULE.md) | `RCA_RULE_ID` |

