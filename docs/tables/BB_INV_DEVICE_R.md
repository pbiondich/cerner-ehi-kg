# BB_INV_DEVICE_R

> Defines the relationship between the inventory devices stored on the inventory_device table and thelocation, service resource, or inventory area with which it is associated.

**Description:** Blood Bank Inventory Device Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BB_INV_DEVICE_ID` | DOUBLE | NOT NULL | FK→ | The system-generated number that uniquely identifies every row on the bb_inv_device table. It exists on this table to link the actual inventory device to each relationship which exists for it (ex. location "SURG" has device "Refrig #1" associated with it). |
| 6 | `BB_INV_DEVICE_R_ID` | DOUBLE | NOT NULL |  | A system-generated number that uniquely identifies every row on this table. |
| 7 | `DEVICE_R_CD` | DOUBLE | NOT NULL |  | The code value that identifies the place that is associated with this inventory device. Currently this is only used for dispensed products dispensed to a certain location (nursing station). This column defines the location with which this device is associated. |
| 8 | `DEVICE_R_TYPE_CD` | DOUBLE | NOT NULL |  | Defines what type of relationship applies to this inventory device and item (blood bank inventory area, service resource, or nursing station location). |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BB_INV_DEVICE_ID` | [BB_INV_DEVICE](BB_INV_DEVICE.md) | `BB_INV_DEVICE_ID` |

