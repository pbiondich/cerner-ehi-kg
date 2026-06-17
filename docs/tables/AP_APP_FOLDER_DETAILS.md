# AP_APP_FOLDER_DETAILS

> This table contains a list of (at most) 10 folders that each user has most frequently accessed for a given anatomic pathology application.

**Description:** ap_app_folder_details  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESS_CNT` | DOUBLE | NOT NULL |  | This field contains the number to times a user has accessed a particular folder for a given application. |
| 2 | `APP_FOLDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains a foreign key to the ap_app_folders table. |
| 3 | `FOLDER_ID` | DOUBLE | NOT NULL |  | This field contains folder_id from the ap_folder table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APP_FOLDER_ID` | [AP_APP_FOLDERS](AP_APP_FOLDERS.md) | `APP_FOLDER_ID` |

