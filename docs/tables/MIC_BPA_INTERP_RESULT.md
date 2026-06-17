# MIC_BPA_INTERP_RESULT

> This reference table contains a dilution result value for a define breakpoint result growth pattern. The biochemical result values that make up the growth pattern are contained in the MIC_INTERP_PLATE_RESULT table.

**Description:** Microbiology Breakpoint Interp Result  
**Table type:** REFERENCE  
**Primary key:** `INTERP_ID`, `SEQUENCE`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INTERP_ID` | DOUBLE | NOT NULL | PK FK→ | This field contains the foreign key value used to join to the parent MIC_BPA_INTERP table. |
| 2 | `RESULT_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the susceptibility alpha result. |
| 3 | `SEQUENCE` | DOUBLE | NOT NULL | PK | This field is used in conjunction with the INTERP_ID to identify a unique breakpoint result growth pattern/dilution result. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTERP_ID` | [MIC_BPA_INTERP](MIC_BPA_INTERP.md) | `INTERP_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_BPA_INTERP_PLATE_RESULT](MIC_BPA_INTERP_PLATE_RESULT.md) | `INTERP_ID` |
| [MIC_BPA_INTERP_PLATE_RESULT](MIC_BPA_INTERP_PLATE_RESULT.md) | `SEQUENCE` |

