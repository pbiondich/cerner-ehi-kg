# CMT_IMPORT_LOG_MSG

> Contains log information for CMT Content loads

**Description:** Community import log message  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CMT_IMPORT_LOG_ID` | DOUBLE | NOT NULL | FK→ | community import log message identifierColumn |
| 2 | `CMT_IMPORT_LOG_MSG_ID` | DOUBLE | NOT NULL |  | community import log message identifierColumn |
| 3 | `END_DT_TM` | DATETIME |  |  | The time the import ended |
| 4 | `LOG_INSTANCE` | DOUBLE | NOT NULL |  | Package from which load was run. |
| 5 | `LOG_MESSAGE` | VARCHAR(250) | NOT NULL |  | log messageColumn |
| 6 | `LOG_SEQ` | DOUBLE | NOT NULL |  | log sequenceColumn |
| 7 | `LOG_STATUS_FLAG` | DOUBLE | NOT NULL |  | Current Status of Import. 0 = unknown; 1 = Running; 2 = Success; 3 = Failed; 4 = Warning. |
| 8 | `START_DT_TM` | DATETIME |  |  | The time the import started |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CMT_IMPORT_LOG_ID` | [CMT_IMPORT_LOG](CMT_IMPORT_LOG.md) | `CMT_IMPORT_LOG_ID` |

