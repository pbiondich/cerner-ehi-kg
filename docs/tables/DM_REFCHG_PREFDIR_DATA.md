# DM_REFCHG_PREFDIR_DATA

> Stores information used to correctly translate preferences that require custom logic

**Description:** Database Architecture Refchg Prefdir Data  
**Table type:** REFERENCE  
**Primary key:** `DM_REFCHG_PREFDIR_DATA_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DIST_NAME` | VARCHAR(2000) | NOT NULL |  | Holds the reference string for the preference |
| 3 | `DIST_NAME_SHORT` | VARCHAR(255) | NOT NULL |  | Short version of DIST_NAME for building indexes on this field. |
| 4 | `DM_REFCHG_PREFDIR_DATA_ID` | DOUBLE | NOT NULL | PK | Primary Key for table ( Sequence for PK will be controlled and shipped from Cerner - no sequence assigned ) |
| 5 | `ENTRY_DATA` | VARCHAR(2000) | NOT NULL |  | Data associated to the DIST_NAME. |
| 6 | `MERGE_ALG` | VARCHAR(10) | NOT NULL |  | Holds the merge algorithm that should be used |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_REFCHG_PREFDIR_DATA_EXCL](DM_REFCHG_PREFDIR_DATA_EXCL.md) | `DM_REFCHG_PREFDIR_DATA_ID` |

