# MANUFACTURER_ITEM

> Manufacturer's items

**Description:** Manufacturer Item  
**Table type:** REFERENCE  
**Primary key:** `ITEM_ID`  
**Columns:** 14  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AWP` | DOUBLE |  |  | Average Wholesale Price |
| 2 | `AWP_BULK` | DOUBLE |  |  | AWP Bulk |
| 3 | `AWP_FACTOR` | DOUBLE |  |  | Average Wholesale Price Factor |
| 4 | `COST1` | DOUBLE |  |  | Cost 1 |
| 5 | `COST2` | DOUBLE |  |  | Cost 1 |
| 6 | `ITEM_ID` | DOUBLE | NOT NULL | PK | Primary key inherited from item_definition |
| 7 | `ITEM_MASTER_ID` | DOUBLE | NOT NULL |  | Item Master Identifier |
| 8 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | Manufacturer code value. |
| 9 | `OMF_SUCCESS_IND` | DOUBLE | NOT NULL |  | The value of 0 or 1 indicates the success or failure of the respective OMF table update. 1 indicates update to OMF table was successful and 0 indicates failure. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [DISPENSE_REPLACE_AUDIT](DISPENSE_REPLACE_AUDIT.md) | `REPLACE_MANF_ITEM_ID` |
| [LINE_ITEM](LINE_ITEM.md) | `ORIGINAL_MANUF_ITEM_ID` |
| [MED_PRODUCT](MED_PRODUCT.md) | `MANF_ITEM_ID` |
| [PHA_PROD_DISP_OBS_ST](PHA_PROD_DISP_OBS_ST.md) | `MANF_ITEM_ID` |
| [RECEIPT_LINE_ITEM](RECEIPT_LINE_ITEM.md) | `ACTUAL_MANF_ITEM_ID` |
| [RX_ADMIN_PROD_DISPENSE_HX](RX_ADMIN_PROD_DISPENSE_HX.md) | `MANF_ITEM_ID` |

