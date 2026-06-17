# PDOC_TAG_HANDLE

> This table captures data about blobs stored remotely (such as Images stored via MMF) that a user tags, i.e. marks as an item of interest.

**Description:** Physician Documentation Tag Handle  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOB_HANDLE` | VARCHAR(2000) | NOT NULL |  | Handle to remote blob. |
| 2 | `FORMAT_CD` | DOUBLE | NOT NULL |  | The format of the blob e.g. PNG, JPG |
| 3 | `PDOC_TAG_HANDLE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PDOC_TAG_HANDLE table. |
| 4 | `STORAGE_CD` | DOUBLE | NOT NULL |  | Identifies location/device where blob is stored. For example, MMF |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

