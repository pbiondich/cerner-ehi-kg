# MM_PAYMENT

> Payment reference table that will store payment transactions

**Description:** mm payment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AMOUNT` | DOUBLE |  |  | Payment amount |
| 2 | `CHECK_NBR` | VARCHAR(40) |  |  | check number |
| 3 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 5 | `CREATE_ID` | DOUBLE | NOT NULL |  | User id of person which created this row |
| 6 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 7 | `FOREIGN_VOUCHER_NBR` | VARCHAR(40) |  |  | foreign voucher number |
| 8 | `MM_PAYMENT_COMMENT` | VARCHAR(255) |  |  | %payement% |
| 9 | `MM_PAYMENT_ID` | DOUBLE | NOT NULL |  | mm payment identifier |
| 10 | `PAYMENT_DT_TM` | DATETIME |  |  | payment date and time |
| 11 | `PAYMENT_METHOD` | VARCHAR(60) |  |  | payment method |
| 12 | `PAYMENT_TYPE` | VARCHAR(60) |  |  | PAYMENT TYPE |
| 13 | `PRSNL_NAME` | VARCHAR(100) |  |  | personnel name |
| 14 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL | FK→ | purchase order identifier |
| 15 | `REFERENCE_NBR` | VARCHAR(60) |  |  | reference number |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PURCHASE_ORDER_ID` | [PURCHASE_ORDER](PURCHASE_ORDER.md) | `PURCHASE_ORDER_ID` |

