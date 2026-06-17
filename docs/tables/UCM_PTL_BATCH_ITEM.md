# UCM_PTL_BATCH_ITEM

> This table tracks the orders and optionally containers that were used in and created by a protocol batch.

**Description:** Unified Case Manager - Protocol Batch Item  
**Table type:** ACTIVITY  
**Primary key:** `UCM_PTL_BATCH_ITEM_ID`  
**Columns:** 21  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BATCH_ITEM_STATUS_CD` | DOUBLE | NOT NULL |  | This field is used to indicate the status of this item within this batch. |
| 4 | `BATCH_ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | Used to indicate the status of the order within this batch. |
| 5 | `BATCH_SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Used to identify the sequence of the order in the batch. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CONTAINER_ID` | DOUBLE | NOT NULL |  | Specifies the container that is associated to this batch. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `EVALUATION_FLAG` | DOUBLE | NOT NULL |  | Current evaluation status of a protocol order. 0 - none; 1 - Pending evaluation; 2 - Completed evaluation |
| 10 | `INPUT_IND` | DOUBLE | NOT NULL |  | Indicates if this batch item was used as input to the batch. If it is not an input to the batch, it was created by the batch. |
| 11 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Specifies the order that is associated to this batch. |
| 12 | `OUTPUT_SEQUENCE_NBR` | DOUBLE | NOT NULL |  | The sequence in which the output containers are created. |
| 13 | `PREV_UCM_PTL_BATCH_ITEM_ID` | DOUBLE | NOT NULL |  | This field is used to track versions of the protocol batch item information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 14 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the specimen type of the container associated with the batch item. |
| 15 | `UCM_PTL_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Identifies the batch to which this item belongs. |
| 16 | `UCM_PTL_BATCH_ITEM_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a given item within a batch. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `UCM_PTL_BATCH_ID` | [UCM_PTL_BATCH](UCM_PTL_BATCH.md) | `UCM_PTL_BATCH_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [UCM_POSITION_MAP_CELL](UCM_POSITION_MAP_CELL.md) | `UCM_PTL_BATCH_ITEM_ID` |
| [UCM_PTL_RESULT](UCM_PTL_RESULT.md) | `UCM_PTL_BATCH_ITEM_ID` |

