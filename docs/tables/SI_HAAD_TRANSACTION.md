# SI_HAAD_TRANSACTION

> Table to keep track of the current status of HAAD transactions ( Health Authority - Abu Dhabi )

**Description:** SI HAAD TRANSACTIONS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLETED_DT_TM` | DATETIME |  |  | The date and time the transaction completed processing. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was originally created. |
| 3 | `RETRIEVE_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Link to the CQM queue_id of the retrieve |
| 4 | `SENDING_FACILITY_IDENT` | VARCHAR(75) |  |  | HAAD license number of sending facility |
| 5 | `SENDING_LOCATION_CD` | DOUBLE | NOT NULL |  | Code value denoting the sending facility |
| 6 | `SI_HAAD_FILE_DOWNLOAD_ID` | DOUBLE | NOT NULL | FK→ | Link to the SI_HAAD_FILE_DOWNLOAD row of the downloaded response |
| 7 | `SI_HAAD_TRANSACTION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 8 | `STATUS_CD` | DOUBLE | NOT NULL |  | Code value denoting the current state of the transaction. |
| 9 | `STATUS_TEXT` | VARCHAR(50) |  |  | Textual detail about the current status |
| 10 | `SUBMIT_MSGLOG_ID` | DOUBLE |  | FK→ | Link to the si_message_log row of the upload request |
| 11 | `SUBMIT_RESP_MSGLOG_ID` | DOUBLE |  | FK→ | Link to the si_message_log row of the uploaded request Response |
| 12 | `TRANSACTION_IDENT` | VARCHAR(25) | NOT NULL |  | Identifier assigned by the health provider to identify the transaction. |
| 13 | `TRANSACTION_NBR` | DOUBLE | NOT NULL |  | TRANSACTION_NBR from the RX_CLAIMS table. |
| 14 | `TRANSACTION_SUBTYPE` | VARCHAR(25) |  |  | Subtype of transaction being sent outbound |
| 15 | `TRANSACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of transaction being sent outbound |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `UPLOAD_DT_TM` | DATETIME |  |  | Date and time of the upload |
| 22 | `UPLOAD_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Link to the CQM queue_id of the upload |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RETRIEVE_QUEUE_ID` | [CQM_OENINTERFACE_QUE](CQM_OENINTERFACE_QUE.md) | `QUEUE_ID` |
| `SI_HAAD_FILE_DOWNLOAD_ID` | [SI_HAAD_FILE_DOWNLOAD](SI_HAAD_FILE_DOWNLOAD.md) | `SI_HAAD_FILE_DOWNLOAD_ID` |
| `SUBMIT_MSGLOG_ID` | [SI_MESSAGE_LOG](SI_MESSAGE_LOG.md) | `SI_MESSAGE_LOG_ID` |
| `SUBMIT_RESP_MSGLOG_ID` | [SI_MESSAGE_LOG](SI_MESSAGE_LOG.md) | `SI_MESSAGE_LOG_ID` |
| `UPLOAD_QUEUE_ID` | [CQM_OENINTERFACE_QUE](CQM_OENINTERFACE_QUE.md) | `QUEUE_ID` |

