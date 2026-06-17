# AP_FOLDER_PROXY

> This table contains all of the user and their given permissions pertaining to anatomic pathology folders.

**Description:** ap_folder_proxy  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTACT_IND` | DOUBLE |  |  | This field identifies whether or not the given user should be used as a point of reference for the given folder. For example, if a user has a question about the purpose of the folder they would contact the person labeled a "contact". |
| 2 | `FOLDER_ID` | DOUBLE | NOT NULL |  | This field contains the foreign key value used to join to the ap_folder table. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the 'ap_folder_proxy' row is related. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this 'ap_folder_proxy' row is related. At this point valid values are PRSNL_GROUP and PRSNL. |
| 5 | `PERMISSION_BITMAP` | DOUBLE |  |  | This field contains the permission values for a given user or group of users. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

