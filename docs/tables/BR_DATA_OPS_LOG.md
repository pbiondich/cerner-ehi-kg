# BR_DATA_OPS_LOG

> BEDROCK OPS LOG DATA

**Description:** BEDROCK DATA OPS LOG  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `END_DT_TM` | DATETIME |  |  | Time process completed |
| 2 | `ERROR_MSG` | VARCHAR(1000) |  |  | Holds error message |
| 3 | `EXCEPTION_IND` | DOUBLE |  |  | Indicates table is not to participate in client fill process |
| 4 | `LOGFILE_NAME` | VARCHAR(40) |  |  | Name of log file, if there's an error |
| 5 | `RUN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to data_data_ops |
| 6 | `SRC_ROW_CNT` | DOUBLE |  |  | Number of rows selected from start data |
| 7 | `START_DT_TM` | DATETIME |  |  | Time process started |
| 8 | `STATUS` | VARCHAR(30) |  |  | Holds values of COMPLETE, READY_TO_RUN, ERROR, RUNNING |
| 9 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of table being processed |
| 10 | `TGT_ROWS_WRITTEN` | DOUBLE |  |  | Number of rows inserted for client |
| 11 | `TTL_SRC_TBL_ROWS` | DOUBLE |  |  | DB Stats for individual table |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RUN_ID` | [BR_DATA_OPS](BR_DATA_OPS.md) | `RUN_ID` |

