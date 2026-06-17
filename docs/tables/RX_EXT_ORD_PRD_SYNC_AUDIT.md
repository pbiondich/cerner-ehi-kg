# RX_EXT_ORD_PRD_SYNC_AUDIT

> Holds audit records for when order products are updated based on an external pharmacy supply.

**Description:** Pharmacy External Order Product Sync Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | The date that the record was created in the table. |
| 2 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The ITEM_ID of the original order product. |
| 3 | `NEW_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The new ITEM_ID of the order product if it was successfully synced |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The ORDER_ID of the order that qualified for syncing |
| 5 | `RX_EXT_ORD_PRD_SYNC_AUDIT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_EXT_ORD_PRD_SYNC_AUDIT table. |
| 6 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Denotes whether or not the order product was synced to an external order product successfully. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `NEW_ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

