# MSG_CATEGORY

> Group level item within a Messaging Configuration defined by it's type, item groups, and filter groups.

**Description:** Messaging Category  
**Table type:** REFERENCE  
**Primary key:** `MSG_CATEGORY_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 2 | `CATEGORY_DESC` | VARCHAR(40) | NOT NULL |  | The Category Description |
| 3 | `CATEGORY_NAME` | VARCHAR(40) | NOT NULL |  | The Category Name |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Original Creation Date and Time |
| 5 | `MSG_CATEGORY_ID` | DOUBLE | NOT NULL | PK | %Catetory% |
| 6 | `MSG_CATEGORY_TYPE_CD` | DOUBLE | NOT NULL |  | %Catetory% |
| 7 | `MSG_COLUMN_GRP_ID` | DOUBLE | NOT NULL | FK→ | Message Column data Group ID |
| 8 | `MSG_ENCNTR_GRP_ID` | DOUBLE | NOT NULL | FK→ | Message Encounter filter Group ID |
| 9 | `MSG_EVENT_GRP_ID` | DOUBLE | NOT NULL | FK→ | Message Event filter Group ID |
| 10 | `MSG_NOTIFY_CATEGORY_CD` | DOUBLE | NOT NULL |  | Identify this category as belonging to the key notifications or due. |
| 11 | `MSG_NOTIFY_ITEM_CD` | DOUBLE | NOT NULL |  | Identify what type of key notification this is. |
| 12 | `POSITION_CD` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 13 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 14 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 15 | `PUBLIC_IND` | DOUBLE | NOT NULL |  | Indicates whether this configuration is offered to others for reuse |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MSG_COLUMN_GRP_ID` | [MSG_COLUMN_GRP](MSG_COLUMN_GRP.md) | `MSG_COLUMN_GRP_ID` |
| `MSG_ENCNTR_GRP_ID` | [MSG_ENCNTR_GRP](MSG_ENCNTR_GRP.md) | `MSG_ENCNTR_GRP_ID` |
| `MSG_EVENT_GRP_ID` | [MSG_EVENT_GRP](MSG_EVENT_GRP.md) | `MSG_EVENT_GRP_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MSG_CFG_CAT_RELTN](MSG_CFG_CAT_RELTN.md) | `MSG_CATEGORY_ID` |
| [MSG_ITM_GRP_CAT_RELTN](MSG_ITM_GRP_CAT_RELTN.md) | `MSG_CATEGORY_ID` |

