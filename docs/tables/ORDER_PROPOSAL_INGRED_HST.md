# ORDER_PROPOSAL_INGRED_HST

> This table will store a history of the ingredients for an order proposal when they are replaced with a different ingredient by the system.

**Description:** Order Proposal Ingredient History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FREETEXT_DOSE` | VARCHAR(255) |  |  | Free text that can be input concerning a dose. allows the user to write comments about the dose. |
| 2 | `INGREDIENT_ALTER_TRIGGER_CD` | DOUBLE | NOT NULL |  | This is a codified value that indicates what triggered the system to alter the ingredient. for example, therapeutic interchange - therapintrch. |
| 3 | `ORDER_PROPOSAL_INGREDIENT_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order proposal ingredient associated with this alteration. |
| 4 | `ORDER_PROPOSAL_INGRED_HST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ORDER_PROPOSAL_INGRED_HST table. |
| 5 | `STRENGTH` | DOUBLE |  |  | The strength of this ingredient. If specified, a Strength Unit Cd must be supplied. |
| 6 | `STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Codified unit of measure on strength for this ingredient. If specified, a Strength must be supplied. |
| 7 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order catalog synonym for this ingredient. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VOLUME` | DOUBLE |  |  | Volume of this ingredient. If specified, a Volume Unit Cd must be supplied. |
| 14 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Codified unit of measure on volume for this ingredient. If specified, a Volume must be supplied. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_PROPOSAL_INGREDIENT_ID` | [ORDER_PROPOSAL_INGREDIENT](ORDER_PROPOSAL_INGREDIENT.md) | `ORDER_PROPOSAL_INGREDIENT_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

