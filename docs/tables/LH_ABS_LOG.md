# LH_ABS_LOG

> Hold debugging and informational information about eQualityCheck (abstrctor) processes

**Description:** LH_ABS_REF  
**Table type:** ACTIVITY  
**Primary key:** `LH_ABS_LOG_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALLING_PROGRAM_TXT` | VARCHAR(100) |  |  | Where the message was logged from |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 7 | `LH_ABS_LOG_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the table. The Primary Key. |
| 8 | `MESSAGE_SEQ` | DOUBLE | NOT NULL |  | If a message needs to be split over multiple rows (due to limited message_txt size) used to order the rows. |
| 9 | `MESSAGE_TXT` | VARCHAR(3000) |  |  | Log messages text to store |
| 10 | `MESSAGE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of message we are storing - 0 = Unknown, 1 = Info, 2 = Warning, 3 = Error |
| 11 | `PARENT_LOG_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the Parent LH_ABS_LOG_ID of a message or sequenced group of messages (sequence = 1) |
| 12 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | User id of the user running the application |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_SOURCE` | VARCHAR(100) |  |  | Script that created the message row |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `UPDT_TASK_TXT` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row (TEXT FORMAT) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_LOG_ID` | [LH_ABS_LOG](LH_ABS_LOG.md) | `LH_ABS_LOG_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [LH_ABS_LOG](LH_ABS_LOG.md) | `PARENT_LOG_ID` |

