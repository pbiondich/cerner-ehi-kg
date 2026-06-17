# MONITOR_FIELD

> This table contains all of the possible column fields for a monitor

**Description:** Monitor field  
**Table type:** REFERENCE  
**Primary key:** `MONITOR_FIELD_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(100) |  |  | Description of the field |
| 2 | `DESCRIPTION_KEY_CAP` | VARCHAR(100) |  |  | Description with all spaces removed. Used for indexing. |
| 3 | `DISPLAY` | VARCHAR(100) |  |  | Display value of the field |
| 4 | `MEANING` | VARCHAR(15) | NOT NULL |  | The Cerner defined meaning of the field. |
| 5 | `MONITOR_FIELD_ID` | DOUBLE | NOT NULL | PK | Meaningless unique identifier of a row on the table. Used as the primary key. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MONITOR_VIEW_FIELD](MONITOR_VIEW_FIELD.md) | `MONITOR_FIELD_ID` |

