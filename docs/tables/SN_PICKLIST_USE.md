# SN_PICKLIST_USE

> Defines the quantity used of an item instance on the picklist for a procedure

**Description:** Surginet Picklist Use  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EQUIPMENT_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the equipment instance at the time the instance was used |
| 2 | `SN_PICKLIST_ITEM_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | The instance of an item on the picklist that the quantity is being used |
| 3 | `SN_PICKLIST_USE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `SURG_CASE_PROC_ID` | DOUBLE | NOT NULL | FK→ | The surgical procedure that the instance of the item was used for |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `USE_DT_TM` | DATETIME |  |  | The Date and Time that the quantity was used |
| 11 | `USE_QTY` | DOUBLE | NOT NULL |  | The quantity of the instance of an item that was used |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SN_PICKLIST_ITEM_DETAIL_ID` | [SN_PICKLIST_ITEM_DETAIL](SN_PICKLIST_ITEM_DETAIL.md) | `SN_PICKLIST_ITEM_DETAIL_ID` |
| `SURG_CASE_PROC_ID` | [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SURG_CASE_PROC_ID` |

