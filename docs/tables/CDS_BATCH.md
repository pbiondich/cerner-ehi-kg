# CDS_BATCH

> Identifies information about each batch generated.

**Description:** Commissioning Data Set - Batch  
**Table type:** ACTIVITY  
**Primary key:** `CDS_BATCH_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDS_BATCH_DT_TM` | DATETIME | NOT NULL |  | The date and time the batch was run. |
| 2 | `CDS_BATCH_END_DT_TM` | DATETIME | NOT NULL |  | Contains the end date of date range of updates or activity that the batch contains. |
| 3 | `CDS_BATCH_FILENAME` | VARCHAR(50) |  |  | The main filename for this batch. |
| 4 | `CDS_BATCH_ID` | DOUBLE | NOT NULL | PK | Uniquely Identifies a given batch. |
| 5 | `CDS_BATCH_SIZE` | DOUBLE |  |  | Contains the number of items in this batch. |
| 6 | `CDS_BATCH_START_DT_TM` | DATETIME | NOT NULL |  | Contains the start date of date range of updates or activity that the batch contains (usually equals the cds_batch_end_date of the last batch of this type for this organization.) |
| 7 | `CDS_BATCH_STATUS_CD` | DOUBLE | NOT NULL |  | Denotes the status of the batch run. Uses Code Set # 254591. |
| 8 | `CDS_BATCH_TYPE_CD` | DOUBLE | NOT NULL |  | Describes the type of batch. |
| 9 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Contains the organization id of the trust. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CDS_BATCH_CONTENT](CDS_BATCH_CONTENT.md) | `CDS_BATCH_ID` |
| [CDS_BATCH_HIST](CDS_BATCH_HIST.md) | `CDS_BATCH_ID` |

