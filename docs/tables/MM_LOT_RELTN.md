# MM_LOT_RELTN

> Stores the relationship between Receipt_Line_item and Lot_Number_info and also the relationship between Dist_Line_Detail and Lot_Number_Info.

**Description:** Materials Management Lot Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEFORE_TRANSFER_QTY` | DOUBLE | NOT NULL |  | Quantity before lot transfer. |
| 2 | `INCREASE_IND` | DOUBLE | NOT NULL |  | Used to determine if the quantity documented is increasing or decreasing the lot. |
| 3 | `LOT_EXP_SOON_IND` | DOUBLE | NOT NULL |  | For that lot, for this distribution, indicates if the lot chosen had an expiration date that was defined as "soon". |
| 4 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from LOT_NUMBER_INFO. This is the lot number for the line item. |
| 5 | `LOT_QTY` | DOUBLE | NOT NULL |  | The quantity of the item on the line item in the particular lot. |
| 6 | `MM_LOT_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated primary key for the MM_LOT_RELTN table. |
| 7 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the package type for the lot. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique identifier from the tables that appear in column parent_entity_name. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the parent table that relates to this component. |
| 10 | `PARENT_LOT_NUMBER_ID` | DOUBLE | NOT NULL | FK→ | In the cases where an item is part of a compound, this identifies the lot number of the compound of which it is a part. |
| 11 | `TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | Used to capture the altered lot_qty per transaction |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `PARENT_LOT_NUMBER_ID` | [LOT_NUMBER_INFO](LOT_NUMBER_INFO.md) | `LOT_NUMBER_ID` |
| `TRANSACTION_ID` | [MM_TRANS_HEADER](MM_TRANS_HEADER.md) | `TRANSACTION_ID` |

