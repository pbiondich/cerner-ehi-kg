# DA_FOLDER_QUERY_RELTN

> Defines the relationship between Folders and queries in Discern Analytics 2.0

**Description:** Discern Analytics Folder Query Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DA_FOLDER_ID` | DOUBLE | NOT NULL | FK→ | The folder that this query resides in. |
| 2 | `DA_FOLDER_QUERY_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DA_FOLDER_QUERY_RELTN table. |
| 3 | `DA_QUERY_ID` | DOUBLE | NOT NULL | FK→ | The query that resides in this folder. |
| 4 | `QUERY_ALIAS_NAME` | VARCHAR(255) |  |  | Name of the Query as it will be shown in the folder. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_FOLDER_ID` | [DA_FOLDER](DA_FOLDER.md) | `DA_FOLDER_ID` |
| `DA_QUERY_ID` | [DA_QUERY](DA_QUERY.md) | `DA_QUERY_ID` |

