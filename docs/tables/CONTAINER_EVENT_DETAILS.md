# CONTAINER_EVENT_DETAILS

> Determines what orders a container event applies to.

**Description:** container event details  
**Table type:** ACTIVITY  
**Primary key:** `CONTAINER_ID`, `EVENT_SEQUENCE`, `ORDER_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTAINER_ID` | DOUBLE | NOT NULL | PK FK→ | The ID of the container that the event applies to. |
| 2 | `EVENT_SEQUENCE` | DOUBLE | NOT NULL | PK FK→ | The unique identifier for the container event. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | PK FK→ | The ID of the order that this container event applies to. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTAINER_ID` | [CONTAINER_EVENT](CONTAINER_EVENT.md) | `CONTAINER_ID` |
| `EVENT_SEQUENCE` | [CONTAINER_EVENT](CONTAINER_EVENT.md) | `EVENT_SEQUENCE` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CONTAINER_EVENT_ASSAY](CONTAINER_EVENT_ASSAY.md) | `CONTAINER_ID` |
| [CONTAINER_EVENT_ASSAY](CONTAINER_EVENT_ASSAY.md) | `EVENT_SEQUENCE` |
| [CONTAINER_EVENT_ASSAY](CONTAINER_EVENT_ASSAY.md) | `ORDER_ID` |

