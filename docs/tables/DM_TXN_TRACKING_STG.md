# DM_TXN_TRACKING_STG

> To eliminate continuous insert/update write patterns in DM_TXN_TRACKING an intermediate 'staging' transaction-tracking table is needed as a bridge between clinical trigger write activity and crawler service read activity. Queries will be always be doing a Full Table Scan and then DELETING all the data that was queried.

**Description:** Data Management Transaction Tracking Staging  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPL_CONTEXT_NBR` | DOUBLE |  |  | Similar to the purge_appl_nbr on DM_DELETE_TRACKING, we can engineer triggers to watch for and propagate application contexts at the transaction level (e.g. think combines, or purges). Might facilitate design patterns having this at a tranaction level. |
| 2 | `DEL_IND` | DOUBLE |  |  | Indicates if a delete operation fired the trigger for the transaction. |
| 3 | `INST_ID` | DOUBLE |  |  | Represents the Oracle instance number from where the INSERT came from. This will be used in the future for partitioning purposes. |
| 4 | `OWNER_NAME` | VARCHAR(30) |  |  | The owner of the table. Defaults to V500. |
| 5 | `TABLE_NAME` | VARCHAR(30) |  |  | The table_name where the transaction occurred. |
| 6 | `TXN_ID_TEXT` | VARCHAR(200) |  |  | The Oracle transaction_id value for one or more DML statements in a session before a commit occurred. This column is used to tie a row on this table back to the Millennium table that inserted (using a trigger) the row . |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

