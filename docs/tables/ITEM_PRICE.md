# ITEM_PRICE

> Holds an item's price per package type.

**Description:** ITEM PRICE  
**Table type:** REFERENCE  
**Primary key:** `ITEM_PRICE_ID`  
**Columns:** 31  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONTRACT_DESCRIPTION` | VARCHAR(100) |  |  | Contract Description is a free text description field that may be used to describe the associated contract. |
| 6 | `CONTRACT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the contract on the item price table. It is an internal system assigned number. |
| 7 | `CONTRACT_LINE_ID` | DOUBLE | NOT NULL | FK→ | Key to MM_CNTRCT_LINE table |
| 8 | `CONTRACT_NBR` | VARCHAR(40) |  |  | Contract Number |
| 9 | `CONTRACT_TYPE` | VARCHAR(100) |  |  | The contract type may be used to differentiate between different types of contracts. This may be GPO, Supplier, or Manufacturer. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 12 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was inserted. |
| 13 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 14 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 15 | `EFFECTIVE_DT_TM` | DATETIME |  |  | The effective date and time indicate the date and time when this price may become effective. It is used to pre-load contract prices into the system. Prices loaded prior to the effective date of the item price will be loaded with a status of inactive. A program may be run to update this status and "activate" the item price. |
| 16 | `EXPIRATION_DT_TM` | DATETIME |  |  | The expiration date and time indicate the date and time when this price expires. It is used to update expiring contract prices in the system. Prices are updated as of the expiration date of the item price with a status of deleted. A program may be run to update this status and "delete" the expiring item prices. |
| 17 | `FIXED_PRICE_IND` | DOUBLE |  |  | The fixed price indicator is used to identify those prices which are on contract and may not be overridden by the user. |
| 18 | `ITEM_PRICE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the item price table. It is an internal system assigned number. |
| 19 | `MIN_ORDER_QTY` | DOUBLE |  |  | Minimum order quantity for Vendor Item. |
| 20 | `ORDER_QTY_MULTIPLE` | DOUBLE |  |  | The order quantity multiple is a quantity which will be used to determine how many economic order quantity units should be automatically reordered. This is not currently implemented. |
| 21 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization associated to the price |
| 22 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the package type table. It is an internal system assigned number. |
| 23 | `PRICE` | DOUBLE | NOT NULL |  | This is the price associated with the price type and package type of the vendor item selected. |
| 24 | `PRICE_QUOTE_SOURCE` | VARCHAR(100) |  |  | The price quote source indicates who quoted the price. |
| 25 | `PRICE_TYPE_CD` | DOUBLE | NOT NULL |  | The Price Type code is used to identify whether the price is quoted, contract, or list type. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 31 | `VENDOR_PRICE_SCHEDULE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the vendor price schedule table. It is an internal system assigned number used to differentiate between prices at locations. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRACT_LINE_ID` | [MM_CNTRCT_LINE](MM_CNTRCT_LINE.md) | `CNTRCT_LINE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ITEM_PRICE_HIST](ITEM_PRICE_HIST.md) | `ITEM_PRICE_ID` |
| [MM_XFI_ITEM](MM_XFI_ITEM.md) | `PRICE_ID` |

