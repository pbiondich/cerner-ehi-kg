# DM_CMB_CONS_COLUMNS

> Mirror table of user_cons_columns. Used for improved combine performance.

**Description:** DM CMB CONS COLUMNS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Name of the column in the constraint. |
| 2 | `CONSTRAINT_NAME` | VARCHAR(30) | NOT NULL | FK→ | Name of the ORACLE constraints. |
| 3 | `POSITION` | DOUBLE | NOT NULL |  | Position the column holds in the constraint. |
| 4 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of the table the constraint is on. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONSTRAINT_NAME` | [DM_CMB_CONSTRAINTS](DM_CMB_CONSTRAINTS.md) | `CONSTRAINT_NAME` |

