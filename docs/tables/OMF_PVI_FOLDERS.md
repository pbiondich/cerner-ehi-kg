# OMF_PVI_FOLDERS

> PowerVision Saved View, Filter and Template folders.

**Description:** OMF PVI FOLDERS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FOLDER_ID` | DOUBLE | NOT NULL |  | Unique identifier of the folder. |
| 3 | `FOLDER_NAME` | VARCHAR(255) | NOT NULL |  | Name of folder. |
| 4 | `GRID_CD` | DOUBLE |  |  | Subject area that this folder is a part of. Not filled out for saved views only, e.g., for filter or template folders. Other codesets can be used besides 14265 depending on the team defining the value. |
| 5 | `GROUP_CD` | DOUBLE | NOT NULL |  | The user group that the folder is associated with. From user-defined codeset 13124 |
| 6 | `ITEM_TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of item this folder holds. |
| 7 | `PARENT_ID` | DOUBLE | NOT NULL |  | ID of parent folder. |
| 8 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The group that this folder belongs to. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `USER_ID` | DOUBLE | NOT NULL |  | Person who owns this folder. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |

