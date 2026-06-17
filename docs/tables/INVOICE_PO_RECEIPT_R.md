# INVOICE_PO_RECEIPT_R

> This table describes which receipts were invoiced for a specific invoice.

**Description:** Invoice - PO Receipt Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was was inserted. |
| 3 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 4 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 5 | `INVOICE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to invoice table. |
| 6 | `PO_RECEIPT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to po_receipt table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | `INVOICE_ID` |
| `PO_RECEIPT_ID` | [PO_RECEIPT](PO_RECEIPT.md) | `PO_RECEIPT_ID` |

