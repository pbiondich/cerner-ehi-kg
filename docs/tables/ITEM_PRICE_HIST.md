# ITEM_PRICE_HIST

> Store history of price modifications to the ITEM_PRICE table.

**Description:** Item Price History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONTRACT_DESCRIPTION` | VARCHAR(100) |  |  | Contract Description is a free text description field that may be used to describe the associated contract. |
| 6 | `CONTRACT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the contract on the item price table. It is an internal system assigned number. |
| 7 | `CONTRACT_LINE_ID` | DOUBLE | NOT NULL | FK→ | Key to MM_CNTRCT_LINE table |
| 8 | `CONTRACT_NBR` | VARCHAR(40) |  |  | Contract Number from MM_CNTRCT_HDR |
| 9 | `CONTRACT_TYPE` | VARCHAR(100) |  |  | The contract type may be used to differentiate between different types of contracts. This may be GPO, Supplier, or Manufacturer. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the record was created. |
| 13 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that created the row in the table. |
| 14 | `CREATE_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted the row. |
| 15 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Effective Date and Time value |
| 16 | `EXPIRATION_DT_TM` | DATETIME |  |  | The expiration date and time indicate the date and time when this price expires. It is used to update expiring contract prices in the system. Prices are updated as of the expiration date of the item price with a status of deleted. A program may be run to update this status and "delete" the expiring item prices. |
| 17 | `FIXED_PRICE_IND` | DOUBLE | NOT NULL |  | The fixed price indicator is used to identify those prices which are on contract and may not be overridden by the user. |
| 18 | `ITEM_PRICE_HIST_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the ITEM_PRICE_HIST table. |
| 19 | `ITEM_PRICE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to item_price table |
| 20 | `MIN_ORDER_QTY` | DOUBLE |  |  | Minimum order quantity for Vendor Item. |
| 21 | `ORDER_QTY_MULTIPLE` | DOUBLE |  |  | The order quantity multiple is a quantity which will be used to determine how many economic order quantity units should be automatically reordered. This is not currently implemented. |
| 22 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization associated to the price |
| 23 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the package type table. It is an internal system assigned number. |
| 24 | `PRICE` | DOUBLE | NOT NULL |  | This is the price associated with the price type and package type of the vendor item selected. |
| 25 | `PRICE_QUOTE_SOURCE` | VARCHAR(100) |  |  | The price quote source indicates who quoted the price. |
| 26 | `PRICE_TYPE_CD` | DOUBLE | NOT NULL |  | The Price Type code is used to identify whether the price is quoted, contract, or list type. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 32 | `VENDOR_PRICE_SCHEDULE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the vendor price schedule table. It is an internal system assigned number used to differentiate between prices at locations. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTRACT_LINE_ID` | [MM_CNTRCT_LINE](MM_CNTRCT_LINE.md) | `CNTRCT_LINE_ID` |
| `ITEM_PRICE_ID` | [ITEM_PRICE](ITEM_PRICE.md) | `ITEM_PRICE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

