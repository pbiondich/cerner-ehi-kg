# MM_CNTRCT_LINE

> Used to store the line itetm detail of a contract.

**Description:** Contract Line  
**Table type:** REFERENCE  
**Primary key:** `CNTRCT_LINE_ID`  
**Columns:** 39  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACQ_PRICE` | DOUBLE |  |  | Acquisition price |
| 2 | `ADJ_EXEMPT_IND` | DOUBLE |  |  | Adjustment exempt identifier |
| 3 | `BASE_UOM_CD` | DOUBLE | NOT NULL |  | Base unit of measure code |
| 4 | `CAPITAL_CD` | DOUBLE | NOT NULL |  | Capital Code |
| 5 | `CLASS_NODE_ID` | DOUBLE | NOT NULL |  | Class Node ID value. |
| 6 | `CNTRCT_ID` | DOUBLE | NOT NULL | FK→ | Contract number key |
| 7 | `CNTRCT_LINE_ID` | DOUBLE | NOT NULL | PK | contract line identifier |
| 8 | `CNTRCT_MGR_ID` | DOUBLE | NOT NULL |  | Contract line contract manager key |
| 9 | `CNTRCT_PACK_FACTOR` | DOUBLE |  |  | Contract unit of measure package factor |
| 10 | `CNTRCT_PRICE` | DOUBLE |  |  | Contract unit of measure price |
| 11 | `CNTRCT_UOM_CD` | DOUBLE | NOT NULL |  | Contract unit of measure code value |
| 12 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center code value |
| 13 | `CREATE_APPLCTX` | DOUBLE |  |  | Application which created this row |
| 14 | `CREATE_DT_TM` | DATETIME |  |  | The date and time when the row was inserted |
| 15 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) who inserted the row in to the table. |
| 16 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 17 | `DIST_MARKUP_IND` | DOUBLE |  |  | Distribution markup indicator |
| 18 | `EST_USAGE` | DOUBLE |  |  | Estimated usage |
| 19 | `ITEM_DESC` | VARCHAR(200) |  |  | Item description |
| 20 | `ITEM_NBR` | VARCHAR(200) |  |  | Item number |
| 21 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Code value for the location on the contract line |
| 22 | `MARKUP_PERCENT` | DOUBLE |  |  | Markup percent |
| 23 | `MFR` | VARCHAR(60) |  |  | manufacturer |
| 24 | `MFR_CATALOG_DESC` | VARCHAR(200) |  |  | Manufacturer catalog description |
| 25 | `MFR_CATALOG_NBR` | VARCHAR(200) |  |  | Manufacturer catalog number |
| 26 | `MIN_ORDER_QTY` | DOUBLE |  |  | Minimum order quantity |
| 27 | `MODEL_NBR` | VARCHAR(200) |  |  | Model number |
| 28 | `PROJECT_CD` | DOUBLE | NOT NULL |  | Contract line project code, code value |
| 29 | `REBATE_EXEMPT_IND` | DOUBLE |  |  | Rebate exempt identifier |
| 30 | `SERIAL_NBR` | VARCHAR(200) |  |  | Serial number |
| 31 | `SHORT_DESC` | VARCHAR(200) |  |  | Short description |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPN` | VARCHAR(200) |  |  | Universal product number |
| 38 | `VENDOR_CATALOG_DESC` | VARCHAR(200) |  |  | Vendor catalog description |
| 39 | `VENDOR_CATALOG_NBR` | VARCHAR(200) |  |  | Vendor catalog number |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNTRCT_ID` | [MM_CNTRCT_HDR](MM_CNTRCT_HDR.md) | `CNTRCT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [ITEM_PRICE](ITEM_PRICE.md) | `CONTRACT_LINE_ID` |
| [ITEM_PRICE_HIST](ITEM_PRICE_HIST.md) | `CONTRACT_LINE_ID` |
| [MM_CNTRCT_LINE_TIER](MM_CNTRCT_LINE_TIER.md) | `CNTRCT_LINE_ID` |
| [MM_XFI_CNTRCT_LINE](MM_XFI_CNTRCT_LINE.md) | `CNTRCT_LINE_ID` |

