# DM_CMB_CONSTRAINTS

> Mirror table of user_constraints used for improved combine performance

**Description:** DM CMB CONSTRAINTS  
**Table type:** REFERENCE  
**Primary key:** `CONSTRAINT_NAME`  
**Columns:** 5  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONSTRAINT_NAME` | VARCHAR(30) | NOT NULL | PK | Name of ORACLE constraints |
| 2 | `CONSTRAINT_TYPE` | CHAR(1) | NOT NULL |  | Type of constraints. P for primary keys, R for foreign keys. |
| 3 | `R_CONSTRAINT_NAME` | VARCHAR(30) |  |  | Primary key constraint referenced by the foreign key. Only valid for constraint_type ="R" |
| 4 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of table the constraint is on. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_CMB_CONS_COLUMNS](DM_CMB_CONS_COLUMNS.md) | `CONSTRAINT_NAME` |

