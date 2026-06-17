# INVOICE_LINE_ITEM

> Holds all line items for an invoice.

**Description:** Invoice Line Item  
**Table type:** ACTIVITY  
**Primary key:** `INVOICE_LINE_ITEM_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUYER_ID` | DOUBLE | NOT NULL |  | Buyer ID of the Buyer |
| 2 | `CHECKED_IND` | DOUBLE |  |  | Indicates whether this line is included on this invoice. |
| 3 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | This cost center for which this line will be charged. |
| 4 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was was inserted. |
| 6 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 7 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 8 | `INVOICE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the invoice table. |
| 9 | `INVOICE_LINE_ITEM_ID` | DOUBLE | NOT NULL | PK | The identifier assigned to line item on an invoice |
| 10 | `LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to line_item table. |
| 11 | `MATCHED_IND` | DOUBLE |  |  | This field determines if the line has been matched to an invoice. |
| 12 | `PO_LINE_NBR` | DOUBLE |  |  | The line number for this line from the purchase order. |
| 13 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the line. |
| 14 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | The sub-account for which to charge this item. |
| 15 | `TRANSMIT_CD` | DOUBLE |  |  | Indicates the status of transmission to an AP system. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | `INVOICE_ID` |
| `LINE_ITEM_ID` | [LINE_ITEM](LINE_ITEM.md) | `LINE_ITEM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_AP_LOG_LINE_HMW](MM_AP_LOG_LINE_HMW.md) | `INVOICE_LINE_ITEM_ID` |

