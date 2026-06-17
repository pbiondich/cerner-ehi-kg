# BB_SHIP_CONTAINER

> This table holds all containers and it's attributes associated with shipments from the BB_SHIPMENT table.

**Description:** BB Ship Container Table  
**Table type:** ACTIVITY  
**Primary key:** `CONTAINER_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONTAINER_CONDITION_CD` | DOUBLE | NOT NULL | FK→ | Contains the condition of the container (i.e. wet ice or room temperature). |
| 6 | `CONTAINER_ID` | DOUBLE | NOT NULL | PK | Unique identifier for the BB_SHIP_CONTAINER table |
| 7 | `CONTAINER_NBR` | DOUBLE | NOT NULL |  | Sequential number given to each container in a specific shipment. |
| 8 | `CONTAINER_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Contains the type of container used (i.e. box or cooler). |
| 9 | `SHIPMENT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from the BB_SHIPMENT table. Indicates which shipment the container is part of. |
| 10 | `TEMPERATURE_DEGREE_CD` | DOUBLE | NOT NULL |  | Indicates the shipment temperature degree unit of measure associated with the container. |
| 11 | `TEMPERATURE_VALUE` | DOUBLE | NOT NULL |  | Indicates the shipment temperature of the container. |
| 12 | `TOTAL_WEIGHT` | DOUBLE | NOT NULL |  | The total weight of the shipment. |
| 13 | `UNIT_OF_MEAS_CD` | DOUBLE | NOT NULL | FK→ | The unit of measure the total weight is given in. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTAINER_CONDITION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `CONTAINER_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SHIPMENT_ID` | [BB_SHIPMENT](BB_SHIPMENT.md) | `SHIPMENT_ID` |
| `UNIT_OF_MEAS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_SHIP_EVENT](BB_SHIP_EVENT.md) | `CONTAINER_ID` |

