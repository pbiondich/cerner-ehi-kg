# SCH_PEND_ORDER

> Contains base order information about an appointment which will be created.

**Description:** Scheduling Pending Order  
**Table type:** ACTIVITY  
**Primary key:** `SCH_PEND_ORDER_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The order catalog. |
| 2 | `MODIFIED_IND` | DOUBLE | NOT NULL |  | Indicates id the order detail has been modified. 0 represents no change. 1 represents that the order details are modified. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order identifier. |
| 4 | `ORDER_SEQ_NBR` | DOUBLE | NOT NULL |  | The sequence in which the order should appear on the event. |
| 5 | `SCH_PEND_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The pending event identifier that this data belongs to. |
| 6 | `SCH_PEND_ORDER_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the SCH_PEND_ORDER table. |
| 7 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The order synonym. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `SCH_PEND_EVENT_ID` | [SCH_PEND_EVENT](SCH_PEND_EVENT.md) | `SCH_PEND_EVENT_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SCH_PEND_ORDER_DETAIL](SCH_PEND_ORDER_DETAIL.md) | `SCH_PEND_ORDER_ID` |
| [SCH_PEND_SURG_ITEM](SCH_PEND_SURG_ITEM.md) | `SCH_PEND_ORDER_ID` |

