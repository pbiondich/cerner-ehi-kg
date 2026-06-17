# AP_FOLDER_ENTITY

> This folder contains a row for each 'item' a folder contains. Currently, items may include reference images, images belonging to a specific pathology case, and entire pathology cases.

**Description:** ap_folder_entity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR` | CHAR(21) |  |  | This field contains the case identifier for the pathology case to which this folder item references. This field will be empty for reference images. |
| 2 | `COMMENT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the long_text table that contains the comment associated with the folder. |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the person_id for the user who added this item to the folder. |
| 4 | `DISPLAY` | VARCHAR(255) |  |  | This field contains the displayable name for the folder item. |
| 5 | `ENTITY_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier for this table. |
| 6 | `ENTITY_TYPE_FLAG` | DOUBLE |  |  | This field identifies the type of folder item. Currently, only reference images, images associated to a pathology case, and pathology cases are valid types. |
| 7 | `FOLDER_ID` | DOUBLE | NOT NULL |  | This field contains the foreign key value used to join to the AP_FOLDER table. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field contains the primary identifier for the parent table. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | This field contains the table name for the parent table. |
| 10 | `SEQUENCE` | DOUBLE |  |  | This field is not currently used. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

