# EXPRESSION

> Information pertaining to an expression that can be evaluated.

**Description:** Expression  
**Table type:** REFERENCE  
**Primary key:** `EXPRESSION_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXPRESSION_CKI` | CHAR(255) | NOT NULL |  | Globally unique identifier |
| 2 | `EXPRESSION_DISPLAY` | CHAR(512) | NOT NULL |  | Text representation of the expression |
| 3 | `EXPRESSION_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [EXPRESSION_COMP](EXPRESSION_COMP.md) | `EXPRESSION_ID` |
| [SCR_ACTION](SCR_ACTION.md) | `EXPRESSION_ID` |

