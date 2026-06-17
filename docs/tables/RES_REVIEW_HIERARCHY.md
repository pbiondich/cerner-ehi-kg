# RES_REVIEW_HIERARCHY

> Defines a unique name for a review hierarchy. Review hierarchies are comprised of reviewers at one or more levels and in one or more groups which must approve results according to the rules of the hierarchy for the results to be released to charting.

**Description:** Result Review Hierarchy  
**Table type:** REFERENCE  
**Primary key:** `REVIEW_HIERARCHY_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `REVIEW_HIERARCHY_DESC` | VARCHAR(20) |  |  | The description of the Review Hierarchy. Unique identifier the user gives the review hierarchy. |
| 3 | `REVIEW_HIERARCHY_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies a Review Hierarchy record. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ORDER_CATALOG](ORDER_CATALOG.md) | `REVIEW_HIERARCHY_ID` |
| [RES_REVIEWER](RES_REVIEWER.md) | `REVIEW_HIERARCHY_ID` |

