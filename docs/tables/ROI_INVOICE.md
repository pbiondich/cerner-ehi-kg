# ROI_INVOICE

> This table hold fields like invoice number and total charges

**Description:** ROI INVOICE TABLE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BALANCE` | DOUBLE |  |  | This is the balance due for this invoice |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CHARGE_COMMENT` | VARCHAR(255) |  |  | This includes any comments for charge adjustments. |
| 8 | `COST_PER_PAGE` | DOUBLE |  |  | This is the cost per page charged on this invoice |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `INITIAL_BILL_DT_TM` | DATETIME |  |  | This is the date and time of the first billing. |
| 11 | `INVOICE_COMMENTS` | VARCHAR(255) |  |  | These are comments to be included on invoices. |
| 12 | `INVOICE_NUMBER` | DOUBLE |  |  | This is a number assigned to this invoice |
| 13 | `NUM_PAGES_COPIED` | DOUBLE |  |  | This is the number of pages copied |
| 14 | `PRINT_CHARGE_COMMENT_IND` | DOUBLE | NOT NULL |  | Indicates if charge comments should be printed on invoice. |
| 15 | `PRINT_INVOICE_COMMENTS_IND` | DOUBLE | NOT NULL |  | Indicates if invoice comments should be printed. |
| 16 | `REQUESTER_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the Requester table. It is an internal system assigned number. |
| 17 | `REQUESTER_SOURCE_CD` | DOUBLE | NOT NULL |  | requester source code |
| 18 | `REQUEST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the roi_request table. It is an internal system assigned number. |
| 19 | `REQUEST_NUMBER` | DOUBLE | NOT NULL |  | Request number |
| 20 | `ROI_INVOICE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the roi_invoice table. It is an internal system assigned number. |
| 21 | `TOTAL_ADJUSTED_CHARGES` | DOUBLE |  |  | This is the actual total of charges for the invoice including any adjustments. |
| 22 | `TOTAL_ADJUSTED_IND` | DOUBLE | NOT NULL |  | Indicates if the total adjusted charges has been modified from the total charges |
| 23 | `TOTAL_CHARGES` | DOUBLE |  |  | This is the total Charges for this invoice |
| 24 | `TOTAL_ELECTRONIC_PAGES` | DOUBLE | NOT NULL |  | This is the total number of electronic pages retrieved for the invoice. |
| 25 | `TOTAL_MICROFILM_PAGES` | DOUBLE | NOT NULL |  | This is the total number of microfilm pages retrieved for the invoice. |
| 26 | `TOTAL_PAID` | DOUBLE | NOT NULL |  | this is the total paid on this invoice |
| 27 | `TOTAL_PAPER_PAGES` | DOUBLE |  |  | This is the total number of paper pages retrieved for the invoice. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

