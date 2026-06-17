# MM_XFI_CNTRCT_HDR

> Table used to store contract header upload information. Data is moved from this table to MM_CNTRCT_HDR.

**Description:** MM XFI CNTRCT HDR  
**Table type:** REFERENCE  
**Primary key:** `TRANSACTION_ID`  
**Columns:** 80  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Action flag for the action |
| 2 | `AGREEMENT_INFO` | VARCHAR(100) |  |  | Agreement information stored at |
| 3 | `CAPITAL_CD` | DOUBLE | NOT NULL |  | Capital code code value |
| 4 | `CAPITAL_CODE` | VARCHAR(60) |  |  | Capital code |
| 5 | `CATALOG_NAME` | VARCHAR(100) |  |  | Catalog name |
| 6 | `CLASS_NODE` | VARCHAR(100) |  |  | Class node value |
| 7 | `CLASS_NODE_ID` | DOUBLE | NOT NULL | FK→ | Class Node ID value. |
| 8 | `CNTRCT_ID` | DOUBLE | NOT NULL | FK→ | Contract number key |
| 9 | `CNTRCT_MGR` | VARCHAR(60) |  |  | Contract manager |
| 10 | `CNTRCT_MGR_ID` | DOUBLE | NOT NULL | FK→ | Contract manager key |
| 11 | `CNTRCT_NAME` | VARCHAR(100) |  |  | Contract name |
| 12 | `CNTRCT_NBR` | VARCHAR(40) | NOT NULL |  | Contract number |
| 13 | `CNTRCT_SRC_TYPE` | VARCHAR(60) |  |  | Contract source type |
| 14 | `CNTRCT_SRC_TYPE_CD` | DOUBLE | NOT NULL |  | Contract source type code value |
| 15 | `CNTRCT_TERM` | VARCHAR(60) |  |  | Contract term |
| 16 | `CNTRCT_TERM_CD` | DOUBLE | NOT NULL |  | Contract term code value |
| 17 | `CNTRCT_TYPE` | VARCHAR(60) |  |  | Contract type |
| 18 | `CNTRCT_TYPE_CD` | DOUBLE | NOT NULL |  | Contract type code value |
| 19 | `CONTRIBUTOR_CD` | DOUBLE | NOT NULL |  | Contributor Source Code value |
| 20 | `COST_CENTER` | VARCHAR(60) |  |  | Cost center value |
| 21 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center code value |
| 22 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 23 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the record was created |
| 24 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 26 | `DESCRIPTION` | VARCHAR(255) |  |  | Contract description |
| 27 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Effective Date and Time value |
| 28 | `END_TRANSACTION_ID` | DOUBLE | NOT NULL |  | end transaction id |
| 29 | `EXCEED_PRICE_IND` | DOUBLE |  |  | Exceed price indicator |
| 30 | `EXECUTED_BY_ORG` | VARCHAR(100) |  |  | Executed by organization |
| 31 | `EXECUTED_BY_VENDOR` | VARCHAR(100) |  |  | Executed by vendor |
| 32 | `EXECUTED_DT_TM` | DATETIME |  |  | Executed date/time |
| 33 | `EXPIRATION_DT_TM` | DATETIME |  |  | Expiration date/time |
| 34 | `EXT_CNTRCT_IND` | DOUBLE |  |  | Extend contract indicator |
| 35 | `EXT_END_DT_TM` | DATETIME |  |  | Extension end date/time |
| 36 | `EXT_NOTE` | VARCHAR(255) |  |  | Extension notes |
| 37 | `EXT_PERIOD` | VARCHAR(60) |  |  | Extension period |
| 38 | `EXT_PERIOD_CD` | DOUBLE | NOT NULL |  | Extension period code value |
| 39 | `EXT_REASON` | VARCHAR(60) |  |  | Extension reason |
| 40 | `EXT_REASON_CD` | DOUBLE | NOT NULL |  | Extension reason code value |
| 41 | `FILL_RATE` | DOUBLE |  |  | Fill rate |
| 42 | `GPO` | VARCHAR(60) |  |  | Group purchasing organization |
| 43 | `GPO_BID_NBR` | VARCHAR(100) |  |  | Group purchasing organization bid number |
| 44 | `GPO_CD` | DOUBLE | NOT NULL |  | Group purchasing organization code value |
| 45 | `GPO_DESCRIPTION` | VARCHAR(255) |  |  | Group purchasing organization description |
| 46 | `GPO_EST_DOLLAR_VALUE` | DOUBLE |  |  | Group purchasing organization estimated dollar value |
| 47 | `GPO_ID_NBR` | VARCHAR(100) |  |  | Group purchasing organization identification number |
| 48 | `GPO_REF_NBR` | VARCHAR(100) |  |  | Group purchasing organization reference number |
| 49 | `HOSPITAL_CONTACT` | VARCHAR(60) |  |  | Hospital contact |
| 50 | `HOSPITAL_CONTACT_ID` | DOUBLE | NOT NULL | FK→ | Hospital contact key |
| 51 | `LEAD_TIME` | DOUBLE |  |  | Lead time |
| 52 | `LOCATION` | VARCHAR(60) |  |  | Location |
| 53 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location code value |
| 54 | `MFR` | VARCHAR(60) |  |  | Manufacturer |
| 55 | `MSTR_AGREEMENT_ID` | DOUBLE | NOT NULL |  | Master agreement key |
| 56 | `MSTR_AGREEMENT_IND` | DOUBLE |  |  | Master agreement indicator |
| 57 | `MSTR_AGREEMENT_NBR` | VARCHAR(40) |  |  | Master agreement number |
| 58 | `PO_ID` | DOUBLE | NOT NULL | FK→ | Purchase order key |
| 59 | `PO_NBR` | VARCHAR(40) |  |  | Purchase order number |
| 60 | `PROCESS_FLAG` | DOUBLE | NOT NULL |  | Process flag |
| 61 | `PROJECT_CD` | DOUBLE | NOT NULL |  | Project code code value |
| 62 | `PROJECT_CODE` | VARCHAR(60) |  |  | project code |
| 63 | `REF_CNTRCT_ID` | DOUBLE | NOT NULL | FK→ | Reference contract number key |
| 64 | `REF_CNTRCT_NBR` | VARCHAR(40) |  |  | Reference contract number |
| 65 | `SCNDRY_VENDOR` | VARCHAR(60) |  |  | Secondary vendor |
| 66 | `SCNDRY_VENDOR_MARKUP` | DOUBLE |  |  | Secondary vendor markup |
| 67 | `SIGNED_BY_ORG` | VARCHAR(100) |  |  | Signed by organization |
| 68 | `SIGNED_BY_VENDOR` | VARCHAR(100) |  |  | Signed by vendor |
| 69 | `START_DT_TM` | DATETIME |  |  | Start date/time |
| 70 | `STATUS` | VARCHAR(60) |  |  | Status |
| 71 | `STATUS_CD` | DOUBLE | NOT NULL |  | Status code value |
| 72 | `TRANSACTION_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 73 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 74 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 75 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 76 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 77 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 78 | `VENDOR` | VARCHAR(60) |  |  | Vendor |
| 79 | `VENDOR_KEY` | VARCHAR(60) |  |  | vendor key |
| 80 | `VENDOR_MARKUP` | DOUBLE |  |  | vendor markup |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLASS_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |
| `CNTRCT_ID` | [MM_CNTRCT_HDR](MM_CNTRCT_HDR.md) | `CNTRCT_ID` |
| `CNTRCT_MGR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `HOSPITAL_CONTACT_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PO_ID` | [PURCHASE_ORDER](PURCHASE_ORDER.md) | `PURCHASE_ORDER_ID` |
| `REF_CNTRCT_ID` | [MM_CNTRCT_HDR](MM_CNTRCT_HDR.md) | `CNTRCT_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [MM_XFI_CNTRCT_ACTION](MM_XFI_CNTRCT_ACTION.md) | `TRANS_PARENT_ID` |
| [MM_XFI_CNTRCT_HDR_TIER](MM_XFI_CNTRCT_HDR_TIER.md) | `TRANS_PARENT_ID` |
| [MM_XFI_CNTRCT_LINE](MM_XFI_CNTRCT_LINE.md) | `TRANS_PARENT_ID` |
| [MM_XFI_CNTRCT_ORG](MM_XFI_CNTRCT_ORG.md) | `TRANS_PARENT_ID` |
| [MM_XFI_CNTRCT_PRICE_ADJ](MM_XFI_CNTRCT_PRICE_ADJ.md) | `TRANS_PARENT_ID` |
| [MM_XFI_CNTRCT_REBATE](MM_XFI_CNTRCT_REBATE.md) | `TRANS_PARENT_ID` |

