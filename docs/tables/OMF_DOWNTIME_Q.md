# OMF_DOWNTIME_Q

> Logs transactions during Care Profiling downtime.

**Description:** Logs transactions during Care Profiling downtime (OCD installs).  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHAR1` | VARCHAR(255) |  |  | Stores character data. |
| 2 | `CHAR2` | VARCHAR(255) |  |  | Stores character data. |
| 3 | `CHAR3` | VARCHAR(255) |  |  | Stores character data. |
| 4 | `CHAR4` | VARCHAR(255) |  |  | Stores character data. |
| 5 | `CHAR5` | VARCHAR(255) |  |  | Stores character data. |
| 6 | `DATE1` | DATETIME |  |  | Stores dates. |
| 7 | `DATE2` | DATETIME |  |  | Stores dates. |
| 8 | `DATE3` | DATETIME |  |  | Stores dates. |
| 9 | `DATE4` | DATETIME |  |  | Stores dates. |
| 10 | `DATE5` | DATETIME |  |  | Stores dates. |
| 11 | `NUM1_ID` | DOUBLE | NOT NULL |  | Stores a millennium identifier. |
| 12 | `NUM2_ID` | DOUBLE | NOT NULL |  | Stores a millennium identifier. |
| 13 | `NUM3_ID` | DOUBLE | NOT NULL |  | Stores a millennium identifier. |
| 14 | `NUM4_ID` | DOUBLE | NOT NULL |  | Stores a millennium identifier. |
| 15 | `NUM5_ID` | DOUBLE | NOT NULL |  | Stores a millennium identifier. |
| 16 | `PROCESS_FLAG` | DOUBLE |  |  | Indicates whether or not the data has been processed by omf_downtime_load. |
| 17 | `Q_ID` | DOUBLE | NOT NULL |  | The unique identifier for the table. |
| 18 | `REQUEST` | DOUBLE | NOT NULL |  | The calling request that is responsible for populating the table. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

