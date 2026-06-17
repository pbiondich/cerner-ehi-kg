# DD_REF_FORMAT

> This table refers to an XSLT blob used to format raw data returned by the Data Retrieval Services. The raw data is returned in XML format that adheres to an XSD defined by Data Retrieval Services.

**Description:** Dynamic Documentation - Reference Format  
**Table type:** REFERENCE  
**Primary key:** `DD_REF_FORMAT_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DD_REF_FORMAT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies an XSLT blob used to format raw data returned by queries made to CDG. |
| 3 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | Contains a brief description of the XSLT. |
| 4 | `EMR_CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the EMR content type. A 0 indicates a reusable format. |
| 5 | `LONG_BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | Long blob reference ID. Points to the actual XSLT blob. |
| 6 | `NAME_TXT` | VARCHAR(255) |  |  | Contains the XSLT file name and path. |
| 7 | `SOURCE_TXT` | VARCHAR(255) | NOT NULL |  | Identifies where the format originated. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_REF_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DD_REF_EMR_CONTENT](DD_REF_EMR_CONTENT.md) | `DD_REF_FORMAT_ID` |

