# SN_PICKLIST_REQUEST

> Defines the quantity requested of an item on the picklist for a specified procedure

**Description:** Surginet Picklist Request  
**Table type:** ACTIVITY  
**Primary key:** `SN_PICKLIST_REQUEST_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HOLD_QTY` | DOUBLE | NOT NULL |  | The quantity of the rquested item that should be picked, but not opened |
| 2 | `MERGE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of merging that was done for the item if it was requested for multiple procedures for the surgical case |
| 3 | `OPEN_QTY` | DOUBLE | NOT NULL |  | The quantity of the requested item that should be opened |
| 4 | `ORIGINAL_HOLD_QTY` | DOUBLE | NOT NULL |  | The original hold quantity of the item prior to optimization |
| 5 | `ORIGINAL_OPEN_QTY` | DOUBLE | NOT NULL |  | The original open quantity of the item prior to optimization |
| 6 | `ORIGINAL_REQUEST_QTY` | DOUBLE | NOT NULL |  | The original requested quantity of the item prior to optimization |
| 7 | `REQUEST_DT_TM` | DATETIME | NOT NULL |  | The date/time the request for items was made |
| 8 | `REQUEST_QTY` | DOUBLE | NOT NULL |  | The quantity of the item being requested |
| 9 | `SN_PICKLIST_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item on the picklist that the quantity is being requested for |
| 10 | `SN_PICKLIST_REQUEST_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 11 | `SURG_CASE_PROC_ID` | DOUBLE | NOT NULL | FK→ | The surgical procedure that the item is being requested for |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SN_PICKLIST_ITEM_ID` | [SN_PICKLIST_ITEM](SN_PICKLIST_ITEM.md) | `SN_PICKLIST_ITEM_ID` |
| `SURG_CASE_PROC_ID` | [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SURG_CASE_PROC_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_PICKLIST_REQUEST_PC](SN_PICKLIST_REQUEST_PC.md) | `SN_PICKLIST_REQUEST_ID` |

