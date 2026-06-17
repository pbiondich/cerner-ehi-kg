# BB_INV_DEVICE

> Defines the inventory devices used by the blood bank. This includes refrigerators and coolers to which blood is dispensed. In the future, this table will be used for any device in which blood is stored, even at the time the product is received.

**Description:** Inventory Device  
**Table type:** REFERENCE  
**Primary key:** `BB_INV_DEVICE_ID`  
**Columns:** 13  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BB_INV_DEVICE_ID` | DOUBLE | NOT NULL | PK | A system-generated number that ensures the uniqueness of every row on this table. |
| 6 | `DESCRIPTION` | VARCHAR(40) | NOT NULL |  | A textual description of the inventory device. |
| 7 | `DEVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of device - a refrigerator, cooler, etc. |
| 8 | `INTERFACE_FLAG` | DOUBLE |  |  | This indicates whether the device is interfaced to Millennium. 0 - Not Interfaced; 1 - Blood Track |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [BB_INV_DEVICE_R](BB_INV_DEVICE_R.md) | `BB_INV_DEVICE_ID` |
| [MODIFY_DEVICE](MODIFY_DEVICE.md) | `DEVICE_ID` |
| [PATIENT_DISPENSE](PATIENT_DISPENSE.md) | `DEVICE_ID` |
| [PATIENT_DISPENSE](PATIENT_DISPENSE.md) | `DISPENSE_COOLER_ID` |

