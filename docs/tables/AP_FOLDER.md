# AP_FOLDER

> This table contains all anatomic pathology folders, both public and private.

**Description:** ap_folder  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANONYMOUS_BITMAP` | DOUBLE |  |  | This field contains the permission values used for users that have not been explicitly assigned proxy permissions, but do have application/task security required to use 'folder' functionality. Valid values are the same for the permission_bitmap. |
| 2 | `COMMENT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the long_text table that contains the comment associated with the folder. |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the person_id of the person who created this folder. |
| 4 | `DEFAULT_BITMAP` | DOUBLE |  |  | This field contains the 'default' permission values used when adding new 'proxy' permissions. |
| 5 | `FOLDER_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier for this table. |
| 6 | `FOLDER_NAME` | VARCHAR(100) |  |  | This field contains the display name of the folder. |
| 7 | `FOLDER_NAME_KEY` | VARCHAR(100) | NOT NULL |  | This field contains the folder_name with all special characters removed and all alpha characters converted to uppercase. This column must be 'unique' at the nodes level. |
| 8 | `FOLDER_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | FOLDER_NAME_KEY_A_NLS column |
| 9 | `FOLDER_NAME_KEY_NLS` | VARCHAR(202) |  |  | This column was added for internationalization reasons. |
| 10 | `PARENT_FOLDER_ID` | DOUBLE | NOT NULL |  | This field contains the folder_id of the parent folder. If this folder is at the 'root' level, this field will contain the same value as the folder_id column. |
| 11 | `PUBLIC_IND` | DOUBLE |  |  | This field indicates whether or not this folder is personal or public. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

