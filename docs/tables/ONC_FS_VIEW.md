# ONC_FS_VIEW

> This table contains views for the Oncology Flowsheet.

**Description:** Oncology Flowsheet View  
**Table type:** REFERENCE  
**Primary key:** `ONC_FS_VIEW_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLATION_SEQ` | DOUBLE | NOT NULL |  | Collation sequence used for ordering Oncology Flowsheet Views |
| 2 | `IN_USE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ONC_FS_VIEW_EVENT_SET_NAME` | VARCHAR(100) |  |  | Name of Event Set to be used in the Oncology Flowsheet View |
| 4 | `ONC_FS_VIEW_ID` | DOUBLE | NOT NULL | PK | Primary key for Oncology Flowsheet Views |
| 5 | `ONC_FS_VIEW_NAME` | VARCHAR(100) | NOT NULL |  | Name of Oncology Flowsheet View |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ONC_FS_VIEW_RX_SET_RELTN](ONC_FS_VIEW_RX_SET_RELTN.md) | `ONC_FS_VIEW_ID` |

