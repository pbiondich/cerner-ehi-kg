# CE_BLOB

> The ce_blob table contains the actual contents of a locally stored document.

**Description:** ce blob  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOB_CONTENTS` | LONGBLOB |  |  | Text of the blob. |
| 2 | `BLOB_LENGTH` | DOUBLE | NOT NULL |  | Number of bytes in the blob. |
| 3 | `BLOB_SEQ_NUM` | DOUBLE | NOT NULL |  | Sequence Nbr is used to make the primary key unique in the case where the document has more than one blob. |
| 4 | `COMPRESSION_CD` | DOUBLE | NOT NULL |  | Specifies type of compression applied to the blob. |
| 5 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the Event Table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when this row is valid. |
| 12 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. We need to determine what that value is. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

