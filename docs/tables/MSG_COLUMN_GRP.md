# MSG_COLUMN_GRP

> Defines a subset of columns within a messaging category

**Description:** Messaging Column Group  
**Table type:** REFERENCE  
**Primary key:** `MSG_COLUMN_GRP_ID`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE |  |  | Represents the private owner of this category |
| 2 | `COLUMN_GRP_DESC` | VARCHAR(40) | NOT NULL |  | Column Group Description |
| 3 | `COLUMN_GRP_NAME` | VARCHAR(40) | NOT NULL |  | Column Group Name |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Create Date Time |
| 5 | `DEF_COLUMN_TYPE_CD` | DOUBLE | NOT NULL |  | The column to default sort by for this column group |
| 6 | `DESCEND_IND` | DOUBLE | NOT NULL |  | Indicates the direction to sort the default column by, 0 - ascending, 1- descending |
| 7 | `MSG_CATEGORY_TYPE_CD` | DOUBLE | NOT NULL |  | Message catetory type code |
| 8 | `MSG_COLUMN_GRP_ID` | DOUBLE | NOT NULL | PK | Message Column Group ID |
| 9 | `MSG_COLUMN_TYPE_CD` | DOUBLE | NOT NULL |  | Column type code |
| 10 | `POSITION_CD` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 11 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 12 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 13 | `PUBLIC_IND` | DOUBLE | NOT NULL |  | Indicates whether this configuration is offered to others for reuse |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MSG_CATEGORY](MSG_CATEGORY.md) | `MSG_COLUMN_GRP_ID` |
| [MSG_COLUMN_GRP_DTL_RELTN](MSG_COLUMN_GRP_DTL_RELTN.md) | `MSG_COLUMN_GRP_ID` |

