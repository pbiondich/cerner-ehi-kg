# TEST_REVIEWER

> Facilitates and records the review process for a specific order. All users or personnel groups that make up the review hierarchy are stored as separate records along with the status and other relevant information for each.

**Description:** Test Reviewer  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ELECTRONIC_SIGNATURE_IND` | DOUBLE |  |  | Indicates that the reviewer's electronic signature should be attached to the chart for this order. NOT CURRENTLY IMPLEMENTED. |
| 2 | `NOTIFY_IND` | DOUBLE |  |  | Indicates that the reviewer should be notified via email when an item is added to their queue. |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates the reviewer to a specific order. It is a foreign key reference to the primary key of the orders table. |
| 4 | `QUEUED_TO_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the personnel group which is responsible for the review. Either a group or an individual, not both, will have the review queued to them. |
| 5 | `QUEUED_TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user who is responsible for the review. Either a group or an individual, not both, will have the review queued to them. |
| 6 | `REVIEWED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user who actually performed the review. This may be the person who the review was queued to, a member of the personnel group, or an individual who was granted access to the queue by the queue owner. |
| 7 | `REVIEW_DT_TM` | DATETIME |  |  | Date and time the review was performed. |
| 8 | `REVIEW_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the review group to which this reviewer belongs. Review groups are used to determine what actions its members must take for the review to progress. It is a foreign key reference to the primary key of the res_review_group table. |
| 9 | `REVIEW_LEVEL_CD` | DOUBLE | NOT NULL |  | The code for the review level. Reviews may consist of multiple levels. All reviews at one level must be completed before reviews can be made at the subsequent level. The review process is complete when all reviews at the highest level are complete. |
| 10 | `REVIEW_SEQ` | DOUBLE | NOT NULL |  | Number assigned to make the record unique. This is necessary since a user can routed it to another individual and have it returned in the same level and group. It is also used to order the reviewers. |
| 11 | `REVIEW_STATUS_CD` | DOUBLE | NOT NULL |  | The code for the review status. Gives the current state the review is in for this reviewer. |
| 12 | `ROUTED_FROM_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user who routed the review to this reviewer. Will only be populated when a review is routed or is returned from a routing. |
| 13 | `ROUTE_RETURN_IND` | DOUBLE |  |  | Indicates that the review item should be returned to the original user if and when the user it was routed to approves it. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `QUEUED_TO_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `QUEUED_TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REVIEWED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REVIEW_GROUP_ID` | [RES_REVIEW_GROUP](RES_REVIEW_GROUP.md) | `REVIEW_GROUP_ID` |
| `ROUTED_FROM_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

