# DA_FOLDER

> The folder table is used to capture information for each folder used in Discern Analyics 2.0 reporting

**Description:** Discern Analytics Folder  
**Table type:** REFERENCE  
**Primary key:** `DA_FOLDER_ID`  
**Columns:** 20  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CORE_IND` | DOUBLE | NOT NULL |  | Indicates this business view was created by Cerner. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date and time the folder was created. |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person that initially created the folder. |
| 4 | `DA_FOLDER_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DA_FOLDER table. |
| 5 | `DA_FOLDER_NAME` | VARCHAR(255) | NOT NULL |  | Name of the folder. |
| 6 | `DA_FOLDER_NAME_KEY` | VARCHAR(255) | NOT NULL |  | Same as the folder name, but converted to upper case with spaces removed. |
| 7 | `DA_FOLDER_NAME_KEY_A_NLS` | VARCHAR(1020) |  |  | The NLS key for searching in all non-English locales. |
| 8 | `FOLDER_DESC` | VARCHAR(2000) | NOT NULL |  | Description of the folder. |
| 9 | `FOLDER_TYPE_CD` | DOUBLE | NOT NULL |  | Method of categorizing a folder. |
| 10 | `FOLDER_UUID` | VARCHAR(100) | NOT NULL |  | The UUID is used to establish a unique identifier across all systems. The UUID for an item will be the same from one environment to another. |
| 11 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last updated. |
| 12 | `LAST_UPDT_USER_ID` | DOUBLE | NOT NULL |  | The person that last updated this row. |
| 13 | `OWNER_GROUP_CD` | DOUBLE | NOT NULL |  | The owner group of the folder, used to categorize items across a solution group or functional area (ex Operational vs Financial). |
| 14 | `PARENT_FOLDER_ID` | DOUBLE | NOT NULL | FK→ | Higher level folder for this one. |
| 15 | `PUBLIC_IND` | DOUBLE | NOT NULL |  | Determines whether the folder is available for public use. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PARENT_FOLDER_ID` | [DA_FOLDER](DA_FOLDER.md) | `DA_FOLDER_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DA_FOLDER](DA_FOLDER.md) | `PARENT_FOLDER_ID` |
| [DA_FOLDER_QUERY_RELTN](DA_FOLDER_QUERY_RELTN.md) | `DA_FOLDER_ID` |
| [DA_FOLDER_REPORT_RELTN](DA_FOLDER_REPORT_RELTN.md) | `DA_FOLDER_ID` |

