# ROI_INVOICE_CHARGE

> This table has fields like charges type and charges

**Description:** Roi Invoice charges has the charges for the invoice  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHARGES` | DOUBLE |  |  | This is the charges value |
| 7 | `CHARGE_RATE` | DOUBLE |  |  | The price per page or mile. |
| 8 | `CHARGE_RATE_FLAG` | DOUBLE | NOT NULL |  | Indicates what the charge rate applies to, 0 - None, 1 - Paper, 2 - Electronic, and 3 - Microfilm, 9 - mileage |
| 9 | `CHARGE_TYPE_CD` | DOUBLE | NOT NULL |  | This is the type of charge such as mileage or postage |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `END_NUMBER` | DOUBLE |  |  | The ending range for the charge tier. |
| 12 | `FLAT_CHARGE_IND` | DOUBLE |  |  | Indicates if the charge is a flat rate for the page range |
| 13 | `INVOICE_NUMBER` | DOUBLE | NOT NULL |  | This is a number assigned to this invoice |
| 14 | `REQUESTER_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the requester table. It is an internal system assigned number. |
| 15 | `REQUEST_NUMBER` | DOUBLE | NOT NULL |  | Request number |
| 16 | `ROI_INVOICE_CHARGE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the roi invoice charge table. It is an internal system assigned number. |
| 17 | `ROI_INVOICE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the roi invoice table. It is an internal system assigned number. |
| 18 | `START_NUMBER` | DOUBLE |  |  | The starting range for the charge tier. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

