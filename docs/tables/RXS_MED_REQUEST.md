# RXS_MED_REQUEST

> Stores missing ordered medications (e.g. not stocked, out of stock, low in quantity, etc.) that are requested from a fill location (e.g. pharmacy)

**Description:** RxStation Medication Request  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The time the medication was requested. |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order which requested the medication |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies the alert that was created for the medication request. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Identifies if the alert that was created for the medication request was from RXS_ALERT or RXS_FOREIGN_DEVICE_ALERT. |
| 5 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | The priority of the med request |
| 6 | `REASON_CD` | DOUBLE | NOT NULL |  | Describes why the med request was initiated. |
| 7 | `REASON_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Refers to an entry in long_text table which can additionally be provided by the user when a medication is requested. Can be 0.0, if user does not provide additional free text reason. |
| 8 | `REQUEST_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who requested the medication. |
| 9 | `RXS_MED_REQUEST_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RXS_MED_REQUEST table. |
| 10 | `RX_ACTION_CD` | DOUBLE | NOT NULL |  | Code to represent how the pharmacist acted on a med request (accept/decline/mark as duplicate) |
| 11 | `RX_ACTION_DT_TM` | DATETIME |  |  | Date and time when a pharmacist acted on a med request (accept/decline) |
| 12 | `RX_ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel ID of the user who acted on a med request (accept/decline). |
| 13 | `RX_ACTION_TZ` | DOUBLE |  |  | Time zone for the pharmacist acting on a med request (accept/decline) |
| 14 | `RX_REASON_CD` | DOUBLE | NOT NULL |  | Codified reason selected by the pharmacist after acting on a med request (accepting/declining) |
| 15 | `RX_REASON_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Free-text comment entered by the pharmacist after acting on a med request (accepting/declining) |
| 16 | `RX_STATUS_CD` | DOUBLE | NOT NULL |  | Code for the status the med request is in. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `REASON_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REQUEST_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RX_ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RX_REASON_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

