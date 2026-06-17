# TPL_APPL_CTX_PARAM

> Stores the context parameters for the applications launched from the build and launch tool.

**Description:** Third Party Launch Application Context Parameter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPL_CTX_PARAM_ID` | DOUBLE | NOT NULL |  | Generated unique ID for the table |
| 2 | `APPL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the TPL_APPL table. |
| 3 | `CTX_CD` | DOUBLE | NOT NULL |  | Code value for the new code set used to maintain the context params. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPL_ID` | [TPL_APPL](TPL_APPL.md) | `APPL_ID` |

