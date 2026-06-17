# MSG_EVENT_GRP

> Defines a set of Event Set Filters

**Description:** Messaging Event Group  
**Table type:** REFERENCE  
**Primary key:** `MSG_EVENT_GRP_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE |  |  | Represents the private owner of this category |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Original Creation Date |
| 3 | `EVENT_GRP_DESC` | VARCHAR(40) | NOT NULL |  | Event Group Description |
| 4 | `EVENT_GRP_NAME` | VARCHAR(40) | NOT NULL |  | Event Group Name |
| 5 | `FILTER_INCLUSIVE_IND` | DOUBLE | NOT NULL |  | Indicates inclusive filtering |
| 6 | `MSG_CATEGORY_TYPE_CD` | DOUBLE | NOT NULL |  | Category Type |
| 7 | `MSG_EVENT_GRP_ID` | DOUBLE | NOT NULL | PK | Message Event Group ID - Primary Key |
| 8 | `POSITION_CD` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 9 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 10 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 11 | `PUBLIC_IND` | DOUBLE | NOT NULL |  | Indicates whether this configuration is offered to others for reuse |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MSG_CATEGORY](MSG_CATEGORY.md) | `MSG_EVENT_GRP_ID` |
| [MSG_EVENT_GRP_DTL_RELTN](MSG_EVENT_GRP_DTL_RELTN.md) | `MSG_EVENT_GRP_ID` |

