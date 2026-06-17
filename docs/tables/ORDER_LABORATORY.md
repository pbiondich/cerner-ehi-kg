# ORDER_LABORATORY

> Allows additional information for an order that is specific to the laboratory.

**Description:** Order Laboratory  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLECTION_COMMENT` | VARCHAR(50) |  |  | Used for recording a comment about the collection process. |
| 2 | `COLLECTION_PRIORITY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific collection priority associated with the collection process taking place. |
| 3 | `CONTINUING_ORDER` | DOUBLE |  |  | Defines the order as a continuing order. (Currently not implemented) |
| 4 | `EXPEDITE_IND` | DOUBLE |  |  | Indicates whether the order should be expedited or not. (Currently not implemented) |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific order. Creates a relationship to the orders table. |
| 6 | `PENDING_REVIEW_IND` | DOUBLE |  |  | Indicates whether a review of the order is in progress. A value of 0 indicates that no review is in progress. A value of 1 indicates that a review of the order is in progress. |
| 7 | `PROP_RESULT_FLAG` | DOUBLE |  |  | Used for orders that have prompt tests associated with them. (Currently not implemented) |
| 8 | `REPORT_PRIORITY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific priority in which a report is to be produced. |
| 9 | `RESOURCE_ROUTE_LEVEL_FLAG` | DOUBLE |  |  | Defines how the discrete task assays associated with an order catalog item are routed to service resources. |
| 10 | `RESULTS_PENDING` | DOUBLE |  |  | (Currently not implemented) |
| 11 | `REVIEW_REQUIRED_IND` | DOUBLE |  |  | Indicates whether a review of the order is required. A value of 0 means no review is required. A value of 1 means the order will always be reviewed. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PENDING_COLLECTION](PENDING_COLLECTION.md) | `ORDER_ID` |

