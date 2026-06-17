# RAD_DOSE_SCAN_ORDER_R

> Stores the relationship between a scan and an order.

**Description:** RadNet Dose Scan Order Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The Order_Id is a foreign key to the Order_Radiology table. It identifies the order this scan is for. |
| 2 | `RAD_DOSE_SCAN_ID` | DOUBLE | NOT NULL | FK→ | Identifies a scan that is related to this order. |
| 3 | `RAD_DOSE_SCAN_ORDER_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RAD_DOSE_SCAN_ORDER_R table. |
| 4 | `SCAN_SEQ` | DOUBLE | NOT NULL |  | Indicates the order the scans occurred for an order. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `RAD_DOSE_SCAN_ID` | [RAD_DOSE_SCAN](RAD_DOSE_SCAN.md) | `RAD_DOSE_SCAN_ID` |

