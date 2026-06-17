# RX_PRODUCT_ASSIGN_AUDIT

> The table is used to log detailed audit information when system attempts to assign pharmacy products automatically. It records significant steps during auto product assign process.

**Description:** Pharmacy product assign audit table.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the catalog group that is being tried for product assign. |
| 2 | `CATALOG_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the catalog item that was selected during auto product assignment. |
| 3 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the product on which matching is performed. For records with item_id valued, catalog_item_id should be populated. Item_id comes from item_id in medication_definition table. |
| 4 | `REPORT_LEVEL_FLAG` | DOUBLE | NOT NULL |  | Report level. 0: audit - find a match successfully. Matching item is recorded in set_item_id or item_id field. 1: info - fail to match because of reasons recorded in status_number and status_string fields 2: debug - additional information about a specific event with details recorded in status_number and status_string fields. |
| 5 | `SET_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the IV set on which product matching is performed. Set_item_id comes from item_id in medication_definition table. |
| 6 | `STATUS_MESSAGE` | VARCHAR(2000) | NOT NULL |  | Text description of a specific event that occurred during the auto product assignment process. |
| 7 | `STATUS_NUMBER` | DOUBLE | NOT NULL |  | Enumerated number used to identify a specific event that occurred during the auto product assignment process. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_GROUP_ID` | [RX_PRODUCT_ASSIGN_GROUP_AUDIT](RX_PRODUCT_ASSIGN_GROUP_AUDIT.md) | `CATALOG_GROUP_ID` |
| `CATALOG_ITEM_ID` | [RX_PRODUCT_ASSIGN_ITEM_AUDIT](RX_PRODUCT_ASSIGN_ITEM_AUDIT.md) | `CATALOG_ITEM_ID` |
| `ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `SET_ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |

