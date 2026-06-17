# PIP_COLUMN

> PIP Column Definition.

**Description:** PIP COLUMN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_TYPE_CD` | DOUBLE | NOT NULL |  | Type of column |
| 2 | `PIP_COLUMN_ID` | DOUBLE | NOT NULL |  | Unique column identifier |
| 3 | `PIP_SECTION_ID` | DOUBLE | NOT NULL |  | ID of section column is within. |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of column definition. If this is 0, then this column appears on everyones section. Otherwise this column only appears on the identified users PIP. |
| 5 | `SEQUENCE` | DOUBLE |  |  | Sequence of column. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

