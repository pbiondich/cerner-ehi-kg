# DM_TABLES_DOC_LOCAL

> Copy of the dm_tables_doc admin table

**Description:** DM TABLES DOC LOCAL  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 41

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BPR_MAX` | DOUBLE |  |  | BPR_MAX |
| 2 | `BPR_MEAN` | DOUBLE |  |  | BPR_MEAN |
| 3 | `BPR_MIN` | DOUBLE |  |  | BPR_MIN |
| 4 | `BPR_STD_DEV` | DOUBLE |  |  | BPR_STD_DEV |
| 5 | `BYTES_PER_ROW` | DOUBLE |  |  | BYTES_PER_ROW |
| 6 | `CORE_IND` | DOUBLE |  |  | CORE_IND |
| 7 | `DATA_MODEL_SECTION` | VARCHAR(80) |  |  | DATA_MODEL_SECTION |
| 8 | `DEFINITION` | VARCHAR(500) |  |  | DEFINITION |
| 9 | `DELETE_FLG` | DOUBLE |  |  | DELETE_FLG |
| 10 | `DESCRIPTION` | VARCHAR(80) |  |  | DESCRIPTION |
| 11 | `DROP_IND` | DOUBLE |  |  | This column will be used mark tables for obsolete. |
| 12 | `FREELIST_CNT` | DOUBLE |  |  | freelist count |
| 13 | `FULL_TABLE_NAME` | VARCHAR(30) |  |  | Full Table Name |
| 14 | `GROWTH_CRITERIA` | VARCHAR(255) |  |  | GROWTH_CRITERIA |
| 15 | `HUMAN_REQD_IND` | DOUBLE |  |  | HUMAN_REQD_IND |
| 16 | `INSERT_FLG` | DOUBLE |  |  | INSERT_FLG |
| 17 | `MERGEABLE_IND` | DOUBLE |  |  | Mergeable Indicator |
| 18 | `MERGE_ACTIVE_IND` | DOUBLE |  |  | Merge Active Indicator |
| 19 | `MERGE_DELETE_IND` | DOUBLE |  |  | Merge Delete Indicator |
| 20 | `MERGE_UI_QUERY` | VARCHAR(255) |  |  | Merge UI Query |
| 21 | `PCT_FREE` | DOUBLE |  |  | PCT_FREE |
| 22 | `PCT_USED` | DOUBLE |  |  | PCT_USED |
| 23 | `PRIMARY_DELETE_SCRIPT` | VARCHAR(200) |  |  | PRIMARY_DELETE_SCRIPT |
| 24 | `PRIMARY_INSERT_SCRIPT` | VARCHAR(200) |  |  | PRIMARY_INSERT_SCRIPT |
| 25 | `PRIMARY_UPDATE_SCRIPT` | VARCHAR(200) |  |  | PRIMARY_UPDATE_SCRIPT |
| 26 | `PURGE_EXCEPT_IND` | DOUBLE |  |  | If set to 1, do not purge this table or any of its children after archiving an encounter. |
| 27 | `READS_FLG` | DOUBLE |  |  | READS_FLG |
| 28 | `REFERENCE_IND` | DOUBLE |  |  | REFERENCE_IND |
| 29 | `SCHEMA_REFRESH_DT_TM` | DATETIME |  |  | SCHEMA_REFRESH_DT_TM |
| 30 | `SCHEMA_REFRESH_REQUEST_DT_TM` | DATETIME |  |  | SCHEMA_REFRESH_REQUEST_DT_TM |
| 31 | `STATIC_ROWS` | DOUBLE |  |  | STATIC_ROWS |
| 32 | `STATIC_SIZE_FLG` | DOUBLE |  |  | STATIC_SIZE_FLG |
| 33 | `SUFFIXED_TABLE_NAME` | VARCHAR(18) |  |  | Suffixed Table Name |
| 34 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | TABLE_NAME |
| 35 | `TABLE_SUFFIX` | VARCHAR(4) | NOT NULL |  | Table Suffix in Text form. Usually a 4 character number with leading zeros |
| 36 | `UPDATE_FLG` | DOUBLE |  |  | UPDATE_FLG |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 40 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 41 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

