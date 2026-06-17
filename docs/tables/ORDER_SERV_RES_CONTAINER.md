# ORDER_SERV_RES_CONTAINER

> Controls all of the PathNet features surrounding 'in-lab' processing. Also, along with the container table, drives specimen transfer lists.

**Description:** Order Service Resource Container  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_DT_TM` | DATETIME |  |  | The time when the order gets to an alert status when monitoring turnaround times. |
| 2 | `AV_IND` | DOUBLE | NOT NULL |  | Provides the ability to turn off autoverification of an accession at a given service resource. |
| 3 | `COLL_INFO_SEQ` | DOUBLE | NOT NULL |  | The sequence value from the collection requirements which was responsible for the container to be associated to the order. |
| 4 | `CONTAINER_ID` | DOUBLE | NOT NULL |  | The system identifier for the container in which the corresponding order resides. |
| 5 | `CURRENT_LOCATION_CD` | DOUBLE | NOT NULL |  | The current location of the container. |
| 6 | `DISPLAY_DT_TM` | DATETIME |  |  | The time when the order gets to a display status when monitoring turnaround times. |
| 7 | `IN_LAB_DT_TM` | DATETIME |  |  | The date/time at which the corresponding order was brought in lab. |
| 8 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The specimen login location of the corresponding service resource. |
| 9 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The system identifier for an order. |
| 10 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The service resource to which the order is currently loaded. |
| 11 | `SPEC_EXPIRE_DT_TM` | DATETIME |  |  | The time when the specimen gets to a display status when monitoring specimen expiration times. |
| 12 | `SPEC_WARNING_DT_TM` | DATETIME |  |  | The time when the specimen gets to a warning status when monitoring specimen expiration times. |
| 13 | `STATUS_FLAG` | DOUBLE |  |  | Indicates the current status of the corresponding order. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `WARNING_DT_TM` | DATETIME |  |  | The time when the order gets to a warning status when monitoring turnaround times. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

