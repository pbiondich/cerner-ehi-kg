# MSG_CONFIG

> Defines a view of messaging items and filtering arrangements

**Description:** Messaging Configuration  
**Table type:** REFERENCE  
**Primary key:** `MSG_CONFIG_ID`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE |  |  | Represents the private owner of this category |
| 2 | `CONFIG_DESC` | VARCHAR(40) | NOT NULL |  | Config Description |
| 3 | `CONFIG_NAME` | VARCHAR(40) | NOT NULL |  | Configuration Name |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Original Creation Date |
| 5 | `MSG_CONFIG_ID` | DOUBLE | NOT NULL | PK | Msg Config ID - Primary Key |
| 6 | `POSITION_CD` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 7 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Represents the private owner of this category |
| 9 | `PUBLIC_IND` | DOUBLE | NOT NULL |  | Indicates whether this configuration is offered to others for reuse |
| 10 | `SEARCH_RNG_UNITS` | DOUBLE |  |  | Search range units, i.e. 1 = Days |
| 11 | `SEARCH_RNG_VALUE` | DOUBLE |  |  | Search range value, i.e. 30 |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `USER_MODIFY_IND` | DOUBLE | NOT NULL |  | Indicates whether the user can modify this configuration from outside the build tools |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MSG_CFG_CAT_RELTN](MSG_CFG_CAT_RELTN.md) | `MSG_CONFIG_ID` |
| [MSG_CONFIG_PUB_ASNMNT](MSG_CONFIG_PUB_ASNMNT.md) | `MSG_CONFIG_ID` |

