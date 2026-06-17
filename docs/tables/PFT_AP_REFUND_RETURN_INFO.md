# PFT_AP_REFUND_RETURN_INFO

> This table is populated with the return information for refunds.

**Description:** PFT AP REFUND RETURN INFO  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHECK_AMT` | DOUBLE |  |  | The amount of the refund check The check could contain more than the related refund. |
| 6 | `CHECK_CASHED_DT_TM` | DATETIME |  |  | The date and time the CHECK CASHED status was received from the AP system. |
| 7 | `CHECK_CUT_DT_TM` | DATETIME |  |  | Date the check was cut for the refund. |
| 8 | `CHECK_NBR` | VARCHAR(100) |  |  | The check number of the refund. |
| 9 | `INVOICE_NBR` | VARCHAR(100) |  |  | The number of the invoice. |
| 10 | `MAILED_DT_TM` | DATETIME |  |  | Date the refund was mailed. |
| 11 | `PAYEE_NAME` | VARCHAR(100) |  |  | Name of the payee. |
| 12 | `PFT_AP_REFUND_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from the pft_ap_refund table. |
| 13 | `PFT_AP_REFUND_RETURN_INFO_ID` | DOUBLE | NOT NULL |  | UNIQUE IDENTIFIER. |
| 14 | `RECEIVED_DT_TM` | DATETIME |  |  | Date the refund was received. |
| 15 | `REFUND_TYPE_CD` | DOUBLE | NOT NULL |  | Refund type code. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `VOID_DT_TM` | DATETIME |  |  | The date and time the VOID status was received from the AP system. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_AP_REFUND_ID` | [PFT_AP_REFUND](PFT_AP_REFUND.md) | `PFT_AP_REFUND_ID` |

