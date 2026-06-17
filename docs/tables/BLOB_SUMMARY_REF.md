# BLOB_SUMMARY_REF

> This table contains a row for each Thumbnail of an anatomic pathology image.

**Description:** blob_summary_ref  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOB_REF_ID` | DOUBLE | NOT NULL |  | This field contains unique identifier of the blob_reference row to which this blob_summary_ref row is derived from. |
| 2 | `COMPRESSION_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the compression algorithm used to store the blob. |
| 3 | `FORMAT_CD` | DOUBLE | NOT NULL |  | This field contains the storage format identifier for a specific thumbnail row. |
| 4 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier for the long_blob row that contains the thumbnail image data. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

