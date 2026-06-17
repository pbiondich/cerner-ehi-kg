# FOREIGN_CONTENT

> The Foreign_Content table contains information about what exists in a certain foreign folder.

**Description:** Foreign Content  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONTENT_NAME` | VARCHAR(255) |  |  | The Content_Name is a free text entry used to identify an item contained in a foreign folder. |
| 3 | `CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | The Content_Type_Cd identifies the media type of the foreign content item. |
| 4 | `FILM_COUNT` | DOUBLE |  |  | The Film_Count captures the number of films that are a part of the foreign content item. |
| 5 | `SEQ_FOREIGN_ID` | DOUBLE | NOT NULL |  | The Seq_Foreign_Id uniquely identifies a row within the Foreign_Content table. It has no other meaning or purpose other than to serve as a unique id. |
| 6 | `SEQ_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | The Seq_Object_Id is a foreign key to the Foreign_Folder table. This uniquely identifies the foreign folder that the foreign content resides in. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEQ_OBJECT_ID` | [FOREIGN_FOLDER](FOREIGN_FOLDER.md) | `SEQ_OBJECT_ID` |

