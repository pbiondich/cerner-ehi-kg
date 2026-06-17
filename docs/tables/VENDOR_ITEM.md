# VENDOR_ITEM

> Child of Item Definition

**Description:** VENDOR ITEM  
**Table type:** REFERENCE  
**Primary key:** `ITEM_ID`  
**Columns:** 11  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ITEM_ID` | DOUBLE | NOT NULL | PK | Primary key inherited from item_definition |
| 2 | `LEAD_TIME` | DOUBLE |  |  | The vendors lead time for this item |
| 3 | `LEAD_TIME_UOM_CD` | DOUBLE | NOT NULL |  | The vendor's lead time unit of measure for this item |
| 4 | `OMF_SUCCESS_IND` | DOUBLE | NOT NULL |  | The value of 0 or 1 indicates the success or failure of the respective OMF table update. 1 indicates update to OMF table was successful and 0 indicates failure. |
| 5 | `PRICE_REVIEW_IND` | DOUBLE |  |  | Indicates that this item has one or more prices in need of review |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VENDOR_CD` | DOUBLE | NOT NULL |  | Code Value for vendor |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [ACQUIREMENT_INFO](ACQUIREMENT_INFO.md) | `PRIMARY_VENDOR_ITEM_ID` |
| [LINE_ITEM](LINE_ITEM.md) | `ORIGINAL_VENDOR_ITEM_ID` |
| [LINE_ITEM](LINE_ITEM.md) | `VENDOR_ITEM_ID` |
| [RECEIPT_LINE_ITEM](RECEIPT_LINE_ITEM.md) | `ACTUAL_VENDOR_ITEM_ID` |

