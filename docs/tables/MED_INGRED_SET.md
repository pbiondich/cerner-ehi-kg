# MED_INGRED_SET

> Contains items in two types of sets. IV Sets contain ingredients that make up the IV. When ordered, all will be contained on one order. Order Sets can be made up of components that are either IV Sets or individual ingredients. When ordered, a separate order will be created for each component in the Order Set.

**Description:** Medical Ingredient Set  
**Table type:** REFERENCE  
**Primary key:** `MED_INGRED_SET_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASE_IND` | DOUBLE |  |  | Indicates which child ingredient is the base for the compound. |
| 2 | `CHILD_ITEM_ID` | DOUBLE | NOT NULL | FK→ | ITEM_ID of a component ingredient of the set. |
| 3 | `CHILD_MED_PROD_ID` | DOUBLE | NOT NULL | FK→ | The id that identifies the actual pharmacy product item of the child item. |
| 4 | `CHILD_PKG_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The type of base package for the child ingredient. |
| 5 | `CMPD_QTY` | DOUBLE |  |  | The quantity for the child ingredient used within the compound. |
| 6 | `DEFAULT_ACTION_CD` | DOUBLE | NOT NULL |  | Indicates whether or not to include, exclude, or review the child ingredient for an order set. |
| 7 | `INC_IN_TOTAL_IND` | DOUBLE |  |  | Indicates whether or not the ingredient is included in the total volume. |
| 8 | `MED_INGRED_SET_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the MED_INGRED_SET table. |
| 9 | `NORMALIZED_RATE_IND` | DOUBLE | NOT NULL |  | Indicates which one item in a set (if any) is associated to the normalized rate defined on the set. |
| 10 | `PARENT_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The ITEM_ID of the set. |
| 11 | `SEQUENCE` | DOUBLE | NOT NULL |  | A number that orders the components of a set. |
| 12 | `STRENGTH` | DOUBLE | NOT NULL |  | Premix ingredient strength. |
| 13 | `STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Premix ingredient strength unit. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VOLUME` | DOUBLE | NOT NULL |  | Premix ingredient volume |
| 20 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Premix ingredient volume unit |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `CHILD_MED_PROD_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |
| `CHILD_PKG_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `PARENT_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MED_IDENTIFIER](MED_IDENTIFIER.md) | `MED_INGRED_SET_ID` |

