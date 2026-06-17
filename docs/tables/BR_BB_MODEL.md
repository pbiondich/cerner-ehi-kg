# BR_BB_MODEL

> Stores proposed models for bloodbank aliasing

**Description:** BR_BB_MODEL  
**Table type:** REFERENCE  
**Primary key:** `BR_BB_MODEL_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_BB_MODEL_ID` | DOUBLE | NOT NULL | PK | Unique id for the row |
| 2 | `MODEL_CD` | DOUBLE | NOT NULL |  | Code value from code set 73 if the proposed model has a millennium match |
| 3 | `MODEL_NAME` | VARCHAR(60) | NOT NULL |  | Name of the proposed model |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_BB_MODEL_ALIAS](BR_BB_MODEL_ALIAS.md) | `BR_BB_MODEL_ID` |

