# CE_DRAFT

> Stores information about a set of clinical event rows that are in a draft state.

**Description:** Clinical Event Draft  
**Table type:** ACTIVITY  
**Primary key:** `CE_DRAFT_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_DRAFT_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the CE_DRAFT table. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Identifies the date & time the record was created. |
| 3 | `ENTRY_MODE_CD` | DOUBLE | NOT NULL |  | The application that created the draft. |
| 4 | `LAST_MODIFIED_DT_TM` | DATETIME | NOT NULL |  | The date and time when any portion of the draft was last modified. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CE_DRAFT_RELTN](CE_DRAFT_RELTN.md) | `CE_DRAFT_ID` |
| [NC_CHARTED_VIEW](NC_CHARTED_VIEW.md) | `CE_DRAFT_ID` |

