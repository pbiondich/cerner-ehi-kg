# BR_BB_MODEL_ALIAS

> Stores proposed alias for bloodbank models

**Description:** BR_BB_MODEL_ALIAS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABORH_CD` | DOUBLE | NOT NULL |  | Code value from code set 1640 for a matching aborh |
| 2 | `BR_BB_MODEL_ALIAS` | VARCHAR(40) | NOT NULL |  | Name of the bloodbank aborh alias |
| 3 | `BR_BB_MODEL_ALIAS_ID` | DOUBLE | NOT NULL |  | Unique id for the row |
| 4 | `BR_BB_MODEL_ID` | DOUBLE | NOT NULL | FK→ | Id from the br_bb_model table |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_BB_MODEL_ID` | [BR_BB_MODEL](BR_BB_MODEL.md) | `BR_BB_MODEL_ID` |

