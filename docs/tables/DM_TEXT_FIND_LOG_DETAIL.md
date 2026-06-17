# DM_TEXT_FIND_LOG_DETAIL

> This table will store log and status of detailed actions performed by Interrogator server 520

**Description:** Interrogator server log details  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_MESSAGE` | VARCHAR(255) |  |  | Contains message about status |
| 2 | `DETAIL_STATUS` | VARCHAR(20) |  |  | Contains the status information of log row |
| 3 | `DM_TEXT_FIND_LOG_DETAIL_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 4 | `DM_TEXT_FIND_LOG_ID` | DOUBLE | NOT NULL | FK→ | Reference to the DM_TEXT_FIND_LOG row that logging affects |
| 5 | `END_DT_TM` | DATETIME |  |  | Contains date/time when logging ended |
| 6 | `START_DT_TM` | DATETIME |  |  | Contains date/time when logging started |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_TEXT_FIND_LOG_ID` | [DM_TEXT_FIND_LOG](DM_TEXT_FIND_LOG.md) | `DM_TEXT_FIND_LOG_ID` |

