# SI_HAAD_FILE_DOWNLOAD

> Table to keep track of downloaded files from HAAD

**Description:** SI HAAD File Download  
**Table type:** ACTIVITY  
**Primary key:** `SI_HAAD_FILE_DOWNLOAD_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILE_CONTENT_ID` | DOUBLE | NOT NULL | FK→ | Identifier on the long_blob table for the row containing the contents of the file. |
| 2 | `FILE_IDENT` | VARCHAR(50) | NOT NULL |  | HAAD-assigned file identifier |
| 3 | `FILE_NAME` | VARCHAR(255) | NOT NULL |  | Name of the file as identified by the uploading system |
| 4 | `PROCESSED_FLAG` | DOUBLE | NOT NULL |  | Whether or not the downloaded file was processed by Millennium. 0 = Not processed, 1 = Processed |
| 5 | `SI_HAAD_FILE_DOWNLOAD_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `SI_HAAD_FILE_POLL_ID` | DOUBLE | NOT NULL | FK→ | Identifier on the SI_HAAD_FILE_POLL table |
| 7 | `TRANSACTION_IDENT` | VARCHAR(25) | NOT NULL |  | Transaction identifier |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `ZIP_IND` | DOUBLE | NOT NULL |  | Indicates whether the file content is a zip file |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FILE_CONTENT_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `SI_HAAD_FILE_POLL_ID` | [SI_HAAD_FILE_POLL](SI_HAAD_FILE_POLL.md) | `SI_HAAD_FILE_POLL_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_HAAD_TRANSACTION](SI_HAAD_TRANSACTION.md) | `SI_HAAD_FILE_DOWNLOAD_ID` |

