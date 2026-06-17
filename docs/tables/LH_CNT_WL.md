# LH_CNT_WL

> This table holds various worklist id's used to determine which worklist filters will be returned back to a worklist mpage.

**Description:** Lighthouse Content Worklist  
**Table type:** REFERENCE  
**Primary key:** `LH_CNT_WL_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LH_CNT_WL_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_CNT_WL table. |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `WORKLIST_MEAN` | VARCHAR(50) | NOT NULL |  | Unique name given to each worklist to help in various filtering processes. |
| 8 | `WORKLIST_NAME` | VARCHAR(255) | NOT NULL |  | A more readable version of the Worklist Mean. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [LH_CNT_WL_FLTR_LIST](LH_CNT_WL_FLTR_LIST.md) | `LH_CNT_WL_ID` |
| [LH_CNT_WL_POP](LH_CNT_WL_POP.md) | `LH_CNT_WL_ID` |
| [LH_CNT_WL_POP_H](LH_CNT_WL_POP_H.md) | `LH_CNT_WL_ID` |

