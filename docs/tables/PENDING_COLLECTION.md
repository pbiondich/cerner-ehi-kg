# PENDING_COLLECTION

> Every PathNet order that is placed in the system as 'not collected' will get a row in this table.

**Description:** Pending Collection  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | Code value identifying the default body site from which this pending collection should be drawn. |
| 2 | `COLLECTION_METHOD_CD` | DOUBLE | NOT NULL |  | Code value identifying the default collection method to be used in collecting this pending order. |
| 3 | `COLLECTION_ROUTE_CD` | DOUBLE | NOT NULL |  | Code value for the collection route to which this pending order has been scheduled. If the order was not scheduled on a collection list this field will be set to 0. |
| 4 | `NURSE_COLLECT_IND` | DOUBLE |  |  | When this field is set to 1, it indicates that a nurse will be collecting this order. A 0 generally means the lab will be collecting. |
| 5 | `NURSE_TASK_TYPE_FLAG` | DOUBLE | NOT NULL |  | This field contains whether the order is eligible for a nurse collection task and the recommended type. 0 - Not eligible; 1 - Order level task; 2 - Container level task |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | A system generated number that uniquely identifies an order. |
| 7 | `PROCESSING_FLAG` | DOUBLE |  |  | This field determines whether an order originated from an external system or from the Cerner system. |
| 8 | `REEVAL_ROUTING_FLAG` | DOUBLE | NOT NULL |  | Field which indicates whether or not routing reevaluation is needed or has already been done. |
| 9 | `RESCHEDULE_IND` | DOUBLE |  |  | This field is set to 1 to indicate that this order has been missed and rescheduled. |
| 10 | `RESPONSIBLE_PARTY_ID` | DOUBLE | NOT NULL |  | This field will indicate a person to whom this order is assigned. The value is taken from the person_id field of the prsnl table. This field is reserved for future functionality. |
| 11 | `SCHEDULED_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time at which this order is scheduled to be collected. For an immediate print order, this field contains the current date and time. |
| 12 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Code value identifying the specimen type of this pending order. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDER_LABORATORY](ORDER_LABORATORY.md) | `ORDER_ID` |

