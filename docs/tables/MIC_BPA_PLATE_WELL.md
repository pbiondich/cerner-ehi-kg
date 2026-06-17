# MIC_BPA_PLATE_WELL

> This reference table contains row and column positions for a Breakpoint plate definition.

**Description:** Microbiology Breakpoint Plate Well  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_POSITION` | DOUBLE | NOT NULL |  | This field defines active well positions. This field is used in conjunction with the ROW_POSITION column. |
| 2 | `PLATE_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the Breakpoint Plate Definition. |
| 3 | `ROW_POSITION` | DOUBLE | NOT NULL |  | This field defines active well positions. This field is used in conjunction with the COLUMN_POSITION column. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

