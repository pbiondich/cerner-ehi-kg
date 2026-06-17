# TRANSACTION_ADMIT_NOTIFY

> This table stores information to track admission notification history for patients.

**Description:** Transaction Admission Notification  
**Table type:** ACTIVITY  
**Primary key:** `TRANSACTION_ADMIT_NOTIFY_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIN_REF_NUM` | VARCHAR(50) |  |  | An additional reference number returned by the payer for the notification. Different payers will return this number under different scenarios. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date and time of the patient's admission that was sent to the payer. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related encounter. If populated, admission notification was submitted as part of the given encounter. |
| 4 | `ENCNTR_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related relationship between encounter and health plan for which the admission notification transaction was submitted. |
| 5 | `NOTIFY_RECEIPT_NUM` | VARCHAR(50) |  |  | An additional reference number returned by the payer for the notification. Different payers will return this number under different scenarios. |
| 6 | `NOTIFY_STATUS_CD` | DOUBLE | NOT NULL |  | The payer specified status of the notification. Returned by the payer that was notified of the admission. |
| 7 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The facility organization that admitted the patient. Identifying information for the facility that was sent to the payer. |
| 8 | `PAYER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related organization for the payer to whom this transaction was submitted. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient whose admission notification was submitted to the payer via this transaction. |
| 10 | `REPLY_DT_TM` | DATETIME |  |  | The date and time the admission notification transaction response was received inbound. |
| 11 | `REVIEW_IDENT_NUM` | VARCHAR(50) |  |  | The primary reference number returned by the payer for the notification. Different payers will return this number under different scenarios. |
| 12 | `SENT_DT_TM` | DATETIME |  |  | The date and time the admission notification transaction was sent outbound. |
| 13 | `SUBMITTER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the personnel that submitted the transaction outbound. |
| 14 | `TRANSACTION_ADMIT_NOTIFY_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies information used to track admission notification history for patients. |
| 15 | `TRANSACTION_SOURCE_IDENT` | VARCHAR(50) | NOT NULL |  | The transaction identifier assigned by transaction services. Used to retrieve the transaction status and response details. |
| 16 | `TRANSACTION_STATUS_CD` | DOUBLE | NOT NULL |  | The high level status of the transaction. |
| 17 | `TRANS_SUB_STATUS_CD` | DOUBLE | NOT NULL |  | The optionally provided detail about the status of the transaction. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_PLAN_RELTN_ID` | [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `ENCNTR_PLAN_RELTN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PAYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SUBMITTER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [TRANSACTION_ADMIT_ERROR](TRANSACTION_ADMIT_ERROR.md) | `TRANSACTION_ADMIT_NOTIFY_ID` |
| [TRANS_ADMIT_NOTIFY_ALT](TRANS_ADMIT_NOTIFY_ALT.md) | `TRANSACTION_ADMIT_NOTIFY_ID` |

