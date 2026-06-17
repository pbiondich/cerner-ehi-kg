# SN_PRIV_APP_REF

> This table holds the applications that are available for building privileges of a specific type.

**Description:** Reference table holding applications for a given privilege type.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESS_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of access to the specified application for a given person or position. |
| 2 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | The number off of the APPLICATION table for an application that will be used for a privilege type. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The _id of the reference object in the table listed in PARENT_ENTITY_NAME that needs to have applications attached to it. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the table that this privilege type refers to. |
| 5 | `PRIV_APP_REF_ID` | DOUBLE | NOT NULL |  | The primary key for this table. |
| 6 | `PRIV_TYPE_NAME` | VARCHAR(32) | NOT NULL |  | The name of the privilege type that these applications are available for. Typically, this is the name of another table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

