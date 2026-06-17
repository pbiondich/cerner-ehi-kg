# ITEM_ITEM_XREF

> Relates two item definitions in inventory as parent-child. Used in HLA to show the relationship between molecular primer kits and aliquotted molecular primer kits.

**Description:** Item to Item Cross Reference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_ITEM_ID` | DOUBLE | NOT NULL | FK→ | An aliquotted primer kit inventory item which is related to a specific non-aliquotted primer kit inventory item. It is a foreign key reference to the primary key of the item_definition table. |
| 2 | `PARENT_ITEM_ID` | DOUBLE | NOT NULL | FK→ | A non-aliquotted primer kit inventory item which is related to one or more aliquotted primer kit inventory items. It is a foreign key reference to the primary key of the item_definition table. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `PARENT_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

