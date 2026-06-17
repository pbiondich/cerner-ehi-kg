# RX_REFILL_TRACK_HX

> Tracks details about requests for refills on existing prescriptions.

**Description:** Pharmacy Refill Tracking History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AGENT_FIRST_NAME` | VARCHAR(100) |  |  | First name of person acting on the prescriber's behalf |
| 3 | `AGENT_LAST_NAME` | VARCHAR(100) |  |  | Last name of person acting on the prescriber's behalf |
| 4 | `AUTH_STATUS_CD` | DOUBLE | NOT NULL |  | Status of a refill request. |
| 5 | `COMMENT_TXT` | VARCHAR(300) | NOT NULL |  | General comments by the person entering the refill request information. |
| 6 | `CONTACT_DT_TM` | DATETIME | NOT NULL |  | The date and time the physician was contacted. |
| 7 | `CONTACT_PRSNL_NAME` | VARCHAR(100) | NOT NULL |  | The person approving or denying the refill request on behalf of the physician. |
| 8 | `CREATED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that created this row. |
| 9 | `DENIED_REASON_TXT` | VARCHAR(1000) |  |  | Reason why the refill request was denied |
| 10 | `DIAGNOSIS_CODE_TXT` | VARCHAR(100) |  |  | Diagnosis code associated to the patient |
| 11 | `NOTIFY_DT_TM` | DATETIME | NOT NULL |  | Date and time the doctor was notified. |
| 12 | `ORDER_ID` | DOUBLE |  | FK→ | The original order for this prescription. |
| 13 | `REFILL_NBR` | DOUBLE | NOT NULL |  | The number of refills approved by the physician. |
| 14 | `REFILL_QTY` | DOUBLE | NOT NULL |  | The dispense quantity authorized for the refill. |
| 15 | `REQUEST_MSG_ID` | DOUBLE |  | FK→ | Identifies the request prescription message identifier that this row relates to |
| 16 | `RESPONSE_FREE_TXT` | VARCHAR(300) |  |  | Freetext response returned in the response message from a prescriber |
| 17 | `RXA_PRESCRIPTION_MSG_ID` | DOUBLE |  | FK→ | The unique identifier for the electronic prescription message associated to the external prescription |
| 18 | `RX_MSG_TRANS_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the transaction type of the message (ie. NEWRX, REFREQ, REFRES, ERROR, STATUS, VERIFY) |
| 19 | `RX_REFILL_TRACK_HX_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_REFILL_TRACK_HX table. |
| 20 | `STEP_TRACK_SEQ` | DOUBLE | NOT NULL |  | An incrementing number that identifies each refill action on a particular order. |
| 21 | `SUPPLY_DAYS` | DOUBLE |  |  | Number of days the prescription will supply |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `REQUEST_MSG_ID` | [RXA_PRESCRIPTION_MSG](RXA_PRESCRIPTION_MSG.md) | `RXA_PRESCRIPTION_MSG_ID` |
| `RXA_PRESCRIPTION_MSG_ID` | [RXA_PRESCRIPTION_MSG](RXA_PRESCRIPTION_MSG.md) | `RXA_PRESCRIPTION_MSG_ID` |

