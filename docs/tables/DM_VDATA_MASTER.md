# DM_VDATA_MASTER

> Store data about data compare process between 2 databases

**Description:** DM_VDATA_MASTER  
**Table type:** ACTIVITY  
**Primary key:** `DM_VDATA_MASTER_ID`  
**Columns:** 40  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPL_IDENT` | VARCHAR(100) |  |  | The client application id that compared the table/owner when status = 'EXECUTING' |
| 2 | `BEGIN_DT_TM` | DATETIME |  |  | Date the last compare began |
| 3 | `COLUMN_LIST` | LONGTEXT |  |  | Comma delimited list of column values to be compared for a table. |
| 4 | `COMPARE_INDEX_NAME` | VARCHAR(30) |  |  | The unique index name used to uniquely compare the data. |
| 5 | `COMPARE_STATUS` | VARCHAR(255) | NOT NULL |  | Status description of the last compare |
| 6 | `CURR_MISMATCH_ROW_CNT` | DOUBLE |  |  | The number of rows that mismatched on the current compare execution |
| 7 | `DATA_TYPE_LIST` | VARCHAR(4000) |  |  | Stores the data type list that makes up the uniquely indexed columns |
| 8 | `DM_VDATA_MASTER_ID` | DOUBLE | NOT NULL | PK | Primary Key Unique Identifier |
| 9 | `END_DT_TM` | DATETIME |  |  | Date the last compare ended |
| 10 | `KEYID_COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | The single unique indexed column name used during the compare process. |
| 11 | `LAG_DT_TM` | DATETIME |  |  | The max delivery lag at the time the table was compared. |
| 12 | `LAST_COMPARE_CNT` | DOUBLE |  |  | Count of rows last matched |
| 13 | `LAST_COMPARE_DT_TM` | DATETIME |  |  | Last Date/Time the table was compared. |
| 14 | `LAST_MATCH_CNT` | DOUBLE |  |  | Count of rows last matched |
| 15 | `LAST_MATCH_DT_TM` | DATETIME |  |  | Last date/time a table matched |
| 16 | `LAST_SRC_MOD_DT_TM` | DATETIME |  |  | The all_tab_modification.timestamp value at the time of the last compare. |
| 17 | `MAX_SRC_KEYID` | DOUBLE |  |  | The max key value from the Source table. |
| 18 | `MESSAGE_TXT` | VARCHAR(4000) |  |  | Stores informational and/or error messages that occur during compare. |
| 19 | `MISMATCH_BEG_KEYID` | DOUBLE |  |  | The min key value that was mismatched for the current compare range. |
| 20 | `MISMATCH_END_KEYID` | DOUBLE |  |  | The ending key value for the current compare range. |
| 21 | `MISMATCH_EVENT_CNT` | DOUBLE |  |  | Number of times a table has successively mismatched |
| 22 | `MISMATCH_ROWID` | VARCHAR(10) |  |  | The Source's rowid for the mismatched row. |
| 23 | `MISMATCH_ROW_DT_TM` | DATETIME |  |  | This value is returned from the Source table based on some updt_dt_tm (or equivalent) column during the compare process. |
| 24 | `MISMATCH_UNIQUE_KEY_TXT` | VARCHAR(4000) |  |  | the concatenated key for mismatches |
| 25 | `MM_PULL_KEY_FROM_SRC_IND` | DOUBLE |  |  | Indicates whether to pull updt_dt_tm and rowid mismatch values from the source database. |
| 26 | `OBJECT_ID_SRC` | DOUBLE |  |  | The object_id from all_objects for the table from the Source Database. |
| 27 | `OWNER_NAME` | VARCHAR(30) | NOT NULL |  | Table Owner |
| 28 | `PREV_MISMATCH_ROW_CNT` | DOUBLE |  |  | The number of rows that mismatched on the previous compare execution |
| 29 | `RANGE_BEG_KEYID` | DOUBLE |  |  | The beginning key value for the current compare range. |
| 30 | `RANGE_END_KEYID` | DOUBLE |  |  | The ending key value for the current compare range. |
| 31 | `RANGE_START_KEYID` | DOUBLE |  |  | The first key value to begin comparison on (key values previous to this value do not need to be compared). |
| 32 | `ROWS_TO_COMPARE` | DOUBLE |  |  | Number of Rows to Compare each time. |
| 33 | `ROW_DT_TM_COL_NAME` | VARCHAR(30) |  |  | The column name used to retrieve mismatched row's date/time |
| 34 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Table Name |
| 35 | `TTL_ROWS_COMPARED` | DOUBLE |  |  | The total cumulative number of rows compared for a table. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_VDATA_EXCLUDE_DTL](DM_VDATA_EXCLUDE_DTL.md) | `DM_VDATA_MASTER_ID` |

