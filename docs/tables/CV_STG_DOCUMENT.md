# CV_STG_DOCUMENT

> This table holds the details of the document provided through external sources (e.g. FHIR)

**Description:** Cardiovascular Staging Document  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTENT_TYPE_TXT` | VARCHAR(255) |  |  | Identifies the type of data in the attachment (e.g., application/pdf ). |
| 2 | `CREATION_DT_TM` | DATETIME |  |  | Date and time of diagnostic result creation.; |
| 3 | `CREATION_TZ` | DOUBLE |  |  | CREATION TZ |
| 4 | `CV_STG_DOCUMENT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `CV_STG_METADATA_ID` | DOUBLE |  | FK→ | The staging diagnostic metadata identifier.; |
| 6 | `DATA_SIZE` | DOUBLE |  |  | The number of bytes of data that makes up the attachment.; |
| 7 | `DATA_URL` | VARCHAR(255) |  |  | URL of the diagnostic result data.; |
| 8 | `DOCUMENT_HANDLE` | VARCHAR(255) |  |  | Identifier of the document object. Media object identifier if stored in the multimedia storage.; |
| 9 | `DOCUMENT_SCAN_STATUS_TXT` | VARCHAR(60) |  |  | The scan status of the document (e.g., Safe, Unsafe, Skip, Timeout, Unknown).; |
| 10 | `DOCUMENT_VERSION_TXT` | VARCHAR(80) |  |  | Version of the identified document object in the multimedia storage.; |
| 11 | `FORMAT_CD` | DOUBLE |  |  | Allows a potential consumer to know how to render the specific media file format of the document and corresponds to the equivalent MIME type of the document as it was stored in CAMM.; |
| 12 | `STORAGE_CD` | DOUBLE |  |  | Identifies the location/device where the BLOB is stored (e.g., BLOB table, multimedia storage).; |
| 13 | `TITLE_TEXT` | VARCHAR(255) |  |  | A label or a set of text to represent the diagnostic result data.; |
| 14 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TZ` | DOUBLE |  |  | UPDT TIME ZONE |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_STG_METADATA_ID` | [CV_STG_METADATA](CV_STG_METADATA.md) | `CV_STG_METADATA_ID` |

