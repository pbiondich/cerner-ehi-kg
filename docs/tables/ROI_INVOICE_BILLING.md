# ROI_INVOICE_BILLING

> This table contains billing and payment information for ROI Invoices.

**Description:** ROI Invoice Billing table.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_DT_TM` | DATETIME |  |  | The date the charged amount was billed |
| 7 | `CHARGED_AMOUNT` | DOUBLE | NOT NULL |  | Charged Amount |
| 8 | `CHECK_NUMBER` | DOUBLE |  |  | Check number |
| 9 | `CREDIT_CARD_CD` | DOUBLE | NOT NULL |  | credit card code |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `INVOICE_NUMBER` | DOUBLE | NOT NULL |  | This is a number assigned to this invoice |
| 12 | `PAYMENT_AMOUNT` | DOUBLE | NOT NULL |  | The amount to be paid. |
| 13 | `PAYMENT_DT_TM` | DATETIME |  |  | The Payment Date Time may provide the date and time that the invoice was actually paid when a two way accounts payable interface is present. |
| 14 | `PAYMENT_TYPE_CD` | DOUBLE | NOT NULL |  | The payment type (credit card, cash, check, etc.) |
| 15 | `REQUESTER_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the requester table. It is an internal system assigned number. |
| 16 | `REQUEST_NUMBER` | DOUBLE | NOT NULL |  | Request number |
| 17 | `ROI_INVOICE_BILLING_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ROI_Invoice_Billing table. It is an internal system assigned number. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

