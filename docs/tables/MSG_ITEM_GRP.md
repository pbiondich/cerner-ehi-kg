# MSG_ITEM_GRP

> Defines a subset of items within a messaging category

**Description:** Messaging Item Group  
**Table type:** REFERENCE  
**Primary key:** `MSG_ITEM_GRP_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE |  |  | Represents the private owner of this category |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Original Creation Date |
| 3 | `ITEM_GRP_DESC` | VARCHAR(40) | NOT NULL |  | Item Group Description |
| 4 | `ITEM_GRP_NAME` | VARCHAR(40) | NOT NULL |  | Item Group Name |
| 5 | `MSG_CATEGORY_TYPE_CD` | DOUBLE | NOT NULL |  | Message Category Type Code |
| 6 | `MSG_ITEM_GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | Message Item Group Type Code |
| 7 | `MSG_ITEM_GRP_ID` | DOUBLE | NOT NULL | PK | Message item Group ID - Primary Key |
| 8 | `MSG_NOTIFY_CATEGORY_CD` | DOUBLE | NOT NULL |  | Identify this category as belonging to the key notifications or due. |
| 9 | `MSG_NOTIFY_ITEM_CD` | DOUBLE | NOT NULL |  | Identify what type of key notification this is. |
| 10 | `POSITION_CD` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 11 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 12 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 13 | `PUBLIC_IND` | DOUBLE | NOT NULL |  | Public Indicator |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MSG_ITEM_GRP_DTL_RELTN](MSG_ITEM_GRP_DTL_RELTN.md) | `MSG_ITEM_GRP_ID` |
| [MSG_ITM_GRP_CAT_RELTN](MSG_ITM_GRP_CAT_RELTN.md) | `MSG_ITEM_GRP_ID` |

