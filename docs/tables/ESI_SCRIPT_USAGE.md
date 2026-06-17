# ESI_SCRIPT_USAGE

> This table stores the scripts, and their duration, executed by the ESI Server.

**Description:** ESI Script Usage  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time message was created. |
| 3 | `ELAPSED_TIME` | DOUBLE | NOT NULL |  | Length of time spent executing the given script.The time in ms for script execution. |
| 4 | `ESI_LOG_ID` | DOUBLE | NOT NULL | FK→ | ESI_LOG_ID associated to the message that used the listed scripts. |
| 5 | `ESI_SCRIPT_USAGE_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 6 | `MESSAGE_TYPE` | VARCHAR(20) | NOT NULL |  | The message type used to generate the message associated to this script. |
| 7 | `MESSGE_TRIGGER` | VARCHAR(20) | NOT NULL |  | The message trigger used to generate the message associated to this script. |
| 8 | `SCRIPT_NAME` | VARCHAR(40) | NOT NULL |  | Name of the executed script. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ESI_LOG_ID` | [ESI_LOG](ESI_LOG.md) | `ESI_LOG_ID` |

