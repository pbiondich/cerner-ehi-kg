# DA_DOCUMENT

> Contains the generated document created when a Report or Query Run is stored in the Discern Analytics 2.0 system.

**Description:** Discern Analytics Document  
**Table type:** ACTIVITY  
**Primary key:** `DA_DOCUMENT_ID`  
**Columns:** 20  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPATIBILITY_VERSION_NBR` | DOUBLE |  |  | Used by Discern Analytics 2.0 to indicate whether a document may be opened by a particular DA2 application revision.; |
| 2 | `CREATED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person that generated this document. |
| 3 | `DA_DOCUMENT_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the DA_DOCUMENT table. |
| 4 | `DA_QUERY_ID` | DOUBLE | NOT NULL | FK→ | The query which this document was generated from |
| 5 | `DA_REPORT_ID` | DOUBLE | NOT NULL | FK→ | The report format which this document was generated from. |
| 6 | `DOCUMENT_NAME` | VARCHAR(100) |  |  | Optional Name assigned to the document. |
| 7 | `DOCUMENT_NAME_KEY` | VARCHAR(100) |  |  | Uppercase, no spaces document name. |
| 8 | `DOCUMENT_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | Facilitates accent insensitive searches/sorts on the DOCUMENT_NAME_KEY column (National Language Support) |
| 9 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The type of document generated (such as html, pdf, postscript, etc.) |
| 10 | `GENERATED_DATA_ID` | DOUBLE | NOT NULL | FK→ | Contains a link to the document data. |
| 11 | `GENERATED_DOC_ID` | DOUBLE | NOT NULL | FK→ | Document as ran, stored on the long_blob table. |
| 12 | `GENERATED_DT_TM` | DATETIME | NOT NULL |  | Date and time that this document was generated. |
| 13 | `REPORT_PARMS_ID` | DOUBLE | NOT NULL | FK→ | XML String containing the parameters entered for this report run. Stored on the long_blob table. |
| 14 | `SECURITY_GROUP_CD` | DOUBLE | NOT NULL |  | Code value for the security group associated with this document. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `VALID_UNTIL_DT_TM` | DATETIME |  |  | Date and time to which the document remains valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DA_QUERY_ID` | [DA_QUERY](DA_QUERY.md) | `DA_QUERY_ID` |
| `DA_REPORT_ID` | [DA_REPORT](DA_REPORT.md) | `DA_REPORT_ID` |
| `GENERATED_DATA_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `GENERATED_DOC_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `REPORT_PARMS_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [DA_BATCH_QUERY_LOG](DA_BATCH_QUERY_LOG.md) | `CREATED_DOCUMENT_ID` |
| [DA_BATCH_REPORT_LOG](DA_BATCH_REPORT_LOG.md) | `CREATED_DOCUMENT_ID` |
| [DA_DOCUMENT_ORG_RELTN](DA_DOCUMENT_ORG_RELTN.md) | `DA_DOCUMENT_ID` |
| [DA_DOCUMENT_PRSNL_RELTN](DA_DOCUMENT_PRSNL_RELTN.md) | `DA_DOCUMENT_ID` |

