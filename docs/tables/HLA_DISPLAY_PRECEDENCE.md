# HLA_DISPLAY_PRECEDENCE

> HLA Display Precedence for assay loci and event sequences.

**Description:** HLA Display Precedence  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HLA_DISPLAY_PRECEDENCE_ID` | DOUBLE | NOT NULL |  | This column is used to uniquely identify a row on the HLA_DISPLAY_PRECEDENCE table. |
| 2 | `PRECEDENCE_DESC` | VARCHAR(80) | NOT NULL |  | Contains the user defined precedence description associated with this task assay code. |
| 3 | `PRECEDENCE_NBR` | DOUBLE | NOT NULL |  | Contains the user defined precedence number associated with this task assay code. |
| 4 | `PRECEDENCE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of precedence for this row. |
| 5 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Identifies the procedure associated to this row. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

