# DM_DELETE_TRACKING

> This table is used to identify deleted rows from select Millennium tables. This data is used by the Crawler to update corresponding tables in the Cloud.

**Description:** Data Management Delete Tracking  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_TEXT` | VARCHAR(4000) |  |  | Used in the small chance they need to store a character based parent id value, or if we need to store 2 or more pieces of key data (e.g. a composite key). |
| 2 | `DM_DELETE_TRACKING_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DM_DELETE_TRACKING table. |
| 3 | `LAST_UTC_TS` | DATETIME(6) |  |  | LAST_UTC_TS is the timestamp when the row in the table was last updated or inserted. The timestamp is populated by a trigger on the table. This column is primarily used by the Project Go Millennium crawlers to determine when they need to send new or updated rows to the cloud |
| 4 | `PARENT_ENTITY_ID` | DOUBLE |  |  | The primary key ID of the 'grouper' table that this table is a part of. Usually this is the foreign key column from the table in column TABLE_NAME pointing back to the parent table in column PARENT_ENTITY_NAME. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(255) |  |  | This is a grouping name. Crawlers are configured into table `groups¿, or concepts. For example the PERSON crawler watches for changes on PERSON, PERSON_PATIENT, PERSON_ALIAS, etc.). The PARENT_ENTITY_NAME for a delete on PERSON_ALIAS will be PERSON, not PERSON_ALIAS. For some tables already having the parent_entity_name concept built into them (like ADDRESS or PHONE), this column is used to help identify which parent the delete belongs to as well. |
| 6 | `PURGE_APPL_NBR` | DOUBLE | NOT NULL |  | In order to improve Millennium+ crawler's performance, we need to prevent it from crawling Purge deletes. This is for the purpose of tracking Purge deletes, |
| 7 | `TABLE_NAME` | VARCHAR(30) |  |  | The name of the table the row was deleted from. |
| 8 | `TABLE_PK_VALUE` | DOUBLE |  |  | The PK value corresponding to the PK of whatever table is in TABLE_NAME. Improve process performance by grabbing this column instead of having to grab and parse DATA_TEXT (when possible). Will only contain the PK if the PK is a numeric single column PK. |
| 9 | `TXN_ID_TEXT` | VARCHAR(200) |  |  | The Oracle transaction_id value for one or more DML statements in a session before a commit occurred. This column is used to tie a row on this table back to the Millennium table that inserted (using a trigger) the row . |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

