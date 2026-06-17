# CODE_VALUE_GROUP

> Used to create logical groupings of code_values

**Description:** CODE VALUE GROUP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_CODE_VALUE` | DOUBLE | NOT NULL | FK→ | The code value of the child record |
| 2 | `CODE_SET` | DOUBLE |  |  | The code set that the child code value belongs to. This is a denormalized column and reads should be from Code_value.code_set of the child code_value |
| 3 | `COLLATION_SEQ` | DOUBLE |  |  | Ordering field for grouping |
| 4 | `PARENT_CODE_VALUE` | DOUBLE | NOT NULL | FK→ | The code value of the parent record |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_CODE_VALUE` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PARENT_CODE_VALUE` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

