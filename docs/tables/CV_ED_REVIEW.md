# CV_ED_REVIEW

> Stores information about an ED physician's review of a cardiology order and the cardiologist's subsequent review

**Description:** CV_ED_REVIEW  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CV_ED_REVIEW_ID` | DOUBLE | NOT NULL |  | Primary key |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order ID to which the record is associated |
| 3 | `REQUESTOR_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The Provider who requested the review. |
| 4 | `REQUEST_DT_TM` | DATETIME |  |  | The date and time when the request was placed. |
| 5 | `REVIEWER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The Provider who reviewed the request. |
| 6 | `REVIEW_DT_TM` | DATETIME |  |  | The date and time when the request was reviewed. |
| 7 | `REVIEW_STATUS_CD` | DOUBLE | NOT NULL |  | A code representing the status of tghe review request |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALID_UNTIL_DT_TM` | DATETIME |  |  | Date/Time used for versioning the states of a review request for an order. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `REQUESTOR_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REVIEWER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

