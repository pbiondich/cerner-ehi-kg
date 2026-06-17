# AP_FOLDER_ROLE

> This table contains a listing of folder roles. Specific permissions can be attributed to given roles. In addition, users can be assigned a role, thus dictating the permissions they will have on given folders.

**Description:** ap_folder_role  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PERMISSION_BITMAP` | DOUBLE |  |  | This field contains the "Default" permission values used when adding new 'proxy privileges'. |
| 2 | `ROLE_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier for this table. |
| 3 | `ROLE_NAME` | VARCHAR(40) |  |  | This field contains the display name for a folder role. |
| 4 | `ROLE_NAME_KEY` | VARCHAR(40) | NOT NULL |  | This field contains the role_name value with all special characters removed and all alpha characters converted to upper case. |
| 5 | `ROLE_NAME_KEY_A_NLS` | VARCHAR(160) |  |  | ROLE_NAME_KEY_A_NLS column |
| 6 | `ROLE_NAME_KEY_NLS` | VARCHAR(82) |  |  | This field was added for internationalization purposes. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

