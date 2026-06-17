# TRANS_ADMIT_NOTIFY_ALT

> The transaction admission notification alternate table stores an alternate/secondary patient admission notification transaction that is submitted to payers by the admission facility.

**Description:** Transaction Admission Notification Alternate  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PM_POST_DOC_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies each Person Management post document. |
| 2 | `REPORT_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a specific report on the report queue table. Matches up with the output_handle_id field. |
| 3 | `TRANSACTION_ADMIT_NOTIFY_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the TRANS_ADMIT_NOTIFY table. |
| 4 | `TRANSMISSION_STATUS_CD` | DOUBLE | NOT NULL |  | The current transmission status of the report. |
| 5 | `TRANSMIT_DT_TM` | DATETIME |  |  | The next valid time that the report can be transmitted based on time scheme criteria. |
| 6 | `TRANS_ADMIT_NOTIFY_ALT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the transaction_admit_notify_alt table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PM_POST_DOC_ID` | [PM_POST_DOC](PM_POST_DOC.md) | `PM_POST_DOC_ID` |
| `REPORT_QUEUE_ID` | [REPORT_QUEUE](REPORT_QUEUE.md) | `OUTPUT_HANDLE_ID` |
| `TRANSACTION_ADMIT_NOTIFY_ID` | [TRANSACTION_ADMIT_NOTIFY](TRANSACTION_ADMIT_NOTIFY.md) | `TRANSACTION_ADMIT_NOTIFY_ID` |

