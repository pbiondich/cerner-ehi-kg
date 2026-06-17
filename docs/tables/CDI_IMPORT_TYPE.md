# CDI_IMPORT_TYPE

> This table defines the types of requests to import Document Imaging documents to the system.

**Description:** Cerner Document Imaging Import Type  
**Table type:** REFERENCE  
**Primary key:** `CDI_IMPORT_TYPE_ID`  
**Columns:** 24  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BATCH_PRIORITY_NBR` | DOUBLE |  |  | Specifies the priority of the batch. Batches are sorted and processed in priority order. Suggested values are 1 = High, 5 = Medium and 10 = Low. |
| 3 | `CDI_IMPORT_TYPE_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the CDI_IMPORT_TYPE table. |
| 4 | `CONTENT_TYPE_NAME` | VARCHAR(60) |  |  | CAMM content type name, if input type is XML files. |
| 5 | `DEFAULT_BATCH_CLASS_NAME` | VARCHAR(32) |  |  | The default name of the batch class. |
| 6 | `DESTINATION_FOLDER_NAME` | VARCHAR(255) |  |  | The destination folder name for files to import. |
| 7 | `DOMAIN_NAME` | VARCHAR(20) |  |  | The name of the domain this import type is for. |
| 8 | `EMAIL_ADDRESSES_TEXT` | VARCHAR(500) |  |  | A comma separated list of email addresses that will be notified of errors. In detail, this email address list is used for notifications if an error occurs in processing a feed. |
| 9 | `IMPORT_TYPE_NAME` | VARCHAR(50) |  |  | The name of a type of request for importing documents into the system. |
| 10 | `INPUT_DIRECTORY_NAME` | VARCHAR(255) |  |  | The source folder name for files to import. |
| 11 | `INPUT_MASK_TEXT` | VARCHAR(10) |  |  | A mask used to filter which files get imported by this import request type. |
| 12 | `INPUT_TYPE_FLAG` | DOUBLE |  |  | Type of input. (0 = text files, 1 = parse file names, 2 = XML files, 3 = filing and bursting) |
| 13 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 14 | `OVERLAY_FORM_NAME` | VARCHAR(50) | NOT NULL |  | The name of a form that text or images can be overlayed to provide context to the data. |
| 15 | `PARSE_DELIMITER_TEXT` | VARCHAR(5) |  |  | The delimiter used to separate field values in the file name of the file being imported. |
| 16 | `PARSE_FIELDS_TEXT` | VARCHAR(2000) |  |  | The fields in the file name of the file being imported. |
| 17 | `PURGE_AGE_HRS` | DOUBLE | NOT NULL |  | The age (in hours) of the source files before they are purged. |
| 18 | `REPORT_TYPE_IDENT` | VARCHAR(255) |  |  | Identifies the report type associated with this type of import request. |
| 19 | `TIME_ZONE` | VARCHAR(100) |  |  | The default time zone for this import type. |
| 20 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CDI_IMPORT_JOB](CDI_IMPORT_JOB.md) | `CDI_IMPORT_TYPE_ID` |
| [CDI_IMPORT_TYPE_SERVICE_R](CDI_IMPORT_TYPE_SERVICE_R.md) | `CDI_IMPORT_TYPE_ID` |

