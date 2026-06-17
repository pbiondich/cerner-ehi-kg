# PHA_LEGAL_CONTROLS

> Pha Legal Controls - Stores state / legal status controls

**Description:** PHA LEGAL CONTROLS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONTROL_NBR_IND` | DOUBLE |  |  | Control nbr ind |
| 6 | `DISP_NOT_GREATER_RX_IND` | DOUBLE |  |  | This Column is OBSOLETE |
| 7 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | Code for Legal status code; part of key |
| 8 | `MAX_REFILLS` | DOUBLE |  |  | Maximum number of refills allowed. |
| 9 | `MAX_TRANSFERS` | DOUBLE |  |  | Maximum number of transfers allowed |
| 10 | `NEW_DISP_QTY_RX_QTY_IND` | DOUBLE |  |  | Value of one (1) indicates the New Prescription's Dispense Quantity must be less than or equal to the Prescription Quantity |
| 11 | `ORDER_EXPIRE_MONTHS` | DOUBLE |  |  | Number of anything (weeks, days, ,years, months) until the order will expire. |
| 12 | `ORDER_EXPIRE_UNITS_CD` | DOUBLE | NOT NULL |  | Units for Order expire time (weeks, days, months, years) |
| 13 | `PAT_ADDRESS_IND` | DOUBLE |  |  | Indicator (0,1) - Indicates whether or not the patient address is required for dispensing. |
| 14 | `PHYS_ADDRESS_IND` | DOUBLE |  |  | Indicator (0,1) - Indicates whether or not the physician address is required for dispensing. |
| 15 | `PHYS_CONTROL_NBR_IND` | DOUBLE |  |  | Physician Control Number Indicator |
| 16 | `PHYS_DEA_IND` | DOUBLE |  |  | Indicator (0,1) - Indicates whether or not the physician DEA # is required for dispensing. |
| 17 | `REFILL_DISP_QTY_REFILL_QTY_IND` | DOUBLE |  |  | Value of one (1) Indicates the Refill's Dispense Quantity must be less than or equal to the Refill Quantity |
| 18 | `REFILL_QTY_RX_QTY_IND` | DOUBLE |  |  | Value of one (1) indicates the New Prescription's Refill Quantity must be less than or equal to the Prescription Quantity. This field replaces the disp_not_greater_rx_ind. |
| 19 | `STATE_CD` | DOUBLE | NOT NULL |  | State for the control |
| 20 | `UNFILLED_EXPIRE_DAYS` | DOUBLE |  |  | How many days can order be unfilled before it expires |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

