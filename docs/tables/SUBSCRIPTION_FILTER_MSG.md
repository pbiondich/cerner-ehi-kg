# SUBSCRIPTION_FILTER_MSG

> Subscription Filter / MSG information

**Description:** Subscription Filter / MSG relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_PRSNL_R_CD` | DOUBLE | NOT NULL |  | The Encounter/Personnel relationship code indicating this type of relationship is being taken into consideration for the associated subscription. |
| 2 | `EXPIRATION_DT_TM` | DATETIME | NOT NULL |  | The Date and Time the associated Encounter/Personnel relationship or Person/Personnel relationship is set to expire. |
| 3 | `HOLD_FLAG` | DOUBLE | NOT NULL |  | The hold flag indicates if the subscription filter is on hold or activated. Hold Flag values are: 0 - No holds / activated, 1 - Holding for encounter discharge, 2 - User unsubscribed |
| 4 | `MSG_FYI_ASSIGNMENT_ID` | DOUBLE | NOT NULL | FK→ | Unique, generated number that is used to identify an individual row on the MSG_FYI_ASSIGNMENT table. |
| 5 | `PERSON_PRSNL_R_CD` | DOUBLE | NOT NULL |  | The Person/Personnel relationship code indicating this type of relationship is being taken into consideration for the associated subscription. |
| 6 | `SUBSCRIBE_DT_TM` | DATETIME |  |  | The Date and Time the filter was subscribed to by the provider. Currently, only populated by ad hoc filters. |
| 7 | `SUBSCRIPTION_FILTER_MSG_ID` | DOUBLE | NOT NULL |  | Unique, generated number that is used to identify an individual row on the SUBSCRIPTION_FILTER_MSG table. |
| 8 | `SUBSCRIPTION_ID` | DOUBLE | NOT NULL | FK→ | Unique, generated number that is used to identify an individual row on the SUBSCRIPTION table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MSG_FYI_ASSIGNMENT_ID` | [MSG_FYI_ASSIGNMENT](MSG_FYI_ASSIGNMENT.md) | `MSG_FYI_ASSIGNMENT_ID` |
| `SUBSCRIPTION_ID` | [SUBSCRIPTION](SUBSCRIPTION.md) | `SUBSCRIPTION_ID` |

