# MP_COMPONENT_COMPONENT_R

> Contains relationships between components of a group and the child components they require to run successfully.

**Description:** MP COMPONENT COMPONENT RELTN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_MP_COMPONENT_ID` | DOUBLE | NOT NULL | FK→ | A child Component value from the MP_COMPONENT table. |
| 2 | `MP_COMPONENT_COMPONENT_R_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `MP_COMPONENT_ID` | DOUBLE | NOT NULL | FK→ | The Parent Component in a component relationship. A value from the MP_COMPONENT table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_MP_COMPONENT_ID` | [MP_COMPONENT](MP_COMPONENT.md) | `MP_COMPONENT_ID` |
| `MP_COMPONENT_ID` | [MP_COMPONENT](MP_COMPONENT.md) | `MP_COMPONENT_ID` |

