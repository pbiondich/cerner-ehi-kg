# SCR_ACTION

> This table will store term and paragraph actions

**Description:** SCR Action  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXPRESSION_ID` | DOUBLE | NOT NULL | FK→ | The ID of the expression [Auto Generated]. |
| 2 | `EXPRESSION_OWNER_IND` | DOUBLE |  |  | Indicates whether it owns expressions or not. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique identifier of the row in the table defined by Parent Entity Name. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Identifies a table where additional information about this row could be found |
| 5 | `SCR_ACTION_CD` | DOUBLE | NOT NULL |  | scr action code such as Select, Equation, Required. |
| 6 | `SCR_ACTION_ID` | DOUBLE | NOT NULL |  | Primary key of SCR_ACTION. Auto generated |
| 7 | `TARGET_ENTITY_ID` | DOUBLE | NOT NULL |  | FK Reference the SCR_TERM_HIER table |
| 8 | `TARGET_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | target entity name |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPRESSION_ID` | [EXPRESSION](EXPRESSION.md) | `EXPRESSION_ID` |

