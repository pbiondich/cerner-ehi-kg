# TRANSACTION_ADMIT_ERROR

> The table stores information to track admission notification error history for patients.

**Description:** Admission Transaction Notification Error  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ERROR_LOCATION_CD` | DOUBLE | NOT NULL |  | The location code describes where the error occurred while processing the eligibility transaction. |
| 2 | `FOLLOW_UP_ACTION_CD` | DOUBLE | NOT NULL |  | This code instructs the recipient of the admission notification response about what action needs to be taken. |
| 3 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This is the identifier of the long_text table row containing the error's text message. |
| 4 | `REJECT_REASON_CD` | DOUBLE | NOT NULL |  | This code defines the reason why the transaction was unable to be processed successfully. |
| 5 | `TRANSACTION_ADMIT_ERROR_ID` | DOUBLE | NOT NULL |  | Admission Notification transaction error history data |
| 6 | `TRANSACTION_ADMIT_NOTIFY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related transaction admission notification. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `TRANSACTION_ADMIT_NOTIFY_ID` | [TRANSACTION_ADMIT_NOTIFY](TRANSACTION_ADMIT_NOTIFY.md) | `TRANSACTION_ADMIT_NOTIFY_ID` |

