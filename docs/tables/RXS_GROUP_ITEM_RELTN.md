# RXS_GROUP_ITEM_RELTN

> The items that are part of a defined group.

**Description:** RxStation Group Item Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates if this item is to be included or not included in the dispense. |
| 2 | `DEFAULT_REASON_CD` | DOUBLE | NOT NULL |  | The reason an override was performed. |
| 3 | `DEFAULT_ROUTE_CD` | DOUBLE | NOT NULL |  | The default route for this item in this group. |
| 4 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item that is in the defined group. |
| 5 | `ITEM_QTY` | DOUBLE | NOT NULL |  | The default dose of the item in this group. |
| 6 | `RXS_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The group that this item belongs to. |
| 7 | `RXS_GROUP_ITEM_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RXS_GROUP_ITEM_RELTN table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `RXS_GROUP_ID` | [RXS_GROUP](RXS_GROUP.md) | `RXS_GROUP_ID` |

