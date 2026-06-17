# ORDER_INGREDIENT_HISTORY

> This table will store a history of the ingredients for an order, when they are replaced with a different ingredient by the system.

**Description:** Order Ingredient History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | FK→ | The sequence number of the order action that was performed for this ingredient. |
| 2 | `COMP_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence number identifying the order of the ingredient. |
| 3 | `FREETEXT_DOSE` | VARCHAR(100) |  |  | Free text that can be input concerning a dose. Allows the user to write comments about the dose. |
| 4 | `INGREDIENT_ALTER_FLAG` | DOUBLE | NOT NULL |  | This flag will indicate what type of change occurred on the current order ingredient row. The possible values are: 1 - Modified, 2 - Add and 3 - Delete. |
| 5 | `INGREDIENT_ALTER_TRIGGER_CD` | DOUBLE | NOT NULL |  | This is a codified value that indicates what triggered the system to alter the ingredient. For example, Therapeutic Interchange - THERAPINTRCH. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order whose ingredient was altered. |
| 7 | `ORDER_INGREDIENT_HISTORY_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of this table. It is a number internally assigned by the system. |
| 8 | `STRENGTH` | DOUBLE |  |  | The strength of this ingredient. |
| 9 | `STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Codified unit of measure on strength for this ingredient. |
| 10 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order catalog synonym for this ingredient. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VOLUME` | DOUBLE |  |  | Volume of this ingredient. |
| 17 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Codified unit of measure on volume for this ingredient. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE` | [ORDER_ACTION](ORDER_ACTION.md) | `ACTION_SEQUENCE` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_ID` | [ORDER_ACTION](ORDER_ACTION.md) | `ORDER_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

