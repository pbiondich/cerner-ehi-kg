# CE_BLOB_SUMMARY

> Blob thumbnail information.

**Description:** CE_BLOB_SUMMARY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOB_LENGTH` | DOUBLE | NOT NULL |  | The size of the blob. |
| 2 | `BLOB_SUMMARY_ID` | DOUBLE | NOT NULL |  | Logical row identifier. |
| 3 | `CE_BLOB_SUMMARY_ID` | DOUBLE | NOT NULL |  | Unique row identifier. |
| 4 | `CHECKSUM` | DOUBLE | NOT NULL |  | The checksum of the blob. |
| 5 | `COMPRESSION_CD` | DOUBLE | NOT NULL |  | Compression used to store the blob. |
| 6 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the Clinical Event table. |
| 7 | `FORMAT_CD` | DOUBLE | NOT NULL |  | Identifies the format of the blob. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Signifies the time that this event began. |
| 14 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Time at which this event ceased to be valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

