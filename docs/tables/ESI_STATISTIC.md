# ESI_STATISTIC

> Keeps statistics for ESI Server transactions

**Description:** ESI STATISTIC  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADD_CODE_VALUE_CNT` | DOUBLE |  |  | Code Values added by this contributor systemColumn |
| 3 | `ADD_HEALTH_PLAN_CNT` | DOUBLE |  |  | Health Plans added by this contributor systemColumn |
| 4 | `ADD_ORGANIZATION_CNT` | DOUBLE |  |  | Organizations added by this contributor systemColumn |
| 5 | `ADD_PRSNL_CNT` | DOUBLE |  |  | Prsnl added by this contributor systemColumn |
| 6 | `AUTO_RECONCILE_CNT` | DOUBLE |  |  | Auto reconciles performed on transactions from this contributor systemColumn |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE |  |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `ESI_STATISTIC_ID` | DOUBLE | NOT NULL |  | ESI Statistic IDColumn |
| 11 | `LAST_UPDT_DT_TM` | DATETIME |  |  | Last date and time this row was updatedColumn |
| 12 | `NEW_ENCNTR_CNT` | DOUBLE |  |  | New encounters added by this contibutor system |
| 13 | `NEW_PERSON_CNT` | DOUBLE |  |  | New persons added by this contributor system |
| 14 | `TRANSACTION_CNT` | DOUBLE |  |  | Transactions received from this contributor systemColumn |
| 15 | `UPDT_ENCNTR_CNT` | DOUBLE |  |  | Encounters updated by this contributor systemColumn |
| 16 | `UPDT_PERSON_CNT` | DOUBLE |  |  | Person updated by this contributor system |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

