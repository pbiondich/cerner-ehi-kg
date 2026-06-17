# SUBSCRPTN_FILTER_MSG_HIST

> Subscription Filter History Information

**Description:** Subscription Filter History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_PRSNL_R_CD` | DOUBLE | NOT NULL |  | The Encounter/Personnel relationship code indicating this type of relationship is being taken into consideration for the associated subscription. |
| 2 | `EXPIRATION_DT_TM` | DATETIME | NOT NULL |  | The Date and Time the associated Encounter/Personnel relationship or Person/Personnel relationship is set to expire. |
| 3 | `HOLD_FLAG` | DOUBLE | NOT NULL |  | The hold flag indicates if the subscription filter is on hold or activated. Hold Flag values are: 0 - No holds / activated, 1 - Holding for encounter discharge, 2 - User unsubscribed |
| 4 | `MSG_FYI_ASSIGNMENT_ID` | DOUBLE | NOT NULL |  | FK VALUE FROM MSG_FYI_ASSIGNMENT |
| 5 | `PERSON_PRSNL_R_CD` | DOUBLE | NOT NULL |  | The Person/Personnel relationship code indicating this type of relationship is being taken into consideration for the associated subscription. |
| 6 | `PURGE_DT_TM` | DATETIME |  |  | The Date and Time the SUBSCRIPTION_FILTER row was purged. |
| 7 | `SUBSCRIBE_DT_TM` | DATETIME |  |  | The Date and Time the filter was subscribed to by the provider. Currently, only populated by ad hoc filters. |
| 8 | `SUBSCRIPTION_FILTER_MSG_ID` | DOUBLE | NOT NULL |  | Unique, generated number that is used to identify an individual row on the SUBSCRIPTION_FILTER_MSG table. |
| 9 | `SUBSCRIPTION_ID` | DOUBLE | NOT NULL |  | Unique, generated number that is used to identify an individual row on the SUBSCRIPTION table. |
| 10 | `SUBSCRPTN_FILTER_MSG_HIST_ID` | DOUBLE | NOT NULL |  | Unique, generated number that is used to identify an individual row on the SUBSCRIPTION_FILTER_HISTORY table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

