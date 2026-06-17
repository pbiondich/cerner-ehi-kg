# SN_PICKLIST_RETURN

> Defines the quantity of an item instance on a picklist that was returned

**Description:** Surginet Picklist Return  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RETURN_DT_TM` | DATETIME |  |  | The Date and Time that the quantity was returned |
| 2 | `RETURN_LOCATION_CD` | DOUBLE | NOT NULL |  | The location the instance of an item was returned to |
| 3 | `RETURN_QTY` | DOUBLE | NOT NULL |  | The quantity of the instance of an item that was returned |
| 4 | `RETURN_STATUS_FLAG` | DOUBLE | NOT NULL |  | Defines where in the process the item was returned (during fill, in the OR, etc.) - 0=Returned During Fill 1=Returned In OR 2=Marked for Return 3=Return Completed |
| 5 | `SN_PICKLIST_ITEM_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | The instance of an item on the picklist that the quantity is being returned |
| 6 | `SN_PICKLIST_RETURN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SN_PICKLIST_ITEM_DETAIL_ID` | [SN_PICKLIST_ITEM_DETAIL](SN_PICKLIST_ITEM_DETAIL.md) | `SN_PICKLIST_ITEM_DETAIL_ID` |

