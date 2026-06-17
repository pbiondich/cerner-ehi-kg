# CQM_ROPRESULTS_QUE

> Result information from POC instruments

**Description:** CQM ROPRESULTS QUE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CLASS` | VARCHAR(15) |  |  | Represents the service resource cd that generated the resultsColumn |
| 3 | `CONTRIBUTOR_EVENT_DT_TM` | DATETIME |  |  | not used by mdiColumn |
| 4 | `CONTRIBUTOR_ID` | DOUBLE | NOT NULL |  | Represents what server inserted the record.Column |
| 5 | `CONTRIBUTOR_REFNUM` | VARCHAR(48) | NOT NULL |  | The patient identifier for the results.Column |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | when the record was createdColumn |
| 7 | `CREATE_RETURN_FLAG` | DOUBLE |  |  | not applicable to mdiColumn |
| 8 | `CREATE_RETURN_TEXT` | VARCHAR(132) |  |  | not used by mdiColumn |
| 9 | `DEBUG_IND` | DOUBLE |  |  | not used by mdiColumn |
| 10 | `MESSAGE` | LONGBLOB |  |  | results received from an instrumentColumn |
| 11 | `MESSAGE_LEN` | DOUBLE | NOT NULL |  | length of the message fieldColumn |
| 12 | `PARAM_LIST_IND` | DOUBLE |  |  | not used by mdiColumn |
| 13 | `PRIORITY` | DOUBLE | NOT NULL |  | not used by mdiColumn |
| 14 | `PROCESS_STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of the recordColumn |
| 15 | `QUEUE_ID` | DOUBLE | NOT NULL |  | table keyColumn |
| 16 | `SUBTYPE` | VARCHAR(15) |  |  | not usedColumn |
| 17 | `SUBTYPE_DETAIL` | VARCHAR(15) |  |  | not usedColumn |
| 18 | `TRIG_CREATE_END_DT_TM` | DATETIME |  |  | not usedColumn |
| 19 | `TRIG_CREATE_START_DT_TM` | DATETIME |  |  | not usedColumn |
| 20 | `TRIG_MODULE_IDENTIFIER` | VARCHAR(16) |  |  | not usedColumn |
| 21 | `TYPE` | VARCHAR(15) |  |  | not usedColumn |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `VERBOSITY_FLAG` | DOUBLE |  |  | not usedColumn |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

