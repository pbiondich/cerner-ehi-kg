# PCS_QUEUE_ASSIGNMENT

> Stores the assignment of review items to queues used for Clinical Validation. A review item can be assigned to multiple queues. Review items will be reviewed by individuals assigned to the corresponding queue.

**Description:** Stores the assignment of review items to queues for Clinical Validation.  
**Table type:** ACTIVITY  
**Primary key:** `QUEUE_REVIEW_ID`  
**Columns:** 23  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COMPLETED_DT_TM` | DATETIME |  |  | Contains date the assignment was completed. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `FROM_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code that uniquely identifies the personnel. Provides tracking to whom forwarded this assignment. This field is used to join to other tables such as PRSNL. |
| 9 | `FROM_QUEUE_REVIEW_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code that uniquely identifies the assignment of queue and review item. Provides tracking from which assignment the current assignment was forwarded. This field is used to join to other tables such as PCS_QUEUE_ASSIGNMENT. |
| 10 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code that uniquely identifies the review hierarchy. This field is used to join to other tables such as PCS_HIERARCHY. |
| 11 | `PENDING_DT_TM` | DATETIME | NOT NULL |  | Contains date the assignment was initiated. |
| 12 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code that uniquely identifies the queue. This field is used to join to other tables such as PCS_QUEUE. |
| 13 | `QUEUE_REVIEW_ID` | DOUBLE | NOT NULL | PK | Contains the internal identification code that uniquely identifies the assignment of queue and review item. |
| 14 | `RETURN_TO_SENDER_IND` | DOUBLE |  |  | Indicates if assignment should be forwarded back to the sender indicated in from_queue_review_id and from_prsnl_id upon approval. |
| 15 | `REVIEW_ID` | DOUBLE | NOT NULL | FK→ | Contains the internal identification code that uniquely identifies a review item. This field is used to join to other tables such as PCS_REVIEW_ITEM. |
| 16 | `REVIEW_LEVEL_SEQ` | DOUBLE | NOT NULL |  | The level or sequence within the assignment that the review item / queue relationship is located. |
| 17 | `REVIEW_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of a single review item in this queue. Code set 29161 |
| 18 | `REVIEW_TYPE_CD` | DOUBLE | NOT NULL |  | This is the type of review: ALL, ONE, FYI. Code set 28961. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FROM_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `FROM_QUEUE_REVIEW_ID` | [PCS_QUEUE_ASSIGNMENT](PCS_QUEUE_ASSIGNMENT.md) | `QUEUE_REVIEW_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `QUEUE_ID` | [PCS_QUEUE](PCS_QUEUE.md) | `QUEUE_ID` |
| `REVIEW_ID` | [PCS_REVIEW_ITEM](PCS_REVIEW_ITEM.md) | `REVIEW_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PCS_QUEUE_ASSIGNMENT](PCS_QUEUE_ASSIGNMENT.md) | `FROM_QUEUE_REVIEW_ID` |
| [PCS_REVIEW_HISTORY](PCS_REVIEW_HISTORY.md) | `QUEUE_REVIEW_ID` |

