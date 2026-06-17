# EXPRESSION_COMP

> Contains an entry for each component (operators and operands) of an expression that can be evaluated

**Description:** Expression Component  
**Table type:** REFERENCE  
**Primary key:** `EXPRESSION_COMP_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXPRESSION_COMP_ID` | DOUBLE | NOT NULL | PK | Primary key of this table (Auto Generated) |
| 2 | `EXPRESSION_COMP_ROLE_CD` | DOUBLE | NOT NULL |  | The role of this expression component such as constant, value, operator, etc. |
| 3 | `EXPRESSION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from table Expression. It is the Primary ID of the Expression table |
| 4 | `PARENT_EXPRESSION_COMP_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the parent of the expression component |
| 5 | `SEQUENCE_NUMBER` | DOUBLE |  |  | The sequence number of the expression comp |
| 6 | `UNITS_CD` | DOUBLE | NOT NULL |  | Code that identifies what type of units are in this table. Examples are Day, Foot, Dose, etc. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VALUE_DT_TM` | DATETIME |  |  | Used if the expression has a date or time in it. |
| 13 | `VALUE_FKEY_ENTITY_NAME` | VARCHAR(255) | NOT NULL |  | Foreign key entity name the row is pointing back to. |
| 14 | `VALUE_FKEY_ID` | DOUBLE | NOT NULL |  | The value foreign key identifier |
| 15 | `VALUE_NUMBER` | DOUBLE |  |  | Number values for the expression |
| 16 | `VALUE_TEXT` | VARCHAR(512) |  |  | Expression strings or CKI's of other existing terms. CKI stands for Cerner Knowledge Index. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPRESSION_ID` | [EXPRESSION](EXPRESSION.md) | `EXPRESSION_ID` |
| `PARENT_EXPRESSION_COMP_ID` | [EXPRESSION_COMP](EXPRESSION_COMP.md) | `EXPRESSION_COMP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EXPRESSION_COMP](EXPRESSION_COMP.md) | `PARENT_EXPRESSION_COMP_ID` |

