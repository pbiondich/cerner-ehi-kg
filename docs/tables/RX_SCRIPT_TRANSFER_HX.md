# RX_SCRIPT_TRANSFER_HX

> Used to track prescription transfers in to and out of pharmacies in the PharmNet System.

**Description:** Pharmacy Prescription Transfer History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LAST_FILL_QTY` | DOUBLE | NOT NULL |  | The quantity of the last fill (represented by last_refill_dt_tm) for the prescription. |
| 2 | `LAST_REFILL_DT_TM` | DATETIME |  |  | The Last Refill Date and Time of the prescription at the time of the transfer. |
| 3 | `LAST_REFILL_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order ID to which this transfer record is associated. |
| 5 | `PHARMACIST_ID` | DOUBLE | NOT NULL | FK→ | The Person (personnel) ID of the pharmacists doing the transfer. |
| 6 | `QTY_REMAINING` | DOUBLE | NOT NULL |  | Quantity remaining of the prescription at the time of transfer. |
| 7 | `REFILLS_REMAINING` | DOUBLE | NOT NULL |  | Refills remaining of the prescription at the time of transfer. |
| 8 | `REFILL_QTY` | DOUBLE | NOT NULL |  | Refill quantity of the prescription at the time of transfer. |
| 9 | `RX_DATE_DT_TM` | DATETIME | NOT NULL |  | Original Rx Date of the prescription at the time of transfer. |
| 10 | `RX_DATE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `RX_NUM_S` | VARCHAR(20) | NOT NULL |  | Original Rx Number of the prescription at the time of transfer. |
| 12 | `RX_QTY` | DOUBLE | NOT NULL |  | Original Rx Quantity of the prescription at the time of transfer. |
| 13 | `RX_TRANSFER_HX_ID` | DOUBLE | NOT NULL |  | Unique ID for this record |
| 14 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Service Resource CD for the order tied to this record. |
| 15 | `SIG` | VARCHAR(250) | NOT NULL |  | The Sig (directions for taking) of the prescription at the time of the transfer. |
| 16 | `TOTAL_REFILLS` | DOUBLE | NOT NULL |  | Total number of refills of the prescription at the time of the transfer. |
| 17 | `TRANSFER_DT_TM` | DATETIME | NOT NULL |  | Transfer Date and Time of the prescription |
| 18 | `TRANSFER_IN_IND` | DOUBLE | NOT NULL |  | Value of 1 is Transfer In record. Value of 0 is Transfer Out record. |
| 19 | `TRANSFER_TZ` | DOUBLE | NOT NULL |  | Time zone for the transfer_dt_tm |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `XFER_ORDER_ID` | DOUBLE | NOT NULL | FK→ | The new order's order id created from transferring this order. |
| 26 | `XFER_PHARMACIST_ID` | DOUBLE | NOT NULL | FK→ | The internal pharmacist's personnel ID of the pharmacist transferring out the internal prescription. |
| 27 | `XFER_PHARMACIST_NAME` | VARCHAR(100) |  |  | The external pharmacist's name transferring in or out the prescription. |
| 28 | `XFER_RX_TRANSFER_CD` | DOUBLE | NOT NULL | FK→ | The external pharmacy the prescription was transferred to/from. |
| 29 | `XFER_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The internal service resource code the prescription was transferred to/from. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PHARMACIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `XFER_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `XFER_PHARMACIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `XFER_RX_TRANSFER_CD` | [PHA_RX_TRANSFERS](PHA_RX_TRANSFERS.md) | `RX_TRANSFER_CD` |
| `XFER_SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

