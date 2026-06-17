# RX_WS_FAC_ITEM_HX

> Contains the historical reference data about the items on a worksheet at a facility.

**Description:** Pharmacy Worksheet Facility Item History  
**Table type:** REFERENCE  
**Primary key:** `RX_WS_FAC_ITEM_HX_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ITEM_ID` | DOUBLE | NOT NULL |  | The Pharmacy or Supply item needed to create the parent item of the Pharmacy Worksheet, expressed in terms of the quantity unit. |
| 2 | `ITEM_QTY` | DOUBLE | NOT NULL |  | The amount of the Pharmacy or Supply item needed to create the parent item of the Pharmacy Worksheet, expressed in terms of the quantity unit. |
| 3 | `ITEM_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of item. |
| 4 | `MAINTAIN_RATIO_IND` | DOUBLE | NOT NULL |  | Indicates if the quantity of the item needed is directly associated to the number of items created. |
| 5 | `RX_WS_FAC_ITEM_HX_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RX_WS_-FAC_ITEM_HX table. |
| 6 | `RX_WS_FAC_RELTN_HX_ID` | DOUBLE | NOT NULL | FK→ | Unique, generated number that identifies a unique row on the RX_WS_FAC_RELTN_HX table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RX_WS_FAC_RELTN_HX_ID` | [RX_WS_FAC_RELTN_HX](RX_WS_FAC_RELTN_HX.md) | `RX_WS_FAC_RELTN_HX_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_WF_WS_ITEM_RELTN](RX_WF_WS_ITEM_RELTN.md) | `RX_WS_FAC_ITEM_HX_ID` |

