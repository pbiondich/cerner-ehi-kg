# MP_GROUP_REFRESH_STATE

> An activity table containing the current state of the caches in MPages Static Content Server

**Description:** MP GROUP REFRESH STATE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASE_FOLDER` | VARCHAR(255) | NOT NULL |  | The folder that will be refreshed. |
| 2 | `BASE_URL` | VARCHAR(200) | NOT NULL |  | An identifier for the WebSphere cluster on which the application is deployed. |
| 3 | `DIAGNOSTIC_INFO_TXT` | VARCHAR(255) |  |  | Optional diagnostic description of why a cache refresh failed. |
| 4 | `IS_PRIMED_IND` | DOUBLE | NOT NULL |  | Specifies whether all the files below the base folder have been read and loaded into the raw file cache. |
| 5 | `IS_READABLE_IND` | DOUBLE | NOT NULL |  | Specifies whether the base folder is readable. |
| 6 | `IS_REFRESHING_IND` | DOUBLE | NOT NULL |  | Specifies whether the web app is currently primining or getting mappings for the cache for a base folder. |
| 7 | `MP_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key value from the MP_GROUP table.The group id of the folder that will be refreshed - or 0 if the folder is specified in environment entries. |
| 8 | `MP_GROUP_REFRESH_STATE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `REFRESH_END_DT_TM` | DATETIME |  |  | The time the last cache refresh for this base folder completed. |
| 10 | `REFRESH_START_DT_TM` | DATETIME |  |  | The time the last cache refresh for this base folder started. |
| 11 | `SERVER_UUID` | VARCHAR(36) | NOT NULL |  | A UUID that is used to correlate a cache on a server to a row in the database. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MP_GROUP_ID` | [MP_GROUP](MP_GROUP.md) | `MP_GROUP_ID` |

