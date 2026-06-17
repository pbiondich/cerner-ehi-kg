# RX_PRINTER_LOCATION_R

> Relationship table between dispense categories and printers

**Description:** RX PRINTER LOCATION R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DENIAL_REPORT_DEVICE_CD` | DOUBLE | NOT NULL | FK→ | The printer to print the denial reports on. |
| 2 | `DEVICE_CD` | DOUBLE | NOT NULL | FK→ | Printer used for this location/dispense category combination. This value comes from the DEVICE table and is not a true CODE_VALUE. |
| 3 | `DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Dispense category key to table. |
| 4 | `LEAFLET_DEVICE_CD` | DOUBLE | NOT NULL |  | Leaflet Printer |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location key for printer assignment. |
| 6 | `REFILL_NOTIFY_DEVICE_CD` | DOUBLE | NOT NULL |  | Contains the device code for the refill notification printer. |
| 7 | `TRANS_NOTIFY_DEVICE_CD` | DOUBLE | NOT NULL |  | Transfer Notification Printer |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `VALIDATION_DEVICE_CD` | DOUBLE | NOT NULL |  | Validation printer |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DENIAL_REPORT_DEVICE_CD` | [DEVICE](DEVICE.md) | `DEVICE_CD` |
| `DEVICE_CD` | [DEVICE](DEVICE.md) | `DEVICE_CD` |
| `LOCATION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

