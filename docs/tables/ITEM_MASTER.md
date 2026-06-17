# ITEM_MASTER

> Contains all Inventory Items tracked internally by an entity.

**Description:** Item Master  
**Table type:** REFERENCE  
**Primary key:** `ITEM_ID`  
**Columns:** 14  
**Referenced by:** 22 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost Center |
| 2 | `COUNTABLE_IND` | DOUBLE |  |  | Indicates whether or not this item is considered countable. |
| 3 | `CRITICAL_IND` | DOUBLE |  |  | Indicates if this item is critical in order for a procedure to be performed. |
| 4 | `FDA_REPORTABLE_IND` | DOUBLE |  |  | Indicates this item is reportable to the FDA. |
| 5 | `ITEM_ID` | DOUBLE | NOT NULL | PK | Primary key. |
| 6 | `SCHEDULABLE_IND` | DOUBLE |  |  | Indicates if this item is schedulable. |
| 7 | `STERILIZATION_REQUIRED_IND` | DOUBLE |  |  | Indicates if this item needs sterilization prior to use. |
| 8 | `STORAGE_REQUIREMENT_CD` | DOUBLE | NOT NULL |  | Describes how to store an item. |
| 9 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | Sub Account |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (22)

| From table | Column |
|------------|--------|
| [ADDITIONAL_AMOUNT_DEF](ADDITIONAL_AMOUNT_DEF.md) | `ITEM_ID` |
| [CASE_CART_PICK_LIST](CASE_CART_PICK_LIST.md) | `ITEM_ID` |
| [DIST_LINE_DETAIL](DIST_LINE_DETAIL.md) | `ACTUAL_ITEM_ID` |
| [EQUIPMENT_MASTER](EQUIPMENT_MASTER.md) | `ITEM_ID` |
| [LINE_ITEM](LINE_ITEM.md) | `ITEM_MASTER_ID` |
| [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `ITEM_ID` |
| [RECEIPT_LINE_ITEM](RECEIPT_LINE_ITEM.md) | `ACTUAL_ITEM_ID` |
| [SA_REF_DILUENT](SA_REF_DILUENT.md) | `ITEM_ID` |
| [SA_REF_FLUID](SA_REF_FLUID.md) | `ITEM_ID` |
| [SA_REF_ITEM](SA_REF_ITEM.md) | `ITEM_ID` |
| [SA_REF_MACRO_FLUID](SA_REF_MACRO_FLUID.md) | `ITEM_ID` |
| [SA_REF_MACRO_ITEM](SA_REF_MACRO_ITEM.md) | `ITEM_ID` |
| [SA_REF_MACRO_MEDICATION](SA_REF_MACRO_MEDICATION.md) | `DILUENT_ITEM_ID` |
| [SA_REF_MACRO_MEDICATION](SA_REF_MACRO_MEDICATION.md) | `ITEM_ID` |
| [SA_REF_MEDICATION](SA_REF_MEDICATION.md) | `ITEM_ID` |
| [SA_TODO_FLUID](SA_TODO_FLUID.md) | `ITEM_ID` |
| [SA_TODO_ITEM](SA_TODO_ITEM.md) | `ITEM_ID` |
| [SA_TODO_MEDICATION](SA_TODO_MEDICATION.md) | `DILUENT_ITEM_ID` |
| [SA_TODO_MEDICATION](SA_TODO_MEDICATION.md) | `ITEM_ID` |
| [SN_PREFCARD_MPAGE_SNOOZE](SN_PREFCARD_MPAGE_SNOOZE.md) | `ITEM_ID` |
| [TRACKING_ITEM](TRACKING_ITEM.md) | `INVENTORY_ID` |

