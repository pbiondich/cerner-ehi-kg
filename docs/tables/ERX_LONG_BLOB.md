# ERX_LONG_BLOB

> Stores BLOB data for Electronic Prescribing

**Description:** Electronic Prescribing Long Blob  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONSUMER_IDENT` | VARCHAR(255) | NOT NULL |  | Unique ID to identify the stored blob data. The ID value is decided by the client/consumer. The in the format is to handle the case where multiple are stored in the same transaction. When multiple are stored, the ID must be guaranteed to be reproduced consistently (regardless of when it is created) to ensure uniqueness of the string and consistency in retrieving the correct data.;Format: : : : |
| 3 | `CONSUMER_IDENT_HASH` | DOUBLE | NOT NULL |  | Hash of CONSUMER_IDENT. This value is used as an index for retrieving data. |
| 4 | `ERX_LONG_BLOB` | LONGBLOB |  |  | The BLOB data to be stored on the ERX_LONG_BLOB table. |
| 5 | `ERX_LONG_BLOB_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

