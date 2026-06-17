# SN_CHARGE_QUEUE

> SurgiNet Charge Queue Table

**Description:** SurgiNet Charge Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AREA_CD` | DOUBLE | NOT NULL |  | The surgical area associated with the transaction. |
| 2 | `BLOCKED_DT_TM` | DATETIME |  |  | The date and time the transaction was last blocked. |
| 3 | `BLOCKED_IND` | DOUBLE | NOT NULL |  | Indicates block status (0 = False, 1 = True). |
| 4 | `BLOCKED_REASON_FLAG` | DOUBLE | NOT NULL |  | Identifies the reason of why the pending charge is being blocked (0 = unknown, 1 = incomplete data, 2 = user, 3 = sync constraint, 4 = other) |
| 5 | `DELAY_REASON` | VARCHAR(250) |  |  | The reason why the transaction was last delayed. |
| 6 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The document type associated with the transaction. This is the second field of the unique identifier on the Table. |
| 7 | `FAILURE_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 when the transaction fails. |
| 8 | `FAILURE_DT_TM` | DATETIME |  |  | The date and time the transaction last failed. |
| 9 | `HOLD_BY_ID` | DOUBLE | NOT NULL |  | The personnel ID who requested to hold the transaction. |
| 10 | `HOLD_DT_TM` | DATETIME |  |  | The date and time the transaction was held. |
| 11 | `HOLD_REASON` | VARCHAR(250) |  |  | The reason why the transaction is being held. |
| 12 | `PROCESS_IND` | DOUBLE | NOT NULL |  | Indicates whether this transaction type is being processed |
| 13 | `RECHARGES_IND` | DOUBLE | NOT NULL |  | Indicates if the transaction was requested to be recharged (0 = False, 1 = True) |
| 14 | `RELEASE_BY_ID` | DOUBLE | NOT NULL |  | Identifies the personnel ID of the personnel releasing the blocked pending charge. |
| 15 | `RELEASE_DT_TM` | DATETIME |  |  | Identifies the date and time of when the blocked pending charge was released. |
| 16 | `RELEASE_REASON` | VARCHAR(250) |  |  | Identifies the reason of releasing the blocked pending charge. |
| 17 | `SUBMITTED_BY_ID` | DOUBLE | NOT NULL |  | The personnel ID who submitted the transaction. |
| 18 | `SUBMITTED_DT_TM` | DATETIME |  |  | The date and time the transaction was last submitted. |
| 19 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | The surgical case associated with the transaction. This is the first field of the unique identifier on the Table. |
| 20 | `TRANS_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | The type of transaction. This is the third field of the unique identifier on the Table. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

