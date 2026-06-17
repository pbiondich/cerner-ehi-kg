# BB_INVENTORY_AREA

> Reference of locations within the blood bank that keep inventory. Locations that stock blood to be dispensed.

**Description:** Blood Bank Inventory Area  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BB_BARCODE_ID` | DOUBLE | NOT NULL |  | Obsolete - This column is no longer being used. |
| 2 | `BB_DEVICE_TYPE_CD` | DOUBLE | NOT NULL |  |  |
| 3 | `BB_MONITORED_TEMP_HI` | DOUBLE |  |  |  |
| 4 | `BB_MONITORED_TEMP_LO` | DOUBLE |  |  |  |
| 5 | `BB_PROD_IND` | DOUBLE |  |  |  |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The service resource with which this inventory area is associated. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

