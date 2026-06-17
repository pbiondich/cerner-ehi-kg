# SN_COMMENT_TEXT

> SurgiNet Comment Text Table

**Description:** SurgiNet Comment Text  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COMMENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of comment that this is. |
| 7 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for creating the row |
| 8 | `CREATE_DT_TM` | DATETIME |  |  | The Create Date and Time for the row |
| 9 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The ID of the Personnel responsible for creating the row |
| 10 | `CREATE_TASK` | DOUBLE |  |  | The task creating the row |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `HEADER` | VARCHAR(150) | NOT NULL |  | Header for the Comment |
| 13 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The ID from the LONG_BLOB table for the blob data |
| 14 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The ID from the LONG_TEXT table for the text data |
| 15 | `REFERENCE_IND` | DOUBLE | NOT NULL |  | Specifies if this is a reference Comment |
| 16 | `ROOT_ID` | DOUBLE | NOT NULL |  | The ID from the table specified in ROOT_NAME for which this comment is being stored for |
| 17 | `ROOT_NAME` | VARCHAR(30) | NOT NULL |  | The table for which the comment is being stored for |
| 18 | `SEG_CD` | DOUBLE | NOT NULL |  | The segment for which the comment is being store for |
| 19 | `SEQ_NUM` | DOUBLE | NOT NULL |  | Sequence number of the comment text |
| 20 | `SN_COMMENT_ID` | DOUBLE | NOT NULL |  | The Unique ID for the table |
| 21 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The Surgical Area for which the comment is stored for |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

