# PN_RECOVERY

> This table will serve as the parent table for PathNet recovery logic. IT will be used to track items as they are processed and provide enough high-level data to rebuild a transaction for recovery in the case of a failure.

**Description:** PathNet Result Recovery  
**Table type:** ACTIVITY  
**Primary key:** `PN_RECOVERY_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXPIRE_DT_TM` | DATETIME | NOT NULL |  | Date/time in which this row will expire. This will be used to determine if an item/event has been "in process" too long, which might indicate a problem with processing. |
| 2 | `FAILURE_CNT` | DOUBLE |  |  | Number of times this item has failed to be processed. |
| 3 | `FIRST_FAILURE_DT_TM` | DATETIME |  |  | Date/Time of the first time this item failed to process. |
| 4 | `IN_PROCESS_FLAG` | DOUBLE | NOT NULL |  | Indicates where this item is in the process: |
| 5 | `LAST_FAILURE_DT_TM` | DATETIME |  |  | Date/Time of the last time this item failed to process. |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique ID to the PARENT_ENTITY_NAME table. |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Table to which this row is linked. |
| 8 | `PN_RECOVERY_ID` | DOUBLE | NOT NULL | PK | Unique ID. |
| 9 | `RECOVERY_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of item. References code set 28600. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PN_RECOVERY_CHILD](PN_RECOVERY_CHILD.md) | `PN_RECOVERY_ID` |

