# DM_REFCHG_PKW_VERS

> Contains versions of RDDS PK_WHERE string for each table it tracks.

**Description:** DM REFCHG PKW VRS  
**Table type:** REFERENCE  
**Primary key:** `DM_REFCHG_PKW_VERS_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DM_REFCHG_PKW_VERS_ID` | DOUBLE | NOT NULL | PK | Unique identifier of table |
| 3 | `PKW_FORMAT` | VARCHAR(1000) |  |  | Format of what a RDDS PK_where should look like for an insert or update on the table_name. |
| 4 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of table that we are storing PK_where formats for. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_CHG_LOG](DM_CHG_LOG.md) | `DM_REFCHG_PKW_VERS_ID` |

