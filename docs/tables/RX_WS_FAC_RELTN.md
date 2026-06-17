# RX_WS_FAC_RELTN

> Contains information pertinent to a worksheet at a facility.

**Description:** Pharmacy Worksheet Facility Relation  
**Table type:** REFERENCE  
**Primary key:** `RX_WS_FAC_RELTN_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FAC_CD` | DOUBLE | NOT NULL | FK→ | The facility that the Pharmacy Worksheet is valid for. |
| 2 | `MAINTAIN_RATIO_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the quantity created by the worksheet is directly related to the child item quantities for the parent item. |
| 3 | `PARENT_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item that is created by the worksheet. |
| 4 | `RX_WS_FAC_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that uniquely identifies a row on the RX_WS_FAC_RELTN table. |
| 5 | `RX_WS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the worksheet that is valid at a specific location. |
| 6 | `STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the worksheet for the given facility. (i.e. 'Approved','In Process', etc.) |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FAC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PARENT_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `RX_WS_ID` | [RX_WS](RX_WS.md) | `RX_WS_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_WS_FAC_ITEM_RELTN](RX_WS_FAC_ITEM_RELTN.md) | `RX_WS_FAC_RELTN_ID` |

