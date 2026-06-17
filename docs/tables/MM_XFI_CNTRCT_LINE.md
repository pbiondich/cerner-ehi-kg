# MM_XFI_CNTRCT_LINE

> Table used to store contract line upload information. Data is moved from this table to MM_CNTRCT_LINE.

**Description:** MM XFI CNTRCT LINE  
**Table type:** REFERENCE  
**Primary key:** `TRANSACTION_ID`  
**Columns:** 51  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACQ_PRICE` | DOUBLE |  |  | Acquisition price |
| 2 | `ACTION_FLAG` | DOUBLE |  |  | Contract line action flag |
| 3 | `ADJ_EXCEMPT_IND` | DOUBLE |  |  | Adjustment exception indicator |
| 4 | `BASE_UOM` | VARCHAR(20) |  |  | base unit of measure value |
| 5 | `BASE_UOM_CD` | DOUBLE | NOT NULL |  | Base unit of measure code |
| 6 | `CAPITAL_CD` | DOUBLE | NOT NULL |  | Contract line capital code, code value |
| 7 | `CAPITAL_CODE` | VARCHAR(60) |  |  | capital code |
| 8 | `CLASS_NODE` | VARCHAR(60) |  |  | class node value |
| 9 | `CLASS_NODE_ID` | DOUBLE | NOT NULL |  | Class Node ID value. |
| 10 | `CNTRCT_LINE_ID` | DOUBLE | NOT NULL | FK→ | contract line identifier |
| 11 | `CNTRCT_MGR` | VARCHAR(60) |  |  | Contract line contract manager |
| 12 | `CNTRCT_MGR_ID` | DOUBLE | NOT NULL | FK→ | Contract line contract manager key |
| 13 | `CNTRCT_PACK_FACTOR` | DOUBLE |  |  | Contract unit of measure package factor |
| 14 | `CNTRCT_PRICE` | DOUBLE |  |  | Contract unit of measure price |
| 15 | `CNTRCT_UOM` | VARCHAR(40) |  |  | Contract unit of measure |
| 16 | `CNTRCT_UOM_CD` | DOUBLE | NOT NULL |  | Contract unit of measure code value |
| 17 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor Source Code value |
| 18 | `COST_CENTER` | VARCHAR(60) |  |  | Contract line cost center |
| 19 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Contract line cost center code value |
| 20 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 21 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the record was created |
| 22 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 24 | `DIST_MARKUP_IND` | DOUBLE |  |  | Distribution markup indicator |
| 25 | `EST_USAGE` | DOUBLE |  |  | Estimated usage |
| 26 | `ITEM_DESC` | VARCHAR(200) |  |  | Item description |
| 27 | `ITEM_NBR` | VARCHAR(200) |  |  | Item number |
| 28 | `LOCATION` | VARCHAR(60) |  |  | Location on the contract line |
| 29 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Code value for the location on the contract line |
| 30 | `MARKUP_PERCENT` | DOUBLE |  |  | Markup percent |
| 31 | `MFR` | VARCHAR(60) |  |  | manufacturer |
| 32 | `MFR_CATALOG_DESC` | VARCHAR(200) |  |  | Manufacturer catalog description |
| 33 | `MFR_CATALOG_NBR` | VARCHAR(200) |  |  | Manufacturer catalog number |
| 34 | `MIN_ORDER_QTY` | DOUBLE |  |  | Minimum order quantity |
| 35 | `MODEL_NBR` | VARCHAR(200) |  |  | Model number |
| 36 | `PROCESS_FLAG` | DOUBLE |  |  | process flag |
| 37 | `PROJECT_CD` | DOUBLE | NOT NULL |  | Contract line project code, code value |
| 38 | `PROJECT_CODE` | VARCHAR(60) |  |  | project code |
| 39 | `REBATE_EXCEMPT_IND` | DOUBLE |  |  | Rebate exception indicator |
| 40 | `SERIAL_NBR` | VARCHAR(200) |  |  | Serial number |
| 41 | `SHORT_DESC` | VARCHAR(200) |  |  | Short description |
| 42 | `TRANSACTION_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 43 | `TRANS_PARENT_ID` | DOUBLE | NOT NULL | FK→ | Transaction parent identifier |
| 44 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 45 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 46 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 47 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 48 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 49 | `UPN` | VARCHAR(200) |  |  | Universal product number |
| 50 | `VENDOR_CATALOG_DESC` | VARCHAR(200) |  |  | Vendor catalog description |
| 51 | `VENDOR_CATALOG_NBR` | VARCHAR(200) |  |  | Vendor catalog number |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNTRCT_LINE_ID` | [MM_CNTRCT_LINE](MM_CNTRCT_LINE.md) | `CNTRCT_LINE_ID` |
| `CNTRCT_MGR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TRANS_PARENT_ID` | [MM_XFI_CNTRCT_HDR](MM_XFI_CNTRCT_HDR.md) | `TRANSACTION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_XFI_CNTRCT_LINE_TIER](MM_XFI_CNTRCT_LINE_TIER.md) | `TRANS_PARENT_ID` |

