# GEL

> Identifies a molecular gel and its dimensions. The the gel may be related to one or more orders.

**Description:** Gel  
**Table type:** ACTIVITY  
**Primary key:** `GEL_NUMBER`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GEL_NUMBER` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies a gel. |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `X_DIM` | DOUBLE |  |  | Horizontal dimension of the HLA molecular typing gel. |
| 8 | `Y_DIM` | DOUBLE |  |  | Vertical dimension of the HLA molecular typing gel. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [GEL_LOADING](GEL_LOADING.md) | `GEL_NUMBER` |
| [GEL_RESULT_COMMENT](GEL_RESULT_COMMENT.md) | `GEL_NUMBER` |

