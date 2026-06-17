# REV_Q_FILT_CRIT_REV_STAT

> Defines the review statuses to be displayed in the Review Queue application when a specfic review queue filter is applied. Filters are defined by user.

**Description:** Review Queue Filter Criteria Review Status  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILTER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the filter of which the review status is a part. Persnl_id and filter_id are a foreign key reference to the primary key of the review_queue_filter_criteria table. |
| 2 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the users who created the filter. Only this user may use the filter. Persnl_id and filter_id are a foreign key reference to the primary key of the review_queue_filter_criteria table. |
| 3 | `REVIEW_STATUS_CD` | DOUBLE | NOT NULL |  | The code referencing the review status which is part of a review queue filter. Only queue entries with statuses which match those in the filter will be displayed in the queue. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FILTER_ID` | [REVIEW_QUEUE_FILTER_CRITERIA](REVIEW_QUEUE_FILTER_CRITERIA.md) | `FILTER_ID` |
| `PRSNL_ID` | [REVIEW_QUEUE_FILTER_CRITERIA](REVIEW_QUEUE_FILTER_CRITERIA.md) | `PRSNL_ID` |

