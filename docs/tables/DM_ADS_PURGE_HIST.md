# DM_ADS_PURGE_HIST

> This table will contain purg data from all ADS Purge events executed inthe current domain.

**Description:** DM_ADS_PURGE_HISTORY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONFIG_NAME` | VARCHAR(120) | NOT NULL |  | Name of ADS Purge configuration |
| 2 | `DM_ADS_CONFIG_ID` | DOUBLE | NOT NULL |  | Foreign Key value from DM_ADS_CONFIG |
| 3 | `DM_ADS_PURGE_HIST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `PURGE_COUNT` | DOUBLE | NOT NULL |  | Count of number of rows that has been purged for each table |
| 5 | `PURGE_DT_TM` | DATETIME | NOT NULL |  | Date and time of purge action |
| 6 | `PURGE_USER` | VARCHAR(100) | NOT NULL |  | User who initiated the purge |
| 7 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of table where data has been purged |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

