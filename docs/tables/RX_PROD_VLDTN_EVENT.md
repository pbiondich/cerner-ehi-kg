# RX_PROD_VLDTN_EVENT

> Stores the history of product validation transactions for workflow monitor statuses.

**Description:** PharmNet Product Validation Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BARCODE_TXT` | VARCHAR(50) |  |  | The information on the barcode that was scanned. |
| 2 | `CONTENT_MATCH_CD` | DOUBLE | NOT NULL |  | Identifies how the product was found in the system. |
| 3 | `DISP_ITEM_ID` | DOUBLE | NOT NULL |  | The dispense product being validated. |
| 4 | `DISP_LABEL_DESCRIPTION_TXT` | VARCHAR(100) |  |  | Information on the label of the dispense product being validated. |
| 5 | `DISP_MANF_DRUG_IDENTIFIER` | VARCHAR(100) |  |  | Identifies the dispense manufacturer being validated. |
| 6 | `DISP_MANF_ITEM_ID` | DOUBLE | NOT NULL |  | Identifies the dispense manufacturer item being validated. |
| 7 | `DISP_VLDTN_QTY` | DOUBLE | NOT NULL |  | The number of scans expected. |
| 8 | `DUPLICATE_PROD_IND` | DOUBLE | NOT NULL |  | Indicates if the user was prompted with a duplicate product list. |
| 9 | `ENTRY_METHOD_CD` | DOUBLE | NOT NULL |  | Identifies the entry method utilized for the product validation event. |
| 10 | `FORMULARY_PROD_IND` | DOUBLE | NOT NULL |  | Indicates if the product was found in the formulary. |
| 11 | `MANUAL_QTY_IND` | DOUBLE | NOT NULL |  | Identifies whether the user manually set the scan quantity. |
| 12 | `MESSAGE_CD` | DOUBLE | NOT NULL |  | Identifies the message displayed for the product validation event. |
| 13 | `OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason a user selects to override a validation event. |
| 14 | `QTY_PER_SCAN_NBR` | DOUBLE | NOT NULL |  | The multiplier factor for the scanned product. |
| 15 | `QTY_PER_SCAN_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for the scanned product relative to the value in qty_per_scan_nbr. |
| 16 | `RX_PROD_VLDTN_EVENT_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RX_PROD_VLDTN_EVENT table. |
| 17 | `RX_VERIFY_IND` | DOUBLE | NOT NULL |  | Indicates if the scan was performed by a user with RXVERIFY privileges. |
| 18 | `RX_WORKFLOW_STS_ID` | DOUBLE | NOT NULL | FK→ | The workflow event this validation pertains to. Foreign key to the RX_WORKFLOW_STS table. |
| 19 | `SCAN_ITEM_ID` | DOUBLE | NOT NULL |  | Identifies the product being used to compare to. |
| 20 | `SCAN_LABEL_DESCRIPTION_TXT` | VARCHAR(100) |  |  | Label description for the scanned product. |
| 21 | `SCAN_MANF_DRUG_IDENTIFIER` | VARCHAR(100) |  |  | Drug identifier for the scanned product. |
| 22 | `SCAN_MANF_ITEM_ID` | DOUBLE | NOT NULL |  | Identifies the manufacturer being used to compare to. |
| 23 | `SCAN_QTY` | DOUBLE | NOT NULL |  | Identifies the quantity being either scanned by a user or entered by a user. The manual_qty_cd field will flag whether or not the user entered a scan quantity amount. |
| 24 | `TOTAL_DOSE_NBR` | DOUBLE | NOT NULL |  | The total dose of the event when a product is scanned. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 30 | `VLDTN_EVENT_DT_TM` | DATETIME |  |  | Identifies when the product validation event occurred. |
| 31 | `VLDTN_EVENT_TZ` | DOUBLE | NOT NULL |  | Time Zone associated with the column vldtn_event_dt_tm. |
| 32 | `VLDTN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person performing the product validation event. |
| 33 | `VLDTN_STS_CD` | DOUBLE | NOT NULL |  | Identifies the validation status of the product validation event. |
| 34 | `WORKFLOW_STS_CD` | DOUBLE | NOT NULL |  | Identifies the status of the workflow sequence associated to an order's dispense. |
| 35 | `WORKFLOW_STS_SEQ` | DOUBLE | NOT NULL |  | An incrementing number for a combination of rx_workflow_sts_id and workflow_sts_cd. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RX_WORKFLOW_STS_ID` | [RX_WORKFLOW_STS](RX_WORKFLOW_STS.md) | `RX_WORKFLOW_STS_ID` |
| `VLDTN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

