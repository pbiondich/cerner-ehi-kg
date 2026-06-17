# CR_REPORT_WATERMARK

> Table that stores the available watermark images that can be applied to a Clinical Reporting XR Report

**Description:** CR REPORT WATERMARK  
**Table type:** REFERENCE  
**Primary key:** `REPORT_WATERMARK_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FILE_NAME` | VARCHAR(100) | NOT NULL |  | filename for a watermark image |
| 3 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | unique identifier to the long_blob_reference table where the image is stored. |
| 4 | `ORIENTATION_FLAG` | DOUBLE | NOT NULL |  | Indication as to what type of page orientation this image should be applied to. 0= Portrait and 1 = Landscape |
| 5 | `REPORT_WATERMARK_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the CR_REPORT_WATERMARK table |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `LANDSCAPE_WATERMARK_ID` |
| [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `PORTRAIT_WATERMARK_ID` |

