# MM_CNTRCT_HDR

> Table used to store contract header information

**Description:** MM CNTRCT HDR  
**Table type:** REFERENCE  
**Primary key:** `CNTRCT_ID`  
**Columns:** 71  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AGREEMENT_INFO` | VARCHAR(100) |  |  | agreement information |
| 2 | `CAPITAL_CD` | DOUBLE | NOT NULL |  | Capital code code value |
| 3 | `CATALOG_NAME` | VARCHAR(100) |  |  | Catalog name |
| 4 | `CLASS_NODE_ID` | DOUBLE | NOT NULL |  | Class Node ID value. |
| 5 | `CNTRCT_ID` | DOUBLE | NOT NULL | PK | Contract number key |
| 6 | `CNTRCT_MGR_ID` | DOUBLE | NOT NULL |  | Contract manager key |
| 7 | `CNTRCT_NAME` | VARCHAR(100) |  |  | Contract name |
| 8 | `CNTRCT_NBR` | VARCHAR(40) | NOT NULL |  | Contract number |
| 9 | `CNTRCT_NBR_KEY` | VARCHAR(40) | NOT NULL |  | contract number key |
| 10 | `CNTRCT_NBR_KEY_A_NLS` | VARCHAR(160) |  |  | CNTRCT_NBR_KEY_A_NLS column |
| 11 | `CNTRCT_NBR_KEY_NLS` | VARCHAR(40) | NOT NULL |  | contract number key nls |
| 12 | `CNTRCT_SRC_TYPE_CD` | DOUBLE | NOT NULL |  | Contract source type code value |
| 13 | `CNTRCT_TERM_CD` | DOUBLE | NOT NULL |  | Contract term code value |
| 14 | `CNTRCT_TYPE_CD` | DOUBLE | NOT NULL |  | Contract type code value |
| 15 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center code value |
| 16 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 17 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was inserted. |
| 18 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) who inserted the row in to the table. |
| 19 | `CREATE_TASK` | DOUBLE |  |  | Task which created this row |
| 20 | `DESCRIPTION` | VARCHAR(255) |  |  | Contract description |
| 21 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Effective Date and Time value |
| 22 | `EXCEED_PRICE_IND` | DOUBLE |  |  | Exceed price indicator |
| 23 | `EXECUTED_BY_ORG` | VARCHAR(100) |  |  | Executed by organization |
| 24 | `EXECUTED_BY_VENDOR` | VARCHAR(100) |  |  | Executed by vendor |
| 25 | `EXECUTED_DT_TM` | DATETIME |  |  | Executed date/time |
| 26 | `EXPIRATION_DT_TM` | DATETIME |  |  | Expiration date/time |
| 27 | `EXT_CNTRCT_IND` | DOUBLE |  |  | Extend contract indicator |
| 28 | `EXT_END_DT_TM` | DATETIME |  |  | Extension end date/time |
| 29 | `EXT_NOTE` | VARCHAR(255) |  |  | Extension notes |
| 30 | `EXT_PERIOD_CD` | DOUBLE | NOT NULL |  | Extension period code value |
| 31 | `EXT_REASON_CD` | DOUBLE | NOT NULL |  | Extension reason code value |
| 32 | `EXT_START_DT_TM` | DATETIME |  |  | extension start date and time |
| 33 | `FILL_RATE` | DOUBLE |  |  | Fill rate |
| 34 | `FREIGHT_TERMS_CD` | DOUBLE | NOT NULL |  | Freight Terms |
| 35 | `GPO_BID_NBR` | VARCHAR(100) |  |  | Group purchasing organization bid number |
| 36 | `GPO_CD` | DOUBLE | NOT NULL |  | Group purchasing organization code value |
| 37 | `GPO_DESCRIPTION` | VARCHAR(255) |  |  | Group purchasing organization description |
| 38 | `GPO_EST_DOLLAR_VALUE` | DOUBLE |  |  | Group purchasing organization estimated dollar value |
| 39 | `GPO_ID_NBR` | VARCHAR(100) |  |  | Group purchasing organization identification number |
| 40 | `GPO_REF_NBR` | VARCHAR(100) |  |  | Group purchasing organization reference number |
| 41 | `HOSPITAL_CONTACT_ID` | DOUBLE | NOT NULL |  | Hospital contact key |
| 42 | `LEAD_TIME` | DOUBLE |  |  | Lead time |
| 43 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Code value for the location on the contract line |
| 44 | `MFR` | VARCHAR(60) |  |  | manufacturer |
| 45 | `MFR_ADDRESS` | VARCHAR(255) |  |  | manufacturer address |
| 46 | `MIN_ORDER_COST` | DOUBLE |  |  | Minimum ordering cost |
| 47 | `MSTR_AGREEMENT_ID` | DOUBLE | NOT NULL |  | Master agreement key |
| 48 | `MSTR_AGREEMENT_IND` | DOUBLE |  |  | Master agreement indicator |
| 49 | `PAYMENT_TERMS_CD` | DOUBLE | NOT NULL |  | Payment Terms |
| 50 | `PRODUCT_LEVEL` | DOUBLE |  |  | Header price tier product level |
| 51 | `PROJECT_CD` | DOUBLE | NOT NULL |  | Contract line project code, code value |
| 52 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL |  | Foreign key to the purchase order table. |
| 53 | `REF_CNTRCT_ID` | DOUBLE | NOT NULL |  | Reference contract number key |
| 54 | `SCNDRY_VENDOR` | VARCHAR(60) |  |  | Secondary vendor |
| 55 | `SCNDRY_VENDOR_MARKUP` | DOUBLE |  |  | Secondary vendor markup |
| 56 | `SHIP_VIA_CD` | DOUBLE | NOT NULL |  | Ship Via Code |
| 57 | `SIGNED_BY_ORG` | VARCHAR(100) |  |  | Signed by organization |
| 58 | `SIGNED_BY_VENDOR` | VARCHAR(100) |  |  | Signed by vendor |
| 59 | `SIGNED_DT_TM` | DATETIME |  |  | This indicated the date n time at which the document is signed. |
| 60 | `START_DT_TM` | DATETIME |  |  | Start date/time |
| 61 | `STATUS_CD` | DOUBLE | NOT NULL |  | Status code value |
| 62 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 63 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 64 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 65 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 66 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 67 | `VENDOR` | VARCHAR(60) |  |  | Vendor. |
| 68 | `VENDOR_ADDRESS` | VARCHAR(255) |  |  | vendor address |
| 69 | `VENDOR_KEY` | VARCHAR(60) |  |  | vendor key |
| 70 | `VENDOR_MARKUP` | DOUBLE |  |  | vendor markup |
| 71 | `VENDOR_TYPE_CD` | DOUBLE | NOT NULL |  | Type of vendor |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (9)

| From table | Column |
|------------|--------|
| [MM_CNTRCT_ACTION](MM_CNTRCT_ACTION.md) | `CNTRCT_ID` |
| [MM_CNTRCT_HDR_TIER](MM_CNTRCT_HDR_TIER.md) | `CNTRCT_ID` |
| [MM_CNTRCT_LINE](MM_CNTRCT_LINE.md) | `CNTRCT_ID` |
| [MM_CNTRCT_ORG](MM_CNTRCT_ORG.md) | `CNTRCT_ID` |
| [MM_CNTRCT_PRICE_ADJ](MM_CNTRCT_PRICE_ADJ.md) | `CNTRCT_ID` |
| [MM_CNTRCT_REBATE](MM_CNTRCT_REBATE.md) | `CNTRCT_ID` |
| [MM_CNTRCT_SIGNATURE](MM_CNTRCT_SIGNATURE.md) | `CNTRCT_ID` |
| [MM_XFI_CNTRCT_HDR](MM_XFI_CNTRCT_HDR.md) | `CNTRCT_ID` |
| [MM_XFI_CNTRCT_HDR](MM_XFI_CNTRCT_HDR.md) | `REF_CNTRCT_ID` |

