# BR_LONG_BLOB_RELTN

> Relates the bill_record to the long_blob

**Description:** BILL RECORD LONG BLOB RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_SIZE` | DOUBLE |  |  | Size of compressed bill record long blob |
| 7 | `BILL_VRSN_NBR` | DOUBLE |  |  | Foreign key to bill record |
| 8 | `BR_LONG_BLOB_RELTN_ID` | DOUBLE | NOT NULL |  | Unique identifier of table |
| 9 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Foreign key to bill record |
| 10 | `DATA_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies the type of data stored in the corresponding long_blob row. 0 - Serialized and Compressed Srv_instance (legacy generation) 1- Claim Data XML 2 - Translated Claim XML 3 - Claim Metadata XML 4 - Claim Data Lite XML 5 - Cached Postscript 6 - Validation XML |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to Long Blob record |
| 13 | `ORIG_SIZE` | DOUBLE |  |  | Original size of bill record before compression |
| 14 | `SEQUENCE` | DOUBLE |  |  | Sequence number of long blob record |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

