# OEN_SCRIPT_BODY

> script body

**Description:** Script body. Stores the actual script content in each line in separate row.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LINE_NBR` | DOUBLE | NOT NULL |  | Line number of the script. The script is broken up into multiple lines. This is the ordering of the lines. |
| 2 | `SCRIPT_ID` | DOUBLE | NOT NULL | FK→ | Script ID from OEN_SCRIPT_LIST. |
| 3 | `SCRIPT_LINE` | VARCHAR(255) |  |  | Actual content of the script line. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VERSION_NBR` | DOUBLE | NOT NULL |  | Version number of the script. When a script is check into/outof production, this number in incremented. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCRIPT_ID` | [OEN_SCRIPT_LIST](OEN_SCRIPT_LIST.md) | `SCRIPT_ID` |

