# CDI_CM_FOLDER

> Stores content management folder information.

**Description:** CPDI Content Management Folder  
**Table type:** REFERENCE  
**Primary key:** `CDI_CM_FOLDER_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_CM_FOLDER_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the CDI_CM_FOLDER table. |
| 2 | `FOLDER_NAME` | VARCHAR(255) | NOT NULL |  | The name of the content management folder. |
| 3 | `FOLDER_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies a purpose for this folder. 0 = Not specified, 1 = Search folder, 2 = Shared folder, 3 - Staged search folder. |
| 4 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 5 | `SEARCH_ORDER` | DOUBLE | NOT NULL |  | The order search folders are used when searching for a document where a lower search order indicates the folder be searched sooner. A search order of 1 indicates the folder where new images are saved (domain default). |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CDI_ARCHIVE_FOLDER_RELTN](CDI_ARCHIVE_FOLDER_RELTN.md) | `CDI_CM_FOLDER_ID` |

