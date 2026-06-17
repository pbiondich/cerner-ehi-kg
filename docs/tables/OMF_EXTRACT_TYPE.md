# OMF_EXTRACT_TYPE

> Contains the feeds for Care Profiling and the active status. The default is inactive; the feeds must be turned on by the project team when Care Profiling is installed.

**Description:** Contains the feeds for Care Profiling and the active status.  
**Table type:** REFERENCE  
**Primary key:** `EXTRACT_TYPE_CD`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EXTRACT_TYPE_CD` | DOUBLE | NOT NULL | PK | The type of extract script referenced by this row. |
| 3 | `LAST_EXTRACT_DT_TM` | DATETIME |  |  | The last time a batch extract was completed for the extract referenced by EXTRACT_TYPE_CD |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OMF_EXTRACT_BATCH](OMF_EXTRACT_BATCH.md) | `EXTRACT_TYPE_CD` |

