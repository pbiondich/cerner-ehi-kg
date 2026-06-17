# SA_REF_DEVICE

> BMDI Devices that are used in Anesthesia

**Description:** Anesthesia Reference Device  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_DEVICE_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `MONITORED_DEVICE_ID` | DOUBLE | NOT NULL | FK→ | Key to monitored device for this row |
| 6 | `SA_REF_DEVICE_ID` | DOUBLE | NOT NULL | PK | Primary Key for table |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MONITORED_DEVICE_ID` | [BMDI_MONITORED_DEVICE](BMDI_MONITORED_DEVICE.md) | `MONITORED_DEVICE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SA_REF_CAT_DEVICE](SA_REF_CAT_DEVICE.md) | `SA_REF_DEVICE_ID` |
| [SA_REF_EXCLUDE_DEVICE](SA_REF_EXCLUDE_DEVICE.md) | `SA_REF_DEVICE_ID` |

