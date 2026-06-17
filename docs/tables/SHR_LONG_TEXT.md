# SHR_LONG_TEXT

> This table is used to store long text informaiton

**Description:** Shared Long Text  
**Table type:** ACTIVITY  
**Primary key:** `SHR_LONG_TEXT_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `LONG_TEXT` | LONGTEXT |  |  | Contains the actual long text. |
| 6 | `LONG_TEXT_HASH_CODE` | DOUBLE | NOT NULL |  | Stores the hash code value of corresponding long_text column. Used to uniquely identify rows as long_text column cannot be used (long data type) |
| 7 | `LONG_TEXT_MD5_HASH_TXT` | VARCHAR(32) |  |  | A text field which stores the MD5 hash code value of corresponding LONG_TEXT column. Used to uniquely identify distinct LONG_TEXT values. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the unique identifier related to the parent entity table. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Uniquely identifies the parent table related to this row. |
| 10 | `SHR_LONG_TEXT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies long text data. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RC_CLN_AREA](RC_CLN_AREA.md) | `SHR_LONG_TEXT_ID` |

