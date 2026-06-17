# RES_REVIEW_GROUP

> Defines a review group used in building review hierarchies. There are 3 types of review groups -- All, One and FYI -- which require all, one or no reviewers assigned to the group to approve the result before the review process can continue.

**Description:** Result Review Group  
**Table type:** REFERENCE  
**Primary key:** `REVIEW_GROUP_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `REVIEW_GROUP_DESC` | VARCHAR(20) |  |  | The description of the Review Group. Unique identifier the user gives the review group. |
| 3 | `REVIEW_GROUP_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies a Review Group record. |
| 4 | `REVIEW_TYPE_CD` | DOUBLE | NOT NULL |  | The code for the type of review group. Valid types are All, One and FYI. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RES_REVIEWER](RES_REVIEWER.md) | `REVIEW_GROUP_ID` |
| [TEST_REVIEWER](TEST_REVIEWER.md) | `REVIEW_GROUP_ID` |

