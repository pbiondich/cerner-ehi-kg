# CASE_CART_PICK_LIST

> Contains all of the items on a case cart pick list, including requested qty, fill qty, used qty, returned qty, wasted qty, charge qty

**Description:** Case Cart Pick List  
**Table type:** ACTIVITY  
**Primary key:** `CASE_CART_PICK_LIST_ID`  
**Columns:** 50  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AVG_COST` | DOUBLE |  |  | Average cost of the pick list item. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CASE_CART_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the case_cart table indicating the case cart associated with this case cart pick list item |
| 8 | `CASE_CART_PICK_LIST_ID` | DOUBLE | NOT NULL | PK | The primary key, uniquely identifying a row on this table |
| 9 | `CHARGE_DUR` | DOUBLE |  |  | The duration to be used in calculating charges associated with this case cart pick list item |
| 10 | `CHARGE_QTY` | DOUBLE |  |  | Charge Qty for the Pick List Item |
| 11 | `CHARGE_UNITS` | DOUBLE |  |  | The units to be used in calculating the charges associated with this case cart pick list item |
| 12 | `COST` | DOUBLE |  |  | Cost of the Pick List Item |
| 13 | `COST_TYPE_CD` | DOUBLE | NOT NULL |  | The cost associated with the item for departmental charging and general ledger updates |
| 14 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 15 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 16 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 17 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 18 | `CURRENT_IND` | DOUBLE |  |  | An indicator of whether or not this is a current item on the case cart pick list |
| 19 | `DUP_IND` | DOUBLE |  |  | An indicator of whether or not this case cart pick list item is a duplicate with an item from another procedure (for multiple procedure cases only) |
| 20 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 21 | `FILL_LOCN_CD` | DOUBLE | NOT NULL |  | The inventory location this case cart pick list item was filled from |
| 22 | `FILL_QTY` | DOUBLE |  |  | The quantity of this item that was filled |
| 23 | `FREE_TEXT_ITEM_DESC` | VARCHAR(200) |  |  | A free-text description of this case cart pick list item. This column will only be populated if the item is not found in the item_master table. |
| 24 | `HOLD_QTY` | DOUBLE |  |  | The requested hold quantity for this item. Defaulted from the preference card |
| 25 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Item Id for the Pick List Item |
| 26 | `LAST_COST` | DOUBLE |  |  | Last cost of the pick list item. |
| 27 | `LINE_ITEM_ID` | DOUBLE | NOT NULL |  | A reference to the line_item table indicating which line item on the requisition this pick list item refers to |
| 28 | `MERGED_ITEM_FLAG` | DOUBLE |  |  | An indicator of whether this duplicate item has been merged |
| 29 | `OBJECT_TYPE_FLAG` | DOUBLE |  |  | An indicator of the type of object this free-text case cart pick list item is, i.e. Equipment, Medication, Implant |
| 30 | `OPEN_QTY` | DOUBLE |  |  | The requested open quantity associated with this case cart pick list item |
| 31 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | A reference to either the order_catalog table or the item_definition table depending on the type of item -- either inventory item or medication |
| 32 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table this item is associated with -- either order_catalog or item_definition, depending on the type of item (inventory item or medication) |
| 33 | `PARENT_PACK_ID` | DOUBLE | NOT NULL |  | The parent pack id if this item is a component of a pack, else it is 0. |
| 34 | `PREF_CARD_TYPE_FLAG` | DOUBLE |  |  | The type of preference card associated with this case cart pick list item, i.e. surgeon/procedure |
| 35 | `QTY_USED` | DOUBLE |  |  | The quantity of this case cart pick list item that was used |
| 36 | `REQUEST_QTY` | DOUBLE |  |  | The quantity of this case cart pick list item that was requested |
| 37 | `RETURN_LOCN_CD` | DOUBLE | NOT NULL |  | The inventory location that this case cart pick list item was returned to. |
| 38 | `RETURN_QTY` | DOUBLE |  |  | The quantity of this case cart pick list item that was returned |
| 39 | `STATUS_FLAG` | DOUBLE |  |  | NOT CURRENTLY BEING USED (always being set to 1) |
| 40 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the surgical_case table indicating the surgical case associated with this case cart pick list item |
| 41 | `SURG_CASE_PROC_ID` | DOUBLE | NOT NULL | FK→ | Surgical Case Procedure associated with this Pick List Item |
| 42 | `SURG_PROC_GRP_DET_ID` | DOUBLE | NOT NULL |  | A reference (foreign key) to the surg_proc_group_detail indicating the surgical procedure/group associated with this case cart pick list item |
| 43 | `SURG_PROC_GRP_ID` | DOUBLE | NOT NULL |  | **OBSOLETE**A reference (foreign key) to the surgical_procedure_group table indicating the surgical procedure group associated with this case cart pick list item |
| 44 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 45 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 46 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 47 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 48 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 49 | `WASTED_QTY` | DOUBLE |  |  | The quantity of this case cart pick list item that was wasted |
| 50 | `WASTED_REASON_CD` | DOUBLE | NOT NULL |  | The reason this pick list item was wasted |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_CART_ID` | [CASE_CART](CASE_CART.md) | `CASE_CART_ID` |
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |
| `SURG_CASE_PROC_ID` | [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SURG_CASE_PROC_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCHED_CASE_PICK_LIST](SCHED_CASE_PICK_LIST.md) | `CASE_CART_PICK_LIST_ID` |

