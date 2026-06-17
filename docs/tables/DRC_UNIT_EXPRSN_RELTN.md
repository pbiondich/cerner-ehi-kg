# DRC_UNIT_EXPRSN_RELTN

> Reference data that defines the unit of measure expressions for dose range checking

**Description:** Dose Range Checking Unit Expression Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DRC_UNIT_EXPRSN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to drc_unit_expression table. |
| 2 | `DRC_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to drc_unit table. |
| 3 | `RELATION_NUMERATOR_IND` | DOUBLE | NOT NULL |  | A value of 1 indicates the unit is in the numerator of the expression and a value of 0 indicates the unit is in the denominator of the expression. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRC_UNIT_EXPRSN_ID` | [DRC_UNIT_EXPRSN](DRC_UNIT_EXPRSN.md) | `DRC_UNIT_EXPRSN_ID` |
| `DRC_UNIT_ID` | [DRC_UNIT](DRC_UNIT.md) | `DRC_UNIT_ID` |

