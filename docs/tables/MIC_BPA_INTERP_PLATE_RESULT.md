# MIC_BPA_INTERP_PLATE_RESULT

> This reference table contains a breakpoint result value for a breakpoint antibiotic plate. The combination of these entries define a growth pattern, which results in the dilution result value contained in the MIC_INTERP_RESULT table.

**Description:** Microbiology Breakpoint Interp Plate Result  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_PLATE_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the Breakpoint antibiotic plate. |
| 2 | `BPA_RESULT_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the Breakpoint plate result. |
| 3 | `INTERP_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the MIC_BPA_INTERP table. This column in conjunction with the SEQUENCE column can be used to join to the MIC_BPA_INTERP_RESULT table. |
| 4 | `SEQUENCE` | DOUBLE | NOT NULL | FK→ | This field is used in conjunction with the INTERP_ID to identify a unique breakpoint result growth pattern/dilution result. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTERP_ID` | [MIC_BPA_INTERP_RESULT](MIC_BPA_INTERP_RESULT.md) | `INTERP_ID` |
| `SEQUENCE` | [MIC_BPA_INTERP_RESULT](MIC_BPA_INTERP_RESULT.md) | `SEQUENCE` |

