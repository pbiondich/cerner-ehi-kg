# DM_STAT_SNAPS

> This table is the parent for all database monitoring snapshots.

**Description:** Statistical Snapshots  
**Table type:** ACTIVITY  
**Primary key:** `DM_STAT_SNAP_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLIENT_MNEMONIC` | VARCHAR(10) | NOT NULL |  | Mnemonic taken from the DM_INFO.INFO_CHAR column where INFO_DOMAIN = 'DATA MANAGEMENT', INFO_NAME = 'CLIENT MNEMONIC' |
| 2 | `DM_STAT_SNAP_ID` | DOUBLE | NOT NULL | PK | Primary key popped from the DM_SEQ sequence. |
| 3 | `DOMAIN_NAME` | VARCHAR(20) | NOT NULL |  | Domain name as taken from req_data->domain |
| 4 | `NODE_NAME` | VARCHAR(30) | NOT NULL |  | Node name as taken from the CURNODE variable. |
| 5 | `SNAPSHOT_TYPE` | VARCHAR(100) | NOT NULL |  | Indicates the type of snapshot taken. Allows the table to be used on various types of snapshots. (system stats, score reports, etc.) |
| 6 | `STAT_SNAP_DT_TM` | DATETIME | NOT NULL |  | Indicates the DATE time that the snapshot was taken. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_STAT_SNAPS_VALUES](DM_STAT_SNAPS_VALUES.md) | `DM_STAT_SNAP_ID` |

