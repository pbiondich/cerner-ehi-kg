# CDS_BATCH_HIST

> Maintains audit information about each batch generated.

**Description:** Commissioning Data Set - Batch History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDS_BATCH_DT_TM` | DATETIME | NOT NULL |  | Contains the Date and Time the batch was run. |
| 2 | `CDS_BATCH_END_DT_TM` | DATETIME | NOT NULL |  | Contains the end date of the date range of udates or activity that the batch contains. |
| 3 | `CDS_BATCH_FILENAME` | VARCHAR(50) |  |  | The main filename for this batch. |
| 4 | `CDS_BATCH_HIST_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a history batch. |
| 5 | `CDS_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the batch related to this history record. |
| 6 | `CDS_BATCH_SIZE` | DOUBLE |  |  | Number of items in this given batch. |
| 7 | `CDS_BATCH_START_DT_TM` | DATETIME | NOT NULL |  | Contains the start date of date range of updates or activity that the batch contains ( usually equal to the cds_batch_end_dt_tm of the last batch of this type for this organization.) |
| 8 | `CDS_BATCH_STATUS_CD` | DOUBLE | NOT NULL |  | Denotes the status of the batch run. Uses the codeset 254591. |
| 9 | `CDS_BATCH_TYPE_CD` | DOUBLE | NOT NULL |  | Contains a code value that describes the type of batch. |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the organization related to this batch. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDS_BATCH_ID` | [CDS_BATCH](CDS_BATCH.md) | `CDS_BATCH_ID` |

