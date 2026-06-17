# MM_OMF_ITEM_MASTER

> Item master summary table

**Description:** MM OMF ITEM MASTER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 65

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_CD` | DOUBLE | NOT NULL |  | Contains the value of the items' active code. |
| 2 | `ACTIVE_DT_NBR` | DOUBLE |  |  | Date, in Julian format, this item became active. |
| 3 | `ACTIVE_DT_TM` | DATETIME |  |  | Date and time the row is activated (active indicator is set to 1). |
| 4 | `ACTIVE_ID` | DOUBLE | NOT NULL |  | The ID from the person table that activated the item |
| 5 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 6 | `ACTIVE_MIN_NBR` | DOUBLE |  |  | Stores the minute value of when the item became active. |
| 7 | `APPROVED_IND` | DOUBLE |  |  | Indicates whether an item is approved. |
| 8 | `BASE_PKG_DESC` | VARCHAR(40) |  |  | Stores the items' base package description. |
| 9 | `BASE_PKG_ID` | DOUBLE | NOT NULL | FK→ | Stores the items' base package identifier. |
| 10 | `BASE_PKG_QTY` | DOUBLE |  |  | Stores the items' base package quantity. |
| 11 | `BASE_PKG_UOM_CD` | DOUBLE | NOT NULL |  | Stores the items' base package quantity unit of measure. |
| 12 | `CLASS_NAME` | VARCHAR(60) |  |  | % whare % |
| 13 | `CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | Relates this OMF Item Master to a specific Class Node |
| 14 | `COMPONENT_IND` | DOUBLE |  |  | Indicates whether an item is a component. |
| 15 | `COUNTABLE_IND` | DOUBLE |  |  | Indicates whether an item is countable. |
| 16 | `CREATE_DT_NBR` | DOUBLE |  |  | A Julian date, number representing the date this item row was created. |
| 17 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this entry was created. |
| 18 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of user who created this row |
| 19 | `CREATE_MIN_NBR` | DOUBLE |  |  | Contains the minute number of when the item row was created. |
| 20 | `CRITICAL_IND` | DOUBLE |  |  | Indicates whether an item is critical. |
| 21 | `DESCRIPTION` | VARCHAR(200) |  |  | Stores an item description. |
| 22 | `FDA_REPORTABLE_IND` | DOUBLE |  |  | Indicates whether an item is FDA reportable. |
| 23 | `ITEM_COUNT` | DOUBLE |  |  | Stores an item count. |
| 24 | `ITEM_LEVEL_FLAG` | DOUBLE | NOT NULL |  | This flag indicates the item type, specifically for med def items. |
| 25 | `ITEM_MASTER_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to Item Master |
| 26 | `LAST_DIST_DT_NBR` | DOUBLE |  |  | Stores the items' last distribution date in a Julian format. |
| 27 | `LAST_DIST_DT_TM` | DATETIME |  |  | Stores the date and time of the items' last distribution. |
| 28 | `LAST_DIST_MIN_NBR` | DOUBLE |  |  | Stores the minute value for the items' last distribution. |
| 29 | `LAST_ORDER_CONTRACT_DESC` | VARCHAR(100) |  |  | % lst% |
| 30 | `LAST_ORDER_DT_NBR` | DOUBLE |  |  | Stores the last order date for the item in Julian format. |
| 31 | `LAST_ORDER_DT_TM` | DATETIME |  |  | Stores the date and time of the items' last order. |
| 32 | `LAST_ORDER_MIN_NBR` | DOUBLE |  |  | Stores the minute value for the items last order time. |
| 33 | `LAST_ORDER_PKG_DESC` | VARCHAR(40) |  |  | Stores the Package Description for the items' last order. |
| 34 | `LAST_ORDER_PRICE` | DOUBLE |  |  | Stores the price of the items' last order. |
| 35 | `LAST_ORDER_PRICE_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the type of order price for the items' last order. |
| 36 | `LAST_RECEIPT_DT_NBR` | DOUBLE |  |  | Last Receipt Date, in Julian format, for this item. |
| 37 | `LAST_RECEIPT_DT_TM` | DATETIME |  |  | Date and Time for the Last Receipt for this item. |
| 38 | `LAST_RECEIPT_MIN_NBR` | DOUBLE |  |  | Minute Number Value for the Last Receipt for this item. |
| 39 | `LAST_RECEIPT_PKG_DESC` | VARCHAR(40) |  |  | Package Description for the Last Receipt for this item. |
| 40 | `LAST_REQ_DT_NBR` | DOUBLE |  |  | date, in Julian format, of the last requisition, for this item. |
| 41 | `LAST_REQ_DT_TM` | DATETIME |  |  | Date and time of the last requisition for this item. |
| 42 | `LAST_REQ_MIN_NBR` | DOUBLE |  |  | Minute value for the last requisition for this item. |
| 43 | `LAST_UPDT_DT_NBR` | DOUBLE |  |  | Date, in Julian format of the Last Update for this item. |
| 44 | `LAST_UPDT_DT_TM` | DATETIME |  |  | Date and time of the Last Update for this item. |
| 45 | `LAST_UPDT_ID` | DOUBLE | NOT NULL |  | Identification of the person who performed the Last Update on this item. |
| 46 | `LAST_UPDT_MIN_NBR` | DOUBLE |  |  | Value of the minutes for the Last Update for this item. |
| 47 | `LAST_VOUCHER_DT_NBR` | DOUBLE |  |  | Date, in Julian format, of the Last Voucher for this item. |
| 48 | `LAST_VOUCHER_DT_TM` | DATETIME |  |  | Date and Time of the Last Voucher for this item. |
| 49 | `LAST_VOUCHER_MIN_NBR` | DOUBLE |  |  | Value of the minutes for the Last Voucher for this item. |
| 50 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 51 | `NDC` | VARCHAR(40) |  |  | National Drug Code related number for this item. |
| 52 | `PHA_TYPE_FLAG` | DOUBLE | NOT NULL |  | This flag indicates the pharmacy item type: inpatient, retail or shared. |
| 53 | `QUICKADD_IND` | DOUBLE |  |  | Indicates whether an item is Quickadd. |
| 54 | `REUSABLE_IND` | DOUBLE |  |  | Indicates whether an item is reusable. |
| 55 | `SCHEDUABLE_IND` | DOUBLE |  |  | Indicates whether an item is schedulable. |
| 56 | `SHORT_DESC` | VARCHAR(200) |  |  | Contains a short description of the item. |
| 57 | `STERILE_REQ_IND` | DOUBLE |  |  | Indicates whether Sterilization is required. |
| 58 | `STOCK_NBR` | VARCHAR(40) |  |  | Contains the stock number for the item. |
| 59 | `SYS_ITEM_NBR` | VARCHAR(20) |  |  | Contains the system item number for the item. |
| 60 | `TYPE_CD` | DOUBLE | NOT NULL |  | A code that identifies the type of item. |
| 61 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 62 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 63 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 64 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 65 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BASE_PKG_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `ITEM_MASTER_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

