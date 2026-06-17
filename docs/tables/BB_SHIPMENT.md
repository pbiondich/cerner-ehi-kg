# BB_SHIPMENT

> Contains the attributes of a shipment, including: shipment number, organization, order date, sent date, needed date, status, courier, and order placed by.

**Description:** Blood Bank Shipment Table  
**Table type:** ACTIVITY  
**Primary key:** `SHIPMENT_ID`  
**Columns:** 24  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COURIER_CD` | DOUBLE | NOT NULL | FK→ | Indicates the courier by which a shipment was sent. |
| 6 | `FROM_FACILITY_CD` | DOUBLE | NOT NULL |  | Identifies from which facility products were shipped. |
| 7 | `INVENTORY_AREA_CD` | DOUBLE | NOT NULL | FK→ | Inventory area to which the shipment is being sent. |
| 8 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Contains notes of type BBSHIPPING pertaining to the shipment. |
| 9 | `NEEDED_DT_TM` | DATETIME |  |  | The date and time the shipment is needed at the receiving organization. |
| 10 | `ORDER_DT_TM` | DATETIME |  |  | The date and time the shipment was ordered by an organization. |
| 11 | `ORDER_PLACED_BY` | VARCHAR(100) |  |  | The person who placed the shipment order. |
| 12 | `ORDER_PRIORITY_CD` | DOUBLE | NOT NULL |  | Indicates the order priority of the shipment. |
| 13 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from the ORGANIZATION table. Indicates the organization to which the shipment is being sent. |
| 14 | `OWNER_AREA_CD` | DOUBLE | NOT NULL | FK→ | Owner area to which the shipment is being sent. |
| 15 | `RECORDED_BY_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who created the new shipment. |
| 16 | `SHIPMENT_DT_TM` | DATETIME |  |  | The date and time the shipment was sent. |
| 17 | `SHIPMENT_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the BB_SHIPMENT table. |
| 18 | `SHIPMENT_NBR` | DOUBLE | NOT NULL |  | A uniquely assigned number given to the shipment. This is created by the BB_SHIPMENT_SEQ. |
| 19 | `SHIPMENT_STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicates the status of the shipment: Ordered, In Progress, Shipped, or Canceled 0 - Shipment has been ordered; 1 - The shpment is in progress; 2 - The shipment has been shipped or transferred; 3 - The shipment has been cancelled. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COURIER_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `INVENTORY_AREA_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OWNER_AREA_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BB_SHIP_CONTAINER](BB_SHIP_CONTAINER.md) | `SHIPMENT_ID` |
| [BB_SHIP_EVENT](BB_SHIP_EVENT.md) | `SHIPMENT_ID` |

