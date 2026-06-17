# SUBSCRPTN_FILTER_RESULTS_RELTN

> Relationship table joining the SUBSCRIPTION_NEW_RESULTS table with the MSG_FYI_FILTER table.

**Description:** Subscription Filter Results Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MSG_FYI_FILTER_ID` | DOUBLE | NOT NULL | FK→ | Unique, generated number that is used to identify an individual row on the MSG_FYI_FILTER table. |
| 2 | `SUBSCRIPTION_NEW_RESULTS_ID` | DOUBLE | NOT NULL | FK→ | Unique, generated number that is used to identify an individual row on the SUBSCRIPTION_NEW_RESULTS table. |
| 3 | `SUBSCRPTN_FILTER_RESULTS_R_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MSG_FYI_FILTER_ID` | [MSG_FYI_FILTER](MSG_FYI_FILTER.md) | `MSG_FYI_FILTER_ID` |
| `SUBSCRIPTION_NEW_RESULTS_ID` | [SUBSCRIPTION_NEW_RESULTS](SUBSCRIPTION_NEW_RESULTS.md) | `SUBSCRIPTION_NEW_RESULTS_ID` |

