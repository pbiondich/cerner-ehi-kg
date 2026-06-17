# DM_TEXT_FIND_LOG

> This table will store log and status of actions performed by Interrogator server 520.

**Description:** Interrogator Server Log  
**Table type:** ACTIVITY  
**Primary key:** `DM_TEXT_FIND_LOG_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_TEXT_FIND_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Reference to the DM_TEXT_FIND_DETAIL row that logging affects |
| 2 | `DM_TEXT_FIND_LOG_ID` | DOUBLE | NOT NULL | PK | Primary Key for table |
| 3 | `END_DT_TM` | DATETIME |  |  | Contains date/time when logging ended |
| 4 | `LOG_DESCRIPTION` | VARCHAR(255) |  |  | Contains additional information about action being logged |
| 5 | `LOG_MESSAGE` | VARCHAR(255) |  |  | Contains message about status |
| 6 | `LOG_STATUS` | VARCHAR(20) |  |  | Contains the status information of log row |
| 7 | `START_DT_TM` | DATETIME |  |  | Contains date/time when logging started |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_TEXT_FIND_DETAIL_ID` | [DM_TEXT_FIND_DETAIL](DM_TEXT_FIND_DETAIL.md) | `DM_TEXT_FIND_DETAIL_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DM_TEXT_FIND_LOG_DETAIL](DM_TEXT_FIND_LOG_DETAIL.md) | `DM_TEXT_FIND_LOG_ID` |
| [DM_TEXT_FIND_QUEUE](DM_TEXT_FIND_QUEUE.md) | `DM_TEXT_FIND_LOG_ID` |
| [DM_TEXT_FIND_QUEUE_HIST](DM_TEXT_FIND_QUEUE_HIST.md) | `DM_TEXT_FIND_LOG_ID` |

