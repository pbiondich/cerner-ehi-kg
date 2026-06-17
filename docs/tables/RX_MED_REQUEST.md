# RX_MED_REQUEST

> Stores order request information (missing medication, scan failure, low quantity) for pharmacy to process

**Description:** Pharmacy Medication Request  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order associated to the medication request |
| 2 | `REQUEST_DT_TM` | DATETIME | NOT NULL |  | The time the medication request was initiated |
| 3 | `REQUEST_PRIORITY_CD` | DOUBLE | NOT NULL |  | The priority of the medication request |
| 4 | `REQUEST_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who requested the medication |
| 5 | `REQUEST_REASON_CD` | DOUBLE | NOT NULL |  | Describes why the medication request was initiated |
| 6 | `REQUEST_REASON_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Refers to an entry in long_text table which can additionally be provided by the user when a medication is request. Can be 0.0, if the user does not provide additional free text reason. |
| 7 | `REQUEST_TZ` | DOUBLE | NOT NULL |  | The time zone when the medication request was initiated |
| 8 | `RX_ACTION_CD` | DOUBLE | NOT NULL |  | Code to represent how the pharmacist acted on the med request (accept/decline/mark as duplicate) |
| 9 | `RX_ACTION_DT_TM` | DATETIME | NOT NULL |  | Date and time when a pharmacist acted on a medication request (accept/decline) |
| 10 | `RX_ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel ID of the user who acted on the medication request (accept/decline) |
| 11 | `RX_ACTION_TZ` | DOUBLE | NOT NULL |  | Time zone when a pharmacist acted on a medication request (accept/decline) |
| 12 | `RX_MED_REQUEST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_MED_REQUEST table. |
| 13 | `RX_REASON_CD` | DOUBLE | NOT NULL |  | Codified reason select by the pharmacist after acting on a medication request (accept/decline) |
| 14 | `RX_REASON_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Free-text comment entered by the pharmacist after acting on a medication request (accept/decline) |
| 15 | `RX_STATUS_CD` | DOUBLE | NOT NULL |  | Code for the status the medication request is currently in |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `REQUEST_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REQUEST_REASON_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `RX_ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RX_REASON_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

