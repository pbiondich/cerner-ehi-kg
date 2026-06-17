# CHART_REQUEST_ARCHIVE

> The chart request archive table is used to store the LONG BLOB IDs referenced to the LONG_BLOB table that contain the XML representation of the archived charts.

**Description:** Chart Request Archive  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARCHIVE_CHART_NBR` | DOUBLE |  |  | The total number of charts archived for all XML files stored in the zip file |
| 2 | `ARCHIVE_DT_TM` | DATETIME |  |  | The date and time of the last archive |
| 3 | `CHART_REQUEST_ARCHIVE_ID` | DOUBLE | NOT NULL |  | The primary Key for rows in this table |
| 4 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The ID of the Long Blob that contains the zip file of the archived charts |
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

