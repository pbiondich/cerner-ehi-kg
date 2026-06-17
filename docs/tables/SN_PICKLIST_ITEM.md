# SN_PICKLIST_ITEM

> Unique Item contained on the given picklist

**Description:** SurgiNet Picklist Item  
**Table type:** ACTIVITY  
**Primary key:** `SN_PICKLIST_ITEM_ID`  
**Columns:** 19  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AD_HOC_IND` | DOUBLE | NOT NULL |  | Indicates that this item was added by the user after the picklist has been generated |
| 2 | `DOC_AT_COMPONENT_IND` | DOUBLE | NOT NULL |  | Indicates that the documentation of use/waste/reutrn should be at the compoent level. Should only be set if this item is a set/pack item and the build setting for the item is that the children generate supply transactions |
| 3 | `EQUIPMENT_TRACKED_IND` | DOUBLE | NOT NULL |  | Indicates that the item is an equipment type that requires instance information when filled |
| 4 | `EXPIRATION_DATE_IND` | DOUBLE | NOT NULL |  | Indicates whether this item requires the expiration date to be documented |
| 5 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Inventory Item represented by this row. From the ITEM_DEFINITION table |
| 6 | `LOT_IND` | DOUBLE | NOT NULL |  | Indicates whether this item requires the lot number to be documented |
| 7 | `MANUFACTURE_DATE_IND` | DOUBLE | NOT NULL |  | Indicates whether this item requires the manufacture date to be documented |
| 8 | `PACK_IND` | DOUBLE | NOT NULL |  | Indictes that this item is a parent level item and that it has children components contained within it |
| 9 | `PARENT_PICKLIST_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Specifies the parent set/pack that this item belongs to |
| 10 | `REPLACES_ITEM_ID` | DOUBLE |  | FK→ | The item on the picklist that this item replaces |
| 11 | `SERIAL_NBR_IND` | DOUBLE | NOT NULL |  | Indicates whether this item requires the serial number to be documented |
| 12 | `SN_PICKLIST_ID` | DOUBLE | NOT NULL | FK→ | Picklist Identifier that this item applies to |
| 13 | `SN_PICKLIST_ITEM_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `USE_COMP_HIERARCHY_IND` | DOUBLE | NOT NULL |  | If the item is a set/pack, If true this indicates whether the components of the set/pack should follow the component hierarchy. If False, componentes of the set/pack would follow the normal Fill/Return hierarchy |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `PARENT_PICKLIST_ITEM_ID` | [SN_PICKLIST_ITEM](SN_PICKLIST_ITEM.md) | `SN_PICKLIST_ITEM_ID` |
| `REPLACES_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `SN_PICKLIST_ID` | [SN_PICKLIST](SN_PICKLIST.md) | `SN_PICKLIST_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SN_PICKLIST_ITEM](SN_PICKLIST_ITEM.md) | `PARENT_PICKLIST_ITEM_ID` |
| [SN_PICKLIST_ITEM_DETAIL](SN_PICKLIST_ITEM_DETAIL.md) | `SN_PICKLIST_ITEM_ID` |
| [SN_PICKLIST_REQUEST](SN_PICKLIST_REQUEST.md) | `SN_PICKLIST_ITEM_ID` |

