# MM_OMF_MFG_ITEM

> Manufacturer item summary table

**Description:** MM OMF MFG ITEM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 53

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_CD` | DOUBLE | NOT NULL |  | active status |
| 2 | `ACTIVE_DT_NBR` | DOUBLE |  |  | Date, in Julian format, this item became active. |
| 3 | `ACTIVE_DT_TM` | DATETIME |  |  | Date and time the row is activated (active indicator is set to 1). |
| 4 | `ACTIVE_ID` | DOUBLE | NOT NULL |  | The ID from the person table that activated the item |
| 5 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 6 | `ACTIVE_MIN_NBR` | DOUBLE |  |  | Stores the minute value of when the item became active. |
| 7 | `AWP` | DOUBLE |  |  | Contains the Average Wholesale Price for the item. |
| 8 | `AWP_BULK` | DOUBLE |  |  | The bulk average wholesale price for this item. |
| 9 | `AWP_FACTOR` | DOUBLE |  |  | Contains the items average wholesale price factor. |
| 10 | `BRAND_NAME` | VARCHAR(100) |  |  | Brand Name of the item. |
| 11 | `COST1` | DOUBLE |  |  | Cost1 - not currently being used. |
| 12 | `COST2` | DOUBLE |  |  | Cost2 - not currently being used. |
| 13 | `CREATE_DT_NBR` | DOUBLE |  |  | A Julian date, number representing the date this item row was created. |
| 14 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 15 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 16 | `CREATE_MIN_NBR` | DOUBLE |  |  | Contains the minute number of when the item row was created. |
| 17 | `DESCRIPTION` | VARCHAR(200) |  |  | textual description of the item |
| 18 | `ITEM_COUNT` | DOUBLE |  |  | Stores an item count. |
| 19 | `ITEM_NBR` | VARCHAR(40) |  |  | An identifying number of the item. |
| 20 | `LAST_DIST_DT_NBR` | DOUBLE |  |  | Stores the items' last distribution date in a Julian format. |
| 21 | `LAST_DIST_DT_TM` | DATETIME |  |  | Stores the date and time of the items' last distribution. |
| 22 | `LAST_DIST_MIN_NBR` | DOUBLE |  |  | Stores the minute value for the items' last distribution. |
| 23 | `LAST_ORDER_CONTRACT_DESC` | VARCHAR(100) |  |  | % lst% |
| 24 | `LAST_ORDER_DT_NBR` | DOUBLE |  |  | Stores the last order date for the item in Julian format. |
| 25 | `LAST_ORDER_DT_TM` | DATETIME |  |  | Stores the date and time of the items' last order. |
| 26 | `LAST_ORDER_MIN_NBR` | DOUBLE |  |  | Stores the minute value for the items last order time. |
| 27 | `LAST_ORDER_PKG_DESC` | VARCHAR(40) |  |  | Stores the Package Description for the items' last order. |
| 28 | `LAST_ORDER_PRICE` | DOUBLE |  |  | Stores the price of the items' last order. |
| 29 | `LAST_ORDER_PRICE_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the type of order price for the items' last order. |
| 30 | `LAST_RECEIPT_DT_NBR` | DOUBLE |  |  | Last Receipt Date, in Julian format, for this item. |
| 31 | `LAST_RECEIPT_DT_TM` | DATETIME |  |  | Date and Time for the Last Receipt for this item. |
| 32 | `LAST_RECEIPT_MIN_NBR` | DOUBLE |  |  | Minute Number Value for the Last Receipt for this item. |
| 33 | `LAST_RECEIPT_PKG_DESC` | VARCHAR(40) |  |  | Package Description for the Last Receipt for this item. |
| 34 | `LAST_REQ_DT_NBR` | DOUBLE |  |  | date, in Julian format, of the last requisition, for this item. |
| 35 | `LAST_REQ_DT_TM` | DATETIME |  |  | Date and time of the last requisition for this item. |
| 36 | `LAST_REQ_MIN_NBR` | DOUBLE |  |  | Minute value for the last requisition for this item. |
| 37 | `LAST_UPDT_DT_NBR` | DOUBLE |  |  | Date, in Julian format of the Last Update for this item. |
| 38 | `LAST_UPDT_DT_TM` | DATETIME |  |  | Date and time of the Last Update for this item. |
| 39 | `LAST_UPDT_ID` | DOUBLE | NOT NULL |  | Identification of the person who performed the Last Update on this item. |
| 40 | `LAST_UPDT_MIN_NBR` | DOUBLE |  |  | Value of the minutes for the Last Update for this item. |
| 41 | `LAST_VOUCHER_DT_NBR` | DOUBLE |  |  | Date, in Julian format, of the Last Voucher for this item. |
| 42 | `LAST_VOUCHER_DT_TM` | DATETIME |  |  | Date and Time of the Last Voucher for this item. |
| 43 | `LAST_VOUCHER_MIN_NBR` | DOUBLE |  |  | Value of the minutes for the Last Voucher for this item. |
| 44 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 45 | `MFG_CD` | DOUBLE | NOT NULL |  | Manufacturer code for the item |
| 46 | `MFG_ITEM_ID` | DOUBLE | NOT NULL |  | Uniquely identifies and Manufacturing Item |
| 47 | `NDC` | VARCHAR(40) |  |  | Uniqule National Drug Code for this item. |
| 48 | `QUICKADD_IND` | DOUBLE |  |  | Indicates whether an item is Quickadd. |
| 49 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 50 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 51 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 52 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 53 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

