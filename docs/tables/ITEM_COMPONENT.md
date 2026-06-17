# ITEM_COMPONENT

> Contains a listing of an item's components

**Description:** ITEM COMPONENT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPONENT_ID` | DOUBLE | NOT NULL | FK→ | Actual component item. Foreign key to item_definition table. |
| 2 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Application which created this row |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date/time this entry was created. |
| 4 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 5 | `CREATE_TASK` | DOUBLE | NOT NULL |  | Task which created this row |
| 6 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Item which is a pack or set. Foreign key to item_definition table. |
| 7 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Package size for this component |
| 8 | `QTY` | DOUBLE | NOT NULL |  | Quantity of component in this pack. |
| 9 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence of components used for display purposes |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMPONENT_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

