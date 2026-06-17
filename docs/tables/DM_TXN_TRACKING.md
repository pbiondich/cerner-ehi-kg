# DM_TXN_TRACKING

> This table tracks transactions from all tables being crawled as part of the Millennium+ platform. It utilizes the Oracle System Change Number to manage the processing of the data appropriately and accurately. The rows on this table are populated by triggers on Millennium tables.

**Description:** Data Management Transaction Tracking  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPL_CONTEXT_NBR` | DOUBLE |  |  | Similar to the purge_appl_nbr on DM_DELETE_TRACKING, we can engineer triggers to watch for and propagate application contexts at the transaction level (e.g. think combines, or purges). Might facilitate design patterns having this at a tranaction level. |
| 2 | `DEL_IND` | DOUBLE |  |  | Indicates if a delete operation fired the trigger for the transaction. |
| 3 | `OWNER_NAME` | VARCHAR(30) |  |  | The owner of the table. Defaults to V500. |
| 4 | `ROW_SCN` | DOUBLE |  |  | Updated with ORA_ROWSCN by the background job. It will get initialized to 0 on insert. ORA_ROWSCN is an Oracle pseudo column that contains the Oracle System Change Number for a transaction. The SCN will be at a block level unless the table is created with option ROWDEPENDANCIES, then it is at the row level. DM_TXN_TRACKING table does have the ROWDEPENDANCIES option. |
| 5 | `TABLE_NAME` | VARCHAR(30) |  |  | The table_name where the transaction occurred. |
| 6 | `TXN_ID_TEXT` | VARCHAR(200) |  |  | The Oracle transaction_id value for one or more DML statements in a session before a commit occurred. This column is used to tie a row on this table back to the Millennium table that inserted (using a trigger) the row . |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

