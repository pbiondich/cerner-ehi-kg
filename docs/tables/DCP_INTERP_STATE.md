# DCP_INTERP_STATE

> Transition States for interpretations.

**Description:** DCP INTERP STATE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DCP_INTERP_ID` | DOUBLE | NOT NULL | FK→ | Id of interpretation |
| 2 | `DCP_INTERP_STATE_ID` | DOUBLE | NOT NULL |  | unique identifier |
| 3 | `FLAGS` | DOUBLE | NOT NULL |  | flags 1 - Numeric Component |
| 4 | `INPUT_ASSAY_CD` | DOUBLE | NOT NULL |  | Task Assay Code of input. |
| 5 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | nomenclature id of input corresponding to transition_assay_cd |
| 6 | `NUMERIC_HIGH` | DOUBLE |  |  | numeric high value |
| 7 | `NUMERIC_LOW` | DOUBLE |  |  | numeric low value |
| 8 | `RESULTING_STATE` | DOUBLE | NOT NULL |  | Next state as a result of current input |
| 9 | `RESULT_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Nomenclature Id that should be returned as result. |
| 10 | `RESULT_VALUE` | DOUBLE |  |  | Numeric Value that should be returned as a result. |
| 11 | `STATE` | DOUBLE | NOT NULL |  | identifier of the state |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_INTERP_ID` | [DCP_INTERP](DCP_INTERP.md) | `DCP_INTERP_ID` |

