# CMT_IMPORT_LOG

> Contains log information for CMT Content loads

**Description:** Community import log  
**Table type:** ACTIVITY  
**Primary key:** `CMT_IMPORT_LOG_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOCK_SIZE` | DOUBLE |  |  | Number of blocks to process at a time. |
| 2 | `CMT_IMPORT_LOG_ID` | DOUBLE | NOT NULL | PK | Sequence value |
| 3 | `END_DT_TM` | DATETIME | NOT NULL |  | end date and timeColumn |
| 4 | `INPUT_FILENAME` | VARCHAR(255) |  |  | input filenameColumn |
| 5 | `LOGFILE_NAME` | VARCHAR(50) |  |  | log file nameColumn |
| 6 | `LOG_LEVEL` | DOUBLE |  |  | Level of logging when load was run. |
| 7 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores a reference to text created by import logs. FK from LONG_TEXT table. |
| 8 | `PACKAGE_NBR` | DOUBLE |  |  | Package from which load was run. |
| 9 | `README` | DOUBLE |  |  | README number for installation |
| 10 | `SCRIPT_NAME` | VARCHAR(35) | NOT NULL |  | Script used to run load. |
| 11 | `START_DT_TM` | DATETIME | NOT NULL |  | Start date and time of load. |
| 12 | `START_RECORD` | DOUBLE |  |  | Starting record in csv file. |
| 13 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Load Status - 0 - success;1 - warnings;2 - failure |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CMT_IMPORT_LOG_MSG](CMT_IMPORT_LOG_MSG.md) | `CMT_IMPORT_LOG_ID` |

