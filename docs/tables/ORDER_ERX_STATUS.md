# ORDER_ERX_STATUS

> Stores status and related information for each electronically routed prescription order

**Description:** Electronic Prescription Order Status  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MESSAGE_IDENT` | VARCHAR(100) |  |  | The identifier uniquely identifying the current NCPDP transaction. |
| 2 | `ORDER_ERX_STATUS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ORDER_ERX_STATUS table. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the order that references the original prescription. |
| 4 | `ORDER_RELATION_CD` | DOUBLE | NOT NULL |  | The relationship between the two orders. |
| 5 | `PHARMACY_IDENT` | VARCHAR(100) |  |  | The identifier of the pharmacy to whom the electronic prescription is being sent. |
| 6 | `PHARMACY_NOTE` | VARCHAR(1000) |  |  | The note or comment from the pharmacy related to the current order. |
| 7 | `REASON_CODES_TXT` | VARCHAR(2000) |  |  | List of reason codes comma delimited. |
| 8 | `REASON_CODE_BITMASK` | DOUBLE |  |  | The reason code if the order was denied/cancelled |
| 9 | `RELATED_ORDER_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the order which is related to the order that references the original prescription. |
| 10 | `RELATES_TO_MESSAGE_IDENT` | VARCHAR(100) |  |  | The identifier of the previous NCPDP transaction that the current message relates to. |
| 11 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the electronic prescription. |
| 12 | `TRANSACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of transaction that the current electronic prescription order is undergoing. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `RELATED_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

