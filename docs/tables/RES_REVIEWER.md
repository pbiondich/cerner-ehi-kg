# RES_REVIEWER

> Defines a specific user or personnel group which belongs to a certain level and group of a review hierarchy.

**Description:** Result Reviewer  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ELECTRONIC_SIGNATURE_IND` | DOUBLE |  |  | Indicates that the reviewer's electronic signature should be attached to the chart for orders reviewed using this hierarchy. NOT CURRENTLY IMPLEMENTED. |
| 2 | `NOTIFY_IND` | DOUBLE |  |  | Indicates that the reviewer should be notified via email when an item is added to their queue. NOT CURRENTLY IMPLEMENTED. |
| 3 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the personnel group which is responsible for the review. Either a group or an individual, not both, must be assigned as a reviewer. |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user who is responsible for the review. Either a group or an individual, not both, must be assigned as a reviewer. |
| 5 | `REVIEWER_ID` | DOUBLE | NOT NULL |  | A sequentially assigned number which uniquely identifies a Reviewer record. |
| 6 | `REVIEW_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the review group to which this reviewer belongs. Review groups are used to determine what actions its members must take for the review to progress. It is a foreign key reference to the primary key of the res_review_group table. |
| 7 | `REVIEW_HIERARCHY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the review hierarchy to which this reviewer belongs. It is a foreign key reference to the primary key of the res_review_hierarchy table. |
| 8 | `REVIEW_LEVEL_CD` | DOUBLE | NOT NULL |  | The code for the review level. Reviews can be built with multiple levels. All reviews at one level must be completed before reviews can be made at the subsequent level. The review process is complete when all reviews at the highest level are complete. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REVIEW_GROUP_ID` | [RES_REVIEW_GROUP](RES_REVIEW_GROUP.md) | `REVIEW_GROUP_ID` |
| `REVIEW_HIERARCHY_ID` | [RES_REVIEW_HIERARCHY](RES_REVIEW_HIERARCHY.md) | `REVIEW_HIERARCHY_ID` |

