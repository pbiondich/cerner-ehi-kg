# MM_XFI_PAYMENT

> Interface staging table to store the payment information for the Purchase orders. Data is moved from this table to MM_PAYMENT.

**Description:** Interface Payment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Determines the action to be taken for this row. (1-Update/Insert,...) |
| 2 | `AMOUNT` | DOUBLE |  |  | amount value |
| 3 | `BATCH_REF` | VARCHAR(100) |  |  | BATCH REFERENCE |
| 4 | `CHECK_NBR` | VARCHAR(40) |  |  | Cheque number for the payment. |
| 5 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context responsible for inserting this row on the table |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the record was created |
| 7 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 8 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 9 | `FOREIGN_VOUCHER_NBR` | VARCHAR(40) |  |  | foreign voucher number |
| 10 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 11 | `MM_PAYMENT_ID` | DOUBLE | NOT NULL |  | ID from mm_payment table to fetch the existing record for update. |
| 12 | `MM_XFI_PAYMENT_COMMENT` | VARCHAR(255) |  |  | mm xfi payment comment |
| 13 | `PAYMENT_DT_TM` | DATETIME |  |  | Determines the dt_tm when the payment occurred. |
| 14 | `PAYMENT_METHOD` | VARCHAR(60) |  |  | Identifies the method of payment (i.e. Cash, Check and Electronic Fund Transfer, etc.). |
| 15 | `PAYMENT_TYPE` | VARCHAR(60) |  |  | PAYMENT TYPE |
| 16 | `PROCESS_FLAG` | DOUBLE |  |  | Defines the state of the row in the upload process. |
| 17 | `PRSNL_NAME` | VARCHAR(100) |  |  | Name of the person who is processed the payment. |
| 18 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL | FK→ | The purchase order this payment is applied to. |
| 19 | `REFERENCE_NBR` | VARCHAR(60) |  |  | reference number |
| 20 | `SEGMENT_IDENTIFIER` | VARCHAR(10) |  |  | Indicates the upload type (item upload, item location upload, etc.) |
| 21 | `SEGMENT_VERSION` | VARCHAR(10) |  |  | Identifies the version of the upload interface |
| 22 | `TRANSACTION_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the MM_XFI_PAYMENT table. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PURCHASE_ORDER_ID` | [PURCHASE_ORDER](PURCHASE_ORDER.md) | `PURCHASE_ORDER_ID` |

