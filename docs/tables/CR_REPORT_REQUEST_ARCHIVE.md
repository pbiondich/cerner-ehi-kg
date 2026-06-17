# CR_REPORT_REQUEST_ARCHIVE

> The report request archive table is used to store the long blob ids referenced to the long_blob table that contain the XML representation of the archived requests

**Description:** Report request archive  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARCHIVED_DT_TM` | DATETIME |  |  | The date and time of the last archive |
| 2 | `ARCHIVED_REPORT_NBR` | DOUBLE | NOT NULL |  | The total number of reports archived for all xml files stored in the zip file. |
| 3 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | Logical domain for purge file |
| 4 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The id of the long blob that contains the zip file of the archived requests |
| 5 | `MAX_REQUEST_DT_TM` | DATETIME | NOT NULL |  | Maximum requested date/time included in zip entry |
| 6 | `MIN_REQUEST_DT_TM` | DATETIME | NOT NULL |  | Minimum requested date/time included in zip entry |
| 7 | `REPORT_REQUEST_ARCHIVE_ID` | DOUBLE | NOT NULL |  | Primary key |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

