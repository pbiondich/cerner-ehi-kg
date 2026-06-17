# RX_LOC_RESOURCE_RELTN

> Location to pharmacy service resource relation.

**Description:** Pharmacy Location Resource Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | DEFAULT_IND |
| 6 | `DISP_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Dispense event type codes (e.g. Fill list, initial dose, extra dose) |
| 7 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location codes (e.g. nurse units, facilities, rooms) |
| 8 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Pharmacy type codes (e.g. INPATIENT, AMBULATORY) |
| 9 | `PRN_IND` | DOUBLE | NOT NULL |  | Default value is 0, value of 1 indicates the routing is for use with PRN orders. PRN(latin) - pro re nata (as the situation demands; as needed). |
| 10 | `RX_LOC_RESOURCE_RELTN_ID` | DOUBLE | NOT NULL |  | Unique identifier for rows on the table. (primary key) |
| 11 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Priority sequence for evaluating the resource list for a given location. |
| 12 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Service resource codes (e.g. Main Pharmacy, Dispensing robot, Pyxis machine) |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

